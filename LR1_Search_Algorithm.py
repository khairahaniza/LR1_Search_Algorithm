import streamlit as st

# --- Title ---
st.title("Breadth First Search (BFS) and Depth First Search (DFS) Visualisation")
st.markdown("Select a starting point and choose which algorithm to run.")

# --- Display image ---
st.image("LabReport_BSD2513_#1.jpg", caption="Graph Respresentation", use_container_width=True)

graph = {
  'A' : ['B','D'],
  'B' : ['C', 'E','G'],
  'C' : ['A'],
  'D' : ['C'],
  'E' : ['H'],
  'F' : [],
  'G' : ['F'],
  'H' : ['G','F']
}


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
