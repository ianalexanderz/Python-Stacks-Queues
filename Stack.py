class Stack:
    def __init__(self):
        self.stack = []
        

    def isEmpty(self):
        """Returns True if Stack is empty, False otherwise"""
        return self.stack == []

    def push(self, item):
        """Adds an item to the top of stack"""
        self.stack.append(item)
        print(self.stack)

    def pop(self):
        """Removes the item from the top of stack. Returns the removed item"""
        return self.stack.pop()

    def peek(self):
        """Returns the top item in the stack, but doesn't remove it"""
        return self.stack[len(self.stack) - 1]

    def size(self):
        """Returns the (int) size of the stack"""
        return len(self.stack)

    def __str__(self):
        """Returns a string representation of all items in stack"""
        new_string = ""
        for i in range(len(self.stack)):
            new_string += self.stack[i] + " "
        return new_string

### TEST SUITE ###
# Use the following code to help you implement the Stack
my_stack = Stack()

print('Is Stack empty? Should be True: \n', my_stack.isEmpty())

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
my_stack.push('D')




print('Popped item should be D: \n', my_stack.pop())
print('Top item should be C: \n', my_stack.peek())
print('Here are all the items in the stack - Should be A B C: \n', my_stack)
# print('The size of stack should be 3: \n', my_stack.size())

# Bonus Question - How would our Stack implementation change if we
# created it with a LinkedList instead of a List?
# What is a LinkedList?





# Driver program to test above functions   
# Driver code
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
 
# print "% d popped from stack" % (stack.pop())
# print "Top element is % d " % (stack.peek())