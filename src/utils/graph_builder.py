import networkx as nx
import json
from datetime import datetime


def _add_nodes_to_graph(G, data):
    for member_id, member_data in data["nodes"].items():
        G.add_node(int(member_id), **member_data)
    return G

def _add_edges_to_graph(G, data, threshold=1):
    for interaction in data["interactions"]:
        speaker1_id = interaction["speaker1_member_id"]
        speaker2_id = interaction["speaker2_member_id"]

        if speaker1_id == speaker2_id:
            continue

        interaction_data = {
            "utterances": {
                speaker1_id: interaction["speaker1_text"],
                speaker2_id: interaction["speaker2_text"],
            },
            "debate_data": {
                "debate_id":   interaction["debate_id"],
                "debate_date": interaction["debate_date"],
                "location":    interaction["Location"],
                "title":       interaction["Title"],
            },
        }

        if G.has_edge(speaker1_id, speaker2_id):
            G[speaker1_id][speaker2_id]['weight'] += 1
            G[speaker1_id][speaker2_id]['interactions'].append(interaction_data)
        else:
            G.add_edge(speaker1_id, speaker2_id, weight=1, interactions=[interaction_data])

    if threshold > 1:
        edges_to_remove = [
            (u, v)
            for u, v, d in G.edges(data=True)
            if d.get("weight", 0) < threshold
        ]
        G.remove_edges_from(edges_to_remove)

    return G


def _filter_isolated_graph(G):
    isolated = [n for n in G.nodes() if G.degree(n) == 0]
    G.remove_nodes_from(isolated)
    return G


def _get_session_data(start_date, end_date, data):
    """Return only interactions that fall within a session date range."""
    sd = datetime.fromisoformat(start_date)
    ed = datetime.fromisoformat(end_date)

    session_interactions = []
    for inter in data["interactions"]:
        inter_date = datetime.fromisoformat(inter["debate_date"])
        if sd <= inter_date <= ed:
            session_interactions.append(inter)

    return {
        "nodes": data["nodes"],
        "interactions": session_interactions
    }


def build_full_graph(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
    
    G = nx.DiGraph()
    G = _add_nodes_to_graph(G, data)
    G = _add_edges_to_graph(G, data, threshold=1)
    G = _filter_isolated_graph(G)

    return G


def build_multiple_session_graphs(file, dates, threshold=1):
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)

    G_sessions = {y: nx.DiGraph() for y in range(1,5)}

    i = 1
    for start_date, end_date in dates:
        session_data = _get_session_data(start_date, end_date, data)
    
        G = nx.DiGraph()
        G = _add_nodes_to_graph(G, session_data)
        G = _add_edges_to_graph(G, session_data, threshold=threshold)
        G = _filter_isolated_graph(G)

        G_sessions[i] = G
        i += 1

    return G_sessions




def add_party_grouped_attribute(G):
    party_map = {
        "Labour": "Labour",
        "Labour (Co-op)": "Labour",
        "Conservative": "Conservative",
        "Liberal Democrat": "Liberal Democrat",
        "Scottish National Party": "Scottish National Party",
        "Independent": "Independent"
    }
    for node, attrs in G.nodes(data=True):
        original_party = attrs.get("Party")
        if original_party is not None:
            G.nodes[node]["Party_Grouped"] = party_map.get(original_party, "Other")
