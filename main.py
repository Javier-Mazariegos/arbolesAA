import arbol
def print_node(node, x):
    if node is not arbol.null:
        print_node(node.left, x)
        print ("    " * (x - node.height), node.data)
        print_node(node.right, x)

root = arbol.make_null()

for x in range(8):
    root = arbol.insert(root, x)
print_node(root, root.height)
print ('-----')
for x in range(8):
    root = arbol.delete(root, x)
    print_node(root, root.height)
    print ('-----')


