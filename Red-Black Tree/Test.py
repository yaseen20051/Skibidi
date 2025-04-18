import RedBlackTree



rbt = RedBlackTree.RBT("Dictionary.txt")
rbt.load()
print(rbt.numberOfNodes(rbt.root))
rbt.insert("Yaseen")
print(rbt.numberOfNodes(rbt.root))
