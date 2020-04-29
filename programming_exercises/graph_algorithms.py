def isBipartite(graph):
    """ Determine if a given graph is bipartite or not.

    Parameters
    ----------
    graph : List[List[int]]
            The graph to study.

    Returns
    -------
    bool
        Whether the graph is bipartite or not.
    """
    white_vertices = set()
    black_vertices = set()
    vertices = set(range(len(graph)))
    last_layer = [0]
    white_vertices.add(0)
    next_layer = list()
    is_white_iter = False
    last_step = False
    while not last_step:
        if len(white_vertices) + len(black_vertices) == len(graph):
            last_step = True
        elif len(last_layer) == 0:
            diff = vertices.difference(white_vertices.union(black_vertices))
            last_layer = [diff.pop()]
            white_vertices.add(last_layer[0])
            is_white_iter = False

        for i in last_layer:
            for j in graph[i]:
                if is_white_iter:
                    if j in black_vertices:
                        return False
                    if j not in white_vertices:
                        white_vertices.add(j)
                        next_layer.append(j)
                else:
                    if j in white_vertices:
                        return False
                    if j not in black_vertices:
                        black_vertices.add(j)
                        next_layer.append(j)

        last_layer = next_layer
        next_layer = []
        is_white_iter = not is_white_iter
    return True
