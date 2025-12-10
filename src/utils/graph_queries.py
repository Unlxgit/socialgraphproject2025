import utils.sentiment_utils as sentiment_utils

def get_member_contributions(G, member_id): 
    outgoing_contributions = get_member_outgoing_contributions(G, member_id)
    ingoing_contributions  = get_member_ingoing_contributions(G, member_id)
    
    return outgoing_contributions + ingoing_contributions


def get_member_outgoing_contributions(G, member_id):
    member_contributions = []
    
    for edge in list(G.out_edges(member_id, data=True)):
        edge_data = edge[2]    
        for interaction in edge_data["interactions"]:
            contribution = interaction["utterances"][member_id]
            member_contributions.append(contribution)

    return member_contributions


def get_member_ingoing_contributions(G, member_id):
    member_contributions = []
    
    for edge in list(G.in_edges(member_id, data=True)):
        edge_data = edge[2]    
        for interaction in edge_data["interactions"]:
            contribution = interaction["utterances"][member_id]
            member_contributions.append(contribution)

    return member_contributions


def get_member_contributions_directed_to(G, member_id, directed_to_member_id):
    member_contributions = []
    edge_data = G.get_edge_data(member_id, directed_to_member_id)

    if edge_data:
        for interaction in edge_data["interactions"]:
            contribution = interaction["utterances"][member_id]
            member_contributions.append(contribution)
    
        return member_contributions
    

def calculate_all_politicians_average_sentiment(G, sentiment_values_dict):
    average_politician_sentiment = {}
    
    for i, node in enumerate(G.nodes):
        if len(list(G.edges(node))) > 0:
            contributions = get_member_contributions(G, node)
            sentiment_value = sentiment_utils.calculate_text_list_sentiment(contributions, sentiment_values_dict)
    
            average_politician_sentiment[node] = sentiment_value
    
        if i % 250 == 0:
            print(str(i) + "/" + str(len(list(G.nodes))))
    
    print(str(len(list(G.nodes))) + "/" + str(len(list(G.nodes))))
    return average_politician_sentiment



def calc_avg_sentiment_against_extreme_politicians_list(G, politicians_list, sentiment_values_dict):    
    sentiment_against_politician_list =  []
    
    for extreme_member_id, sentiment in politicians_list:
        contributions_against_member = []
        
        for member_id in list(G.nodes):
            if member_id in politicians_list:
                continue
                
            contributions = get_member_contributions_directed_to(G, member_id, extreme_member_id)
                
            if contributions:
                contributions_against_member += contributions


        if (len(contributions_against_member)) >= 10:
            sentiment_against_politician = sentiment_utils.calculate_text_list_sentiment(contributions_against_member, sentiment_values_dict)            
            sentiment_against_politician_list.append(sentiment_against_politician)
    

    return sentiment_against_politician_list
    