class Node:
    def __init__(self, left, right, value) -> None:
        self.left = left
        self.right = right
        self.value = value


infinite = float("inf")

root = Node(
    Node(Node(None, None, 4), Node(None, None, 2), 11),
    Node(None, Node(None, None, 111), 4),
    3,
)


def depthfirst_recursive(root):
    if not root:
        return infinite
    return min(
        [root.value, depthfirst_recursive(root.left), depthfirst_recursive(root.right)]
    )


def depthfirst_iterative(root):
    min = infinite
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if not current:
            continue

        if current.value < min:
            min = current.value

        stack.append(current.left)
        stack.append(current.right)
    return min


def breadthfirst(root):
    min = infinite
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)

        if not current:
            continue

        if current.value < min:
            min = current.value

        queue.append(current.left)
        queue.append(current.right)
    return min


def min_value(root):
    return breadthfirst(root)


print(breadthfirst(root))
print(depthfirst_iterative(root))
print(depthfirst_recursive(root))
print(min_value(root))
