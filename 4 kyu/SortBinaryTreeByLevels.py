def tree_by_levels(node):
    values = []
    nodes = [node]

    while nodes:
        val = nodes.pop(0)

        if val is not None:
            values.append(val.value)
            nodes += [val.left, val.right]

    return [] if node is None else values
