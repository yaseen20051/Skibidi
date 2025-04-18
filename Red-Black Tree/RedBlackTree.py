from collections import deque

class RBNode:
    def __init__(self,value = None,color = 'R'):
        self.value = value
        self.right = None
        self.left = None
        self.parent  = None
        self.color = color

    def grandParent(self):
        if not self.parent :
            return None
        return self.parent.parent

    def uncle(self):
        if not self.parent:
            return None
        if self.parent.parent.right == self.parent:
            return self.parent.parent.left
        else: return self.parent.parent.right

    def sibling(self):
        if not self.parent:
            return None
        if self.parent.right == self:
            return self.parent.left
        else: return self.parent.right

    def changeColor(self):
        if self.color == 'R':
            self.color = 'B'
        else:
            self.color = 'R'
class RBT:
    def __init__(self,sourceFile):
        self.root = None
        self.sourceFile = sourceFile
        self.dataBaseLoaded = False
        self.load()


    def load(self):
        my_file = open(self.sourceFile, "r")

        # reading the file
        data = my_file.read()

        # replacing end splitting the text
        # when newline ('\n') is seen.
        data_into_list = data.split("\n")
        # print(data_into_list)
        my_file.close()

        for word in data_into_list:
            self.insert(word)
        self.dataBaseLoaded = True
    def save(self,word):
        file1 = open(self.sourceFile, "a")  # append mode
        file1.write("\n"+word)
        file1.close()
    def insert(self,value):
        new_node = RBNode(value)
        if self.root == None:
            self.root = new_node
        else:
            if(self.search(value)):
                return False
            currentNode = self.root
            parent = None
            while currentNode != None:
                if new_node.value>currentNode.value:
                    parent = currentNode
                    currentNode = currentNode.right
                else:
                    parent = currentNode
                    currentNode = currentNode.left


            if new_node.value>parent.value:
                parent.right = new_node
            else: parent.left = new_node
            new_node.parent = parent
        self.fix_tree(new_node)
        if(self.dataBaseLoaded):
          self.save(new_node.value)
        return True
    def inOrderTraverse(self,node):  ## print elements from min ---> mac
        if node:
            if node.left != None :
                self.inOrderTraverse(node.left)
            print(node.value)
            if node.right != None:
                self.inOrderTraverse(node.right)

    def fix_tree(self,node):
        # -----------------------   CASE 1 ----------------------------------- #

        if node.parent == None:

            self.root.color = 'B'
        else:
            if node.parent.color == 'R':

                if (node.uncle() == None or node.uncle().color == 'B'):
               ## if   node.uncle().color == 'B':
                    grandparent = node.grandParent()
               # -----------------------   CASE 3 ----------------------------------- #
                    if (grandparent.right == node.parent and node == node.parent.left) :
                        ## rotate right (parent)
                        self.rotateRight(node.parent)
                        ## change color grandparent
                        node.right.parent.changeColor()
                        node.right.grandParent().changeColor()
                        self.rotateLeft(node.right.grandParent())
                    elif(grandparent.left == node.parent and node == node.parent.right):
                        self.rotateLeft(node.parent)
                        ## change color grandparent

                        node.left.parent.changeColor()
                        node.left.grandParent().changeColor()
                        self.rotateRight(node.left.grandParent())
                        # -----------------------   CASE 4 ----------------------------------- #

                    elif(grandparent.right == node.parent and node == node.parent.right):
                        node.parent.changeColor()
                        node.grandParent().changeColor()
                        self.rotateLeft(node.grandParent())
                    elif(grandparent.left == node.parent and node == node.parent.left):
                        node.parent.changeColor()
                        node.grandParent().changeColor()
                        self.rotateRight(node.grandParent())


                # -----------------------   CASE 2 ----------------------------------- #

                elif node.uncle().color == 'R':

                    node.parent.changeColor()
                    node.uncle().changeColor()
                    if node.grandParent() == self.root or node.grandParent().color == 'R':
                        node.grandParent().color = 'B'
                    else: node.grandParent().changeColor()



    def rotateLeft(self,node):
        y = node.right
        node.right = y.left
        if (y.left != None):
            y.left.parent = node
        y.parent = node.parent
        # -----------------------   THE NODE IS THE ROOT  ----------------------------------- #

        if (node.parent == None):
            self.root = y
        elif(node == node.parent.left):
            node.parent.left = y
        elif(node == node.parent.right):
            node.parent.right = y
        y.left = node
        node.parent = y

    def search(self,value):


        pivot = self.root
        while(pivot != None):
            if(pivot.value == value): return True
            elif(value>pivot.value): pivot = pivot.right
            else: pivot = pivot.left
        return False


    def rotateRight(self,node):
        y = node.left
        node.left = y.right
        if(y.right != None):
            y.right.parent = node
        y.parent = node.parent
        if(node.parent == None):
            self.root = y
        elif(node.parent.right == node):
            node.parent.right = y
        elif(node.parent.left == node):
            node.parent.left = y
        y.right = node
        node.parent = y

    def height(self,node):
        if (node == None): return 0
        else:
            rightHeight = self.height(node.right)+1
            leftHeight = self.height(node.left)+1
            if(rightHeight>leftHeight) : return rightHeight
            else: return leftHeight

    def blackNodes(self,node):
        if (node == None):
            return 1
        else:
            leftBlackNodes = self.blackNodes(node.left)
            rightBlackNodes = self.blackNodes(node.right)
            if(leftBlackNodes != rightBlackNodes):
               return "Fix the error"
            if(node.color == 'B') : leftBlackNodes =+1
            return leftBlackNodes
    def numberOfNodes(self,node):
        if(node == None): return 0
        else:
            if(node!=None): return  self.numberOfNodes(node.left)+self.numberOfNodes(node.right)+1

    def printTreeDetails(self):
        print("Height of the Tree = "+str(self.height(self.root)))
        print("Black Height of the Root = "+str(self.blackNodes(self.root)))
        print("Number of words = "+str(self.numberOfNodes(self.root)))
    def displayTree(self):
            if not self.root:
                print("Tree is empty.")
                return

            q = deque()
            q.append((self.root, 0))
            current_level = 0
            output = ""

            while q:
                node, level = q.popleft()
                if level != current_level:
                    print(output)
                    output = ""
                    current_level = level

                output += str(node.value) +'('+ node.color +')'+"    "

                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

            if output:
                print(output)
