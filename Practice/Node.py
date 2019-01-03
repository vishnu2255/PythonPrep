class Node:
    def __init__(self, initial=None):
        self.value = initial
        self.next = None

    def isEmpty(self):
        return (self.value == None)

    def append(self,v):

        if self.isEmpty():
            self.value = v
            return

        temp = self
        while temp.next != None:
            temp = temp.next

        newnode = Node(v)
        temp.next = newnode

        return








