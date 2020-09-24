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

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=="__main__":
    llist=LinkedList()
    llist.push(6)
    llist.push(99)
    llist.printList() #Print all elements of LinkidList

