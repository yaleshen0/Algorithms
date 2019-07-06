class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = len(self.stack)

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        return(self.stack.append(x))

    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[:self.size-1]
        return(self.stack)

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[self.size -1]
        return top
        

    def getMin(self):
        """
        :rtype: int
        """
        minval = self.stack[0]
        for i in range(1,self.size):
            if self.stack[i] < minval:
                minval = self.stack[i]
        return(minval)


# Your MinStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.pop()
    print(obj.stack)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.getMin()
    print(param_4)