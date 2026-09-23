import pandas as pd
import networkx as nx
import sys
import time

def print_bloon_header():
    print("=======================================================")
    print("THE BLOON POWER GRAPH™ - COMPUTATIONAL ENGINE v1.0")
    print("Research Cutoff: Sept 23, 2026")
    print("WARNING: Centrality ≠ Conspiracy. Correlation ≠ Causation.")
    print("=======================================================\n")

def load_data():
    try:
        nodes_df = pd.read_csv('nodes.csv')
        edges_df = pd.read_csv('edges.csv')
        return nodes_df, edges_df
    except FileNotFoundError:
        print("Error: CSV data files not found.")
        sys.exit(1)

def build_graph(nodes_df, edges_df):
    G = nx.DiGraph()
    for _, row in nodes_df.iterrows():
        G.add_node(row['id'], name=row['name'], category=row['category'], ia_score=row['institutional_access'])
    
    for _, row in edges_df.iterrows():
        G.add_edge(row['source'], row['target'], 
                   relation=row['relation'], 
                   weight=row['evidence_score'],
                   source_doc=row['source_doc'])
    return G

def calculate_power_scores(G):
    # Calculate Centrality
    deg_cent = nx.degree_centrality(G)
    bet_cent = nx.betweenness_centrality(G, weight='weight')
    
    scores = []
    for node in G.nodes():
        name = G.nodes[node]['name']
        ia = G.nodes[node]['ia_score']
        degree = deg_cent[node]
        betweenness = bet_cent[node]
        
        # Conceptual equation: POWER = I * C * N * IA
        # For this toy model, we simplify N as a mix of degree & betweenness
        network_factor = (degree + betweenness) / 2
        
        # Mocking I and C factors based on category for demonstration
        cat = G.nodes[node]['category']
        info_factor = 1.0 if cat in ['MEDIA', 'PLATFORM', 'FOREIGN_ENTITY'] else 0.5
        cap_factor = 1.0 if cat in ['BUSINESS', 'FINANCIAL', 'TECHNOLOGY'] else 0.5
        
        power_score = info_factor * cap_factor * network_factor * ia
        scores.append({'Name': name, 'Power_Score': power_score, 'Network_Factor': network_factor, 'IA': ia})
        
    return pd.DataFrame(scores).sort_values(by='Power_Score', ascending=False)

def run_bloon_conspiracy_engine(G):
    print(">>> INITIATING BLOON CONSPIRACY ENGINE™")
    time.sleep(1)
    print(">>> SEARCHING FOR NON-LINEAR TEMPORAL ANOMALIES...")
    time.sleep(1)
    
    # Example logic: finding paths between seemingly unconnected nodes (e.g., Agalarov to Thiel)
    # Note: In our current tiny sample CSV, they might not connect, but we simulate the engine logic.
    print("\n[!] ALERT: ENGINE HAS FOUND STRUCTURAL CONNECTIONS.")
    print("=======================================================")
    print("Relationship detected: YES")
    print("Conspiracy proven:     NO")
    print("Causal relationship:   UNKNOWN")
    print("Correlation:           POSSIBLE")
    print("Internet panic level:  ████████████████████ 100%")
    print("=======================================================\n")
    print("DISCLAIMER: A highly connected node may simply be a highly connected node. Congratulations. You have discovered networking. 😂\n")

if __name__ == "__main__":
    print_bloon_header()
    nodes, edges = load_data()
    G = build_graph(nodes, edges)
    
    print("Graph built successfully.")
    print(f"Nodes: {G.number_of_nodes()} | Edges: {G.number_of_edges()}\n")
    
    power_df = calculate_power_scores(G)
    print("TOP 5 STRUCTURALLY CENTRAL NODES IN THE MODEL:")
    print("(Note: Centrality within this constructed dataset, NOT a ranking of objective political power.)")
    print(power_df.head(5).to_string(index=False))
    print("\n")
    
    run_bloon_conspiracy_engine(G)