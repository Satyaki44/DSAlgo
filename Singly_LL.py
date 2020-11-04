
  
# Node class 
class Node(object): 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printlist(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
    
    #inserting nodes in the linked list-->
    #inserting node at first:
    def insertfirst(self,newdata):
        newnode=Node(newdata)
        if (llist.head==None):
            llist.head=newnode
        else:
            newnode.next=llist.head
            llist.head=newnode

    def insertlast(self,newdata):
        newnode=Node(newdata)
        if (llist.head==None):
            llist.head=newnode
        else:
            temp=self.head
            while temp.next!= None:
                temp=temp.next
            temp.next=newnode
    def deletefirst(self):
        if(llist.head==None):
            print("LL is empty")
        else:
            llist.head=llist.head.next
    def deletelast(self):
        if (llist.head==None):
            print("LL is empty")
        else:
            temp=self.head
            while temp.next!= None:
                temp=temp.next
            temp.next=None


  
  
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    llist.head.next = second; # Link first node with second 
    second.next = third; # Link second node with the third node 
  
    #traversing linked list
    llist.printlist() 
    
    #performing various functions
    llist.insertfirst(5)
    llist.insertfirst(6)
    llist.printlist()
    llist.insertlast(99)
    llist.printlist()
    llist.deletefirst()
    llist.printlist()
    llist.deletelast()
    llist.printlist() 
