# este algoritmo lo que hace es medir la altura del arbol, calculando la distancia entre la raiz
# y las hojas y tomando el maximo.


class Node:
    def __init__(self, left, right, value) -> None:
        self.left = left
        self.right = right
        self.value = value


infinite = float("inf")

root = Node(
    Node(Node(None, Node(None, Node(None, None, 0), 55), 4), Node(None, None, 2), 11),
    Node(None, Node(None, None, 111), 4),
    3,
)


def depthfirst_recursive(root, h):
    if not root:
        return h - 1
    return max(
        [
            depthfirst_recursive(root.left, h + 1),
            depthfirst_recursive(root.right, h + 1),
        ]
    )


def depthfirst_iterative(root):
    stack = [(root, 0)]  # (node, height)
    max_h = 0

    while len(stack) > 0:
        (current, h) = stack.pop()
        if not current:
            continue

        max_h = max([max_h, h])

        stack.append((current.left, h + 1))
        stack.append((current.right, h + 1))
    return max_h


def breadthfirst(root):
    queue = [(root, 0)]  # (node, height)
    max_h = 0
    while len(queue) > 0:
        (current, h) = queue.pop(0)

        if not current:
            continue
        max_h = max([max_h, h])
        queue.append((current.left, h + 1))
        queue.append((current.right, h + 1))
    return max_h


def max_root_to_leaf_path(root):
    return breadthfirst(root)


print(breadthfirst(root))
print(depthfirst_iterative(root))
print(depthfirst_recursive(root, 0))
print(max_root_to_leaf_path(root))
