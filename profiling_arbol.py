import cProfile
import arbol

root = arbol.make_null()
cProfile.run("arbol.make_null()")
cProfile.run("arbol.insert(root, 1)")
cProfile.run("arbol.insert(root, 2)")
cProfile.run("arbol.insert(root, 3)")
cProfile.run("arbol.delete(root, 1)")