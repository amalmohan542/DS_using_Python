class Node:         #Class for each single node to be created
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkidList:   #Class for LinkedLIst to br created to hold the entore set of nodes
    def __init__(self):
        self.head=None #Initially when a LinkidList object is created we set its Head as None During creation
    def printList(self):
        temp=self.head #Recive the Head of Linkid list and assign to temp for traversal
        while(temp):#Loop execute until when temp points to None (ie,Last node is reached)
            print(temp.data)
            temp=temp.next

if __name__ == "__main__":
    llist=LinkidList();
    llist.head=Node(1)#Created Node1 with head pointer
    second=Node(2) #Created 2nd node with with value 2
    third=Node(3) #Created 3rd node with with value 3
    llist.head.next=second #Linked first node next part to second node
    second.next=third  #Linked Second node next part to third node
    fourth=Node(4) #Created 4th node with with value 4
    third.next=fourth #Linked third node next part to 4th node
    llist.printList() #Print all elements of LinkidList
