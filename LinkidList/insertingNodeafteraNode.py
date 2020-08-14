class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAfter(self, prev_nodeData, new_data): 
        temp=self.head
        while temp:
            if prev_nodeData == temp.data:
                break
            else:
                temp=temp.next
        newNode=Node(new_data)
        newNode.next=temp.next
        temp.next=newNode

        

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__ == "__main__":
    llist=LinkedList()
    llist.head=Node(1)#Created Node1 with head pointer
    second=Node(2) #Created 2nd node with with value 2
    third=Node(3) #Created 3rd node with with value 3
    llist.head.next=second #Linked first node next part to second node
    second.next=third  #Linked Second node next part to third node
    fourth=Node(4) #Created 4th node with with value 4
    third.next=fourth #Linked third node next part to 4th node
    llist.printList() #Print all elements of LinkidList
    print()
    llist.insertAfter(2,78)
    llist.printList() #Print all elements of LinkidList
