
null = None
class Node:
    def __init__(self, x):
        self.data = x
        self.height = 1
        self.left = null
        self.right = null

def make_null():
    global null
    if null is None:
        null = Node(None)
        null.height = 0
        null.left = null
        null.right = null
    return null

def rotate_right(node):
    lnode = node.left
    node.left = lnode.right
    lnode.right = node
    return lnode

def rotate_left(node):
    rnode = node.right
    node.right = rnode.left
    rnode.left = node
    return rnode

def skew(node):
    if node.left.height == node.height:
        node = rotate_right(node)
    return node

def split(node):
    if node.height == node.right.right.height:
        node = rotate_left(node)
        node.height += 1
    return node

def insert(node, x):
    if node is null: return Node(x)
    elif x == node.data: return node
    elif x < node.data:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return split(skew(node))

def search_min(node):
    while node.left is not null: node = node.left
    return node.data

def delete(node, x):
    if node is not null:
        if x == node.data:
            if node.left is null: return node.right
            elif node.right is null: return node.left
            else:
                node.data = search_min(node.right)
                node.right = delete(node.right, node.data)
        elif x < node.data:
            node.left = delete(node.left, x)
        else:
            node.right = delete(node.right, x)
        if node.left.height < node.height - 1 or node.right.height < node.height - 1:
            node.height -= 1
            if node.right.height > node.height:
                node.right.height = node.height
            node = skew(node)
            node.right = skew(node.right)
            node.right.right = skew(node.right.right)
            node = split(node)
            node.right = split(node.right)
    return node