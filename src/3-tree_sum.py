class Node:
    def __init__(self, left, right, value) -> None:
        self.left = left
        self.right = right
        self.value = value


root = Node(
    Node(Node(None, None, 4), Node(None, None, 2), 11),
    Node(None, Node(None, None, 1), 4),
    3,
)


def depthfirst_recursive(root):
    if not root:
        return 0

    return (
        root.value + depthfirst_recursive(root.right) + depthfirst_recursive(root.left)
    )


def depthfirst_iterative(root):
    sum = 0
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if not current:
            continue
        sum += current.value

        stack.append(current.left)
        stack.append(current.right)
    return sum


def breadthfirst(root):
    sum = 0
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)

        if not current:
            continue

        sum += current.value

        queue.append(current.left)
        queue.append(current.right)
    return sum


def tree_sum(root):
    return depthfirst_recursive(root)


print(breadthfirst(root))
print(depthfirst_iterative(root))
print(depthfirst_recursive(root))
print(tree_sum(root))
