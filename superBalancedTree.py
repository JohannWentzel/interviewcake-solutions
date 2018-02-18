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

    def isSuperBalanced(self):

        maxDepth = float('-inf')
        minDepth = float('inf')
        currentDepth = 0

        stack = []

        if self.left == None and self.right == None:
            return True

        stack.append((node,0))

        while len(stack) > 0:
            current, currentDepth = stack.pop()
            if current.left == None and current.right == None:
                maxDepth = max(maxDepth,currentDepth)
                minDepth = min(minDepth, currentDepth)

            else: 
                if current.left != None:
                    stack.append((current.left,currentDepth + 1))
                if current.right != None:
                    stack.append((current.right, currentDepth + 1))



        return abs(maxDepth - minDepth) <= 1



if __name__ == '__main__':
    node = BinaryTreeNode(1)
    node.insert_right(2)
    node.insert_left(5)
    node.right.insert_right(3)
    node.right.right.insert_left(4)


    print(node.isSuperBalanced())
    
    


