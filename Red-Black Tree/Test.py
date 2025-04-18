import RedBlackTree


# opening the file in read mode
my_file = open("Dictionary.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
my_file.close()

rbt = RedBlackTree.RBT()
for i in data_into_list:
    rbt.insert(i)
rbt.displayTree()
print(rbt.search("treat"))
print(rbt.height(rbt.root))
print(rbt.blackNodes(rbt.root))
print(rbt.numberOfNodes(rbt.root))
rbt.insert("Yaseen")
print(rbt.search("Yaseen"))
print(rbt.height(rbt.root))
print(rbt.blackNodes(rbt.root))
print(rbt.numberOfNodes(rbt.root))

