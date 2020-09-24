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
    def remove(self,dataRemove):
        temp=self.head
        #If the element to br removed is the 1st element itself
        if temp.data==dataRemove:
            self.head=temp.next
        else:
            
            while temp:
                if temp.data==dataRemove:
                    break
                prev=temp
                temp=temp.next
            if temp==None:
                print("Element ro be removed is not found in Linked List")
                return
            #Unlinking the node to be removed from Linked List
            prev.next = temp.next
            temp = None


    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=="__main__":
    llist = LinkedList() 
    llist.push(7) 
    llist.push(1) 
    llist.push(3) 
    llist.push(2) 
    llist.push(8) 
    llist.printList()
    llist.remove(8)
    print()
    llist.printList()
