import streamlit as st

# --- Title ---
st.title("Breadth First Search (BFS) and Depth First Search (DFS) Visualisation")
st.markdown("Select a starting point and choose which algorithm to run.")

# --- Display image ---
st.image("LabReport_BSD2513_#1.jpg", caption="Graph Respresentation", use_container_width=True)

# --- Graph ---
graph = {
    'A': ['D', 'B'],
    'B': ['C', 'A', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['F', 'G']
}

nodes = list(graph.keys())  # ['A','B','C','D','E','F','G','H']


# --- BFS Function ---
def bfs(graph, start_node):
    visited = []
    queue = []
    traversal_order = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        traversal_order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return traversal_order


# --- DFS Function ---
def dfs(graph, start_node):
    visited = set()
    traversal_order = []

    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbour in graph[node]:
                dfs_recursive(neighbour)

    dfs_recursive(start_node)
    return traversal_order


# --- Streamlit Controls ---
st.subheader("Choose Options")

start_node = st.selectbox("Select Starting Node:", nodes)

algorithm = st.radio(
    "Choose Algorithm:",
    ("Breadth First Search (BFS)", "Depth First Search (DFS)")
)

# --- Run button ---
if st.button("Run Algorithm"):
    if algorithm == "Breadth First Search (BFS)":
        result = bfs(graph, start_node)
    else:
        result = dfs(graph, start_node)
    
    st.success(f"Traversal Order: {' → '.join(result)}")

