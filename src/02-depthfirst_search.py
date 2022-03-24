my_graph = {"a": ["b", "d"], "b": ["c"], "c": [], "d": ["b", "f"], "e": ["d"], "f": []}


def deepthfirst_search_recursive(graph, node):
    if node in graph.keys():
        print(node)
        for adj in graph[node]:
            deepthfirst_search_recursive(graph, adj)
            deepthfirst_search_recursive(graph, adj)
    return


def deepthfirst_search_iterative(graph, node):
    result = []
    stack = []

    stack.append(node)
    while node and len(stack) > 0:
        node = stack.pop()
        result.append(node)

        if node in graph.keys():
            for adj in graph[node]:
                stack.append(adj)

    return result


deepthfirst_search_recursive(my_graph, "a")
print(deepthfirst_search_iterative(my_graph, "a"))
