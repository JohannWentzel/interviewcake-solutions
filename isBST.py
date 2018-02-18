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

    def isBST_iterative(self):
        if self.left == None and self.right == None:
            return True

        stack = []

        #tuple layout: (node, min, max)

        stack.append((self, float('-inf'), float('inf')))

        while len(stack) > 0:
            current, minConstraint, maxConstraint = stack.pop()

            if current.value > maxConstraint or current.value < minConstraint:
                print(current.value, "invalid for min:",minConstraint, ", max:", maxConstraint)
                return False

            if current.left != None:
                stack.append((current.left, minConstraint, min(maxConstraint, current.value)))

            if current.right != None:
                stack.append((current.right, max(minConstraint,current.value), maxConstraint))

        return True

    def isBST_recursive(self, node, minConstraint, maxConstraint):
        if node is None:
            # print("Reached end, returning true")
            return True

        leftValid = node.isBST_recursive(node.left, minConstraint, min(maxConstraint, node.value))

        rightValid = node.isBST_recursive(node.right, max(minConstraint, node.value), maxConstraint)

        if leftValid and rightValid and node.value > minConstraint and node.value < maxConstraint:
            # print("valid for", node.value, minConstraint, maxConstraint)
            return True
        else:
            print("invalid for", node.value, minConstraint, maxConstraint)
            return False

    def isBST_inorder(self):
        traversalList = []
        stack = []

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

        print("Traversal: ", traversalList)
        return traversalList == sorted(traversalList)

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

    print(root.isBST_iterative())
    print(root.isBST_recursive(root, float("-inf"), float("inf")))
    print(root.isBST_inorder())