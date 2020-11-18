
def earliest_ancestor(ancestors, starting_node):
    stack = []
    dict = {}
    for parent, child in ancestors:
        if child is not None:
            dict.setdefault(child, list([parent]))
        else:
            dict[child].append(parent)
    stack.append(starting_node)
    generations = []
    while stack:
        child = stack.pop()
        parents = []
        if child in dict:
            for parent in dict[child]:
                if parent in dict:
                    stack.append(parent)
                if len(parents) < 2:
                    parents.append(parent)
            generations.append(parents)
            print(f"Parents: {generations}")
        else: 
            generations.append(parents)
            break
    earliest_gen = generations[-1]
    print(f"Earliest gen: {earliest_gen}")
    earliest_ancestor = None
    if len(earliest_gen) is 0:
        return -1
    else:
        for parent in earliest_gen:
            if earliest_ancestor is None:
                earliest_ancestor = parent
            if parent < earliest_ancestor:
                earliest_ancestor = parent
    print(f"Earliest Ancestor: {earliest_ancestor}")
    return earliest_ancestor