class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def push(self,newData):
        if self.head==None:
            newNode=Node(newData)
            self.head=newNode
        else:
            newNode=Node(newData)
            newNode.next=self.head
            self.head=newNode

    def deleteIndexNode(self,index):
        temp=self.head
        if temp==None:
            print("Linked List is empty")
            return
        if index==0:
            self.head=temp.next
            return
        for i in range(0,index-1):
            temp=temp.next
            if temp==None:
                break
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next=temp.next.next
        # Unlink the node from linked list 
        temp.next = next 
        temp=None


    def printList(self):
        temp=self.head
        while temp:
            print(str(temp.data)+"-->",end =" ")
            temp=temp.next
if __name__ == "__main__":
    # Driver program to test above function 
    llist = LinkedList() 
    llist.push(7) 
    llist.push(1) 
    llist.push(3) 
    llist.push(2) 
    llist.push(8) 
    llist.printList()
    llist.deleteIndexNode(2)
    print()
    llist.printList()

        