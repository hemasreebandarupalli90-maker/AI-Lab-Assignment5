# AI-Lab-Assignment5
# Hemasree
# SE24UCSE045

Overview
This repository contains implementations of important Artificial Intelligence concepts including search algorithms, intelligent planning systems, knowledge representation, and probabilistic reasoning.

Projects Included
Search Algorithms Implementation
Test Cases for Search Algorithms
AI-Based Travel Planner
Knowledge Graph Implementation
Bayesian Network Implementation
1. Search Algorithms Implementation
Objective
To implement and compare various AI search algorithms using the Tic-Tac-Toe game environment.

Algorithms Implemented
Minimax Search Algorithm
Alpha-Beta Pruning
Heuristic Alpha-Beta Search
Monte Carlo Tree Search (MCTS)
Description
This project demonstrates how AI agents make intelligent decisions in a game environment. Tic-Tac-Toe is used as the testing platform where each algorithm selects the most optimal move based on the current board state.

Minimax Algorithm
The Minimax algorithm explores all possible game states and chooses the move that maximizes the player’s winning chances while minimizing the opponent’s advantage.

Alpha-Beta Pruning
Alpha-Beta pruning improves the efficiency of Minimax by eliminating unnecessary branches during the search process.

Heuristic Alpha-Beta Search
This approach combines heuristic evaluation with depth-limited search to improve performance and reduce computation time.

Monte Carlo Tree Search (MCTS)
MCTS performs multiple random simulations to estimate the best move based on success probability.

Files
search_algorithms.py
test_search_algorithms.py
How to Run
python search_algorithms.py
python test_search_algorithms.py
Expected Output
The algorithms should generate valid and optimal moves according to the Tic-Tac-Toe board configuration.

2. Test Cases for Search Algorithms
Objective
To validate the correctness and efficiency of the implemented search algorithms.

Description
Different Tic-Tac-Toe board states are tested to evaluate the behavior of Minimax, Alpha-Beta Search, Heuristic Alpha-Beta Search, and MCTS.

Test Cases
Winning move detection
Opponent blocking
Empty board evaluation
Draw state handling
How to Run
python test_search_algorithms.py
Expected Output
All algorithms should return correct and valid moves for the given test cases.

3. AI-Based Travel Planner
Objective
To design an intelligent travel planning system using a predefined travel knowledge base.

Description
The system generates personalized travel recommendations based on user preferences such as budget, travel interests, food preferences, and trip duration.

Features
Tourist place recommendations
Food suggestions
Budget-based hotel recommendations
Cost estimation
Personalized travel itinerary generation
Knowledge Base
The system contains information about:

Tourist attractions
Food specialties
Hotel categories
Transportation facilities
Cities Included
Hyderabad
Visakhapatnam
Bengaluru
User Inputs
Destination city
Budget
Number of days
Travel interests
Food preferences
Outputs
Recommended tourist places
Food suggestions
Estimated travel expenses
Personalized travel plan
How to Run
python travel_planner.py
Expected Output
The system generates a customized travel itinerary along with recommendations and estimated cost.

4. Knowledge Graph Implementation
Objective
To explore knowledge representation and relationship mapping using Knowledge Graphs.

Description
This project models relationships between cities, tourist attractions, food items, and transportation systems using graph structures.

Example Relationships
Hyderabad → has_place → Charminar
Hyderabad → has_food → Hyderabadi Biryani
Hyderabad → has_transport → Metro
Features
Knowledge representation
Relationship mapping
Information retrieval
Graph exploration
Tools Explored
Neo4j
RDFLib
Protégé
GraphDB
NetworkX
How to Run
python knowledge_graphs.py
Expected Output
The system displays graph-based relationships between cities, tourist places, food recommendations, and transportation facilities.

5. Bayesian Network Implementation
Objective
To understand probabilistic reasoning and inference using Bayesian Networks.

Description
This project demonstrates a disease diagnosis system using Bayesian Networks with symptoms such as fever, cough, and fatigue.

Problem Representation
Disease → Fever
Disease → Cough
Disease → Fatigue
Inference
The system predicts disease probability based on observed symptoms using probabilistic inference techniques.

Tools Explored
pgmpy
GeNIe
Netica
BayesiaLab
bnlearn
Requirements
pip install pgmpy
How to Run
python bayesian_networks.py
Expected Output
The system performs probabilistic inference and predicts disease likelihood based on user symptoms.

Conclusion
These projects demonstrate practical applications of Artificial Intelligence concepts such as search algorithms, intelligent planning, knowledge representation, graph-based reasoning, and probabilistic inference. The implementations highlight how AI techniques can be applied to solve real-world problems involving decision-making, planning, reasoning, and prediction.
