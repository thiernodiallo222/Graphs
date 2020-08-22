# from util import Stack, Queue  # These may come in handy

def get_parents(vertex, graph):
    parents = []
    for vertex, children in graph.items():
        if vertex in children:
            parents.append(vertex)
    return parents

# myStack = Stack()

def earliest_ancestor(ancestors, starting_node):
    visited = set()  #create a set of visited vertices
    path = []  # this is where we store the paths
    path.append(starting_node)
    terminating_path=[]
    
    while len(path)> 0:
        current_path = path.pop()
        vertex = current_path[-1]
        if vertex not in visited:
            visited.add(vertex)
            parents = get_parents(vertex, graph)
            if not parents and len(current_path) > 1:
                terminating_paths.append(current_path)
            for item in parents:
                next_path = current_path.copy()
                next_path.append(item)
                path.append(next_path)
    if not terminating_paths:
        return - 1
     
    longest_path_len = max([len(item) for item in terminating_paths])

    earliest_ancestors = [item[-1] for element in terminating_paths if len(element) == longest_path_len]
    return min(earliest_ancestors)
        