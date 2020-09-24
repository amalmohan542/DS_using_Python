class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
    def ListLength(self):
        temp=self.head
        c=0
        while temp:
            c+=1
            temp=temp.next
        print(str(c))

    def printList(self):
        temp=self.head
        while temp:
            print(str(temp.data)+"-->",end =" ")
            temp=temp.next

if __name__=="__main__":
    llist = LinkedList() 
    llist.push(7) 
    llist.push(1) 
    llist.push(3) 
    llist.push(2) 
    llist.push(8) 
    llist.printList()
    print()
    llist.ListLength()