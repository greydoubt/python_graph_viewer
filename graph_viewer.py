import graphviz

# Define the graph in DOT format
graph = graphviz.Digraph()
graph.attr(rankdir='LR') # sets the direction of the graph to left-to-right

graph.node('A')
graph.node('B')
graph.node('C')
graph.node('D')

graph.edge('A', 'B', label='Edge from A to B')
graph.edge('B', 'C', label='Edge from B to C')
graph.edge('C', 'D', label='Edge from C to D')
graph.edge('D', 'A', label='Edge from D to A')

# Render the graph as a PDF file
graph.render('example-graph', view=True)