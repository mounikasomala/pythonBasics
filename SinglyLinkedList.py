class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
     newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head

def insertNodeAtHeadOfLinkedList(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
 
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head
 
  
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele)
    head = insertNodeAtHeadOfLinkedList(head, ele)
 
printLinkedList(head)
 head = insertAtSpecificPosition(head, 1, 1009)
printLinkedList(head)






# DELETION IN SINGLY LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def printlist(head):
    curr=head
 
    while curr!=None:
         print(curr.data,end=" ")
        curr=curr.next
    print()
 
 
def deleteHeadNodeInLinkedList(head):
    if head == None:
        return None 
 
    secondNode = head.next 
    head.next = None 
    return secondNode     
 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInLinkedList(head)
    curr = head 
    index = 1 
    while index != position - 1:
        curr = curr.next 
        index += 1 
    mainNode = curr.next 
    nextNode = mainNode.next 
    mainNode.next = None 
    curr.next = None 
    curr.next = nextNode 
    return head
 
 
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)
head = deleteHeadNodeInLinkedList(head)
printlist(head)
 
head = deleteHeadNodeInLinkedList(head)
printlist(head)


