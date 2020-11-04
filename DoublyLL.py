#creation of node
class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

#creation of class doubly linked list
class DoublyLL(object):
    def __init__(self):
        self.head=None
        self.tail=None
    
    #traverse the list
    def printlist(self):
        curr_node = self.head
        while curr_node != None :
            print(curr_node.data)
            curr_node = curr_node.next
            
    
    #insert node at beg
    def insertbeg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        newnode.prev=None
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode

    #insert node at end
    def insertend(self,data):
        newnode=Node(data)
        newnode.next=None
        if self.head == None:
            newnode.prev=None
            self.head=newnode
        else:
            first_node=self.head
            while first_node.next:
                first_node=first_node.next
            first_node.next=newnode
            newnode.prev=first_node

    #delete node at beg
    def deletebeg(self):
        if self.head == None:
            print("Nothing to delete")
        elif self.head.next is None:
            self.head = None
        else:
            self.head=self.head.next
            self.head.prev=None
    #delete node at end
    def deleteend(self):
        if self.head==None:
            print("Nothing to delete")
        elif self.head.next==None:
            self.head=None
        else:
            curr_node=self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.prev.next = None



#execution of code
if __name__ == "__main__":
    dll=DoublyLL()
    dll.insertbeg(1)
    dll.insertbeg(2)
    dll.insertbeg(9)
    dll.insertbeg(4)
    dll.insertend(87)
    dll.deleteend()
    dll.deleteend()
    dll.deletebeg()
    dll.printlist()