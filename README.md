## Social Network and Text Analysis of Debates in the UK House of Commons (58th Parliament)

This repository contains the code and analysis for the project “Social Network and Text Analysis of Debates in the House of Commons of the 58th Parliament of the United Kingdom”, developed as part of the DTU course [02805 Social Graphs and Interactions](https://kurser.dtu.dk/course/02805).

The project accompanies the paper:

Social Network and Text Analysis of Debates in the House of Commons of the 58th Parliament of the United Kingdom

Meike Hanneke Röelle Bosa¹, Max Bürkner¹², Gerard Ramos Pomar¹

Compiled December 10, 2025

¹ DTU Compute, Technical University of Denmark

² Correspondence: s252890@dtu.dk

## 📌 Overview

This project analyzes parliamentary debates from the UK’s 58th House of Commons (2019–2024) through:

Interaction network reconstruction using a large language model classifier to detect MP-to-MP exchanges.

Network analysis (centrality, backbone extraction, degree distributions) to identify structural patterns in parliamentary debate.

Community detection to uncover groups of MPs who interact more frequently, revealing clusters based on policy expertise rather than party lines.

Text and word-frequency analysis to infer community-level topics such as defence, housing, foreign affairs, environment, and more.

Sentiment analysis to examine:

Emotional tone across MPs

Influence of particularly positive or negative MPs

Longitudinal trends in parliamentary sentiment over the full term

## 🔍 Key Findings (as described in the paper)

The interaction network is dense, with heavy-tailed interaction intensities indicating a few highly active MP pairs.

Central figures such as Boris Johnson, Rishi Sunak, Matt Hancock, and Liz Truss dominate the network structure.

Community detection reveals around 12 moderately cohesive communities, driven by expertise and policy focus, not party membership.

Word-frequency analysis shows clear topical clusters (e.g. defence, education & COVID, environment, housing regulation).

Sentiment across MPs is generally neutral with low variance, but emotional tone significantly shifts in response to highly positive or negative MPs.

Over the full parliamentary term, sentiment trends slightly downward, suggesting a gradual worsening emotional climate.

## 📁 Repository Contents

data/ — Raw and processed parliamentary transcripts

notebooks/ — Jupyter notebooks for network extraction, analysis, and visualization

src/ — Source code for:

LLM-based interaction extraction

Network construction

Community detection and topic modelling

Sentiment analysis

figures/ — Selected plots used in the paper

paper/ — LaTeX source (if included)

## 🛠️ Methods & Tools

Large Language Models for MP-to-MP interaction extraction

NetworkX for graph construction and analysis

Louvain algorithm for community detection

Word-frequency overuse scoring for topic inference

Sentiment analysis using a lexicon-based classifier

Backbone extraction using high-salience skeletons and edge betweenness

## 📄 Citation

If you use this repository, please cite the accompanying paper:

Röelle Bosa, M. H., Bürker, M., & Ramos Pomar, G. (2025). Social Network and Text Analysis of Debates in the House of Commons of the 58th Parliament of the United Kingdom. DTU Compute.

## 📬 Contact

For questions, please reach out to:

Max Bürkner — s252890@dtu.dk

Technical University of Denmark (DTU)
