```python
# Knowledge Graph Representation

knowledge_graph = {

    "Hyderabad": {

        "has_place": [
            "Charminar",
            "Golconda Fort",
            "Hussain Sagar"
        ],

        "has_food": [
            "Hyderabadi Biryani",
            "Irani Chai"
        ],

        "has_transport": [
            "Metro",
            "Bus",
            "Cab"
        ]
    },

    "Bengaluru": {

        "has_place": [
            "Cubbon Park",
            "Lalbagh",
            "Bangalore Palace"
        ],

        "has_food": [
            "Masala Dosa",
            "Filter Coffee"
        ],

        "has_transport": [
            "Metro",
            "Bus",
            "Cab"
        ]
    },

    "Visakhapatnam": {

        "has_place": [
            "RK Beach",
            "Kailasagiri",
            "Yarada Beach"
        ],

        "has_food": [
            "Seafood",
            "Fish Curry"
        ],

        "has_transport": [
            "Bus",
            "Cab",
            "Train"
        ]
    }
}


# Function to Display Knowledge Graph Information

def show_knowledge_graph(city):

    if city not in knowledge_graph:
        print("City not found in Knowledge Graph")
        return

    print("\n========== KNOWLEDGE GRAPH ==========")
    print("City:", city)

    print("\nTourist Places:")
    for place in knowledge_graph[city]["has_place"]:
        print("-", place)

    print("\nFood Recommendations:")
    for food in knowledge_graph[city]["has_food"]:
        print("-", food)

    print("\nTransport Options:")
    for transport in knowledge_graph[city]["has_transport"]:
        print("-", transport)


# Example Usage

city = "Hyderabad"

show_knowledge_graph(city)


# Tools Used for Knowledge Graphs

print("\n========== TOOLS USED ==========")

tools = [
    "Neo4j",
    "RDFLib",
    "Protégé",
    "GraphDB",
    "NetworkX"
]

for i, tool in enumerate(tools, start=1):
    print(f"{i}. {tool}")
```
