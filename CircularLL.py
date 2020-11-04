#creating the nodes

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

#creating circular class
class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.end = None

    #printing list
    def printlist(self):
        curr_node = self.head
        while curr_node.next :
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break

    #inserting at beg
    def insertbeg(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.end=newnode
            self.head.next=newnode
        else:
            self.end.next=newnode
            newnode.next=self.head
            self.head=newnode

    #inserting at end
    def insertend(self,data):
        newnode=Node(data)
        if self.head:
            self.end.next=newnode
            newnode.next=self.head
            self.end=newnode
        else:
            self.head=newnode
            self.end=newnode
            self.head.next=newnode

    #deleting at beg
    def deletebeg(self):
        if self.head==None:
            print("List is empty")
        else:
            self.head=self.head.next
            self.end.next=self.head

    #deleting at end
    def deleteend(self):    
        #Checks whether list is empty    
        if(self.head == None):    
            print("List is empty");    
        else:    
            #Checks whether contain only one element    
            if(self.head != self.end ):    
                temp = self.head;    
                #Loop will iterate till the second last element as current.next is pointing to tail    
                while(temp.next != self.end):    
                    temp = temp.next;    
                #Second last element will be new tail    
                self.end = temp;    
                #Tail will point to head as it is a circular linked list    
                self.end.next = self.head;    
            #If the list contains only one element     
            #Then it will remove it and both head and tail will point to null    
            else:    
                self.head = self.end = None;   
                







#code execution starts here
if __name__ == "__main__":
    
    cllist=CircularLinkedList()
    cllist.insertbeg(1)
    cllist.insertbeg(2)
    cllist.insertbeg(3)
    cllist.insertbeg(66)
    cllist.insertend(9)
    cllist.deletebeg()
    cllist.deleteend()
    cllist.printlist()