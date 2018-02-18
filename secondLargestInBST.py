class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def secondLargest_recursive(self):

        current = self

        if (current.right == None and current.left == None) or current == None: 
            raise ValueError("Needs at least two nodes!")

        if current.right == None and current.left != None:
            return current.value

        while current.right != None:
            parent = current
            current = current.right

        return parent.value

    def secondLargest_inOrder(self):
        stack = []
        traversalList = []
        done = False
        current = self

        while not done:
            if current != None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    traversalList.append(current.value)
                    current = current.right
                else:
                    done = True

        print(traversalList)

        return traversalList[-2]



if __name__ == '__main__':
    root = BinaryTreeNode(50)
    thirty = root.insert_left(30)
    eighty = root.insert_right(80)
    twenty = thirty.insert_left(20)
    ten = twenty.insert_left(10)
    forty = thirty.insert_right(40)
    seventy = eighty.insert_left(70)
    sixty = seventy.insert_left(60)
    ninety = eighty.insert_right(90)
    eightyfive = ninety.insert_left(85)
    hundred = ninety.insert_right(100)

    print(root.secondLargest_recursive())
    print(root.secondLargest_inOrder())

