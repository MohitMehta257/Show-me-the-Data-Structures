class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    l1=[]
    l2=[]
    uni=[]
    node=llist_1.head
    
    while node:
        l1.append(node.value)
        node=node.next
        
    node2=llist_2.head
    
    while node2:
        l1.append(node2.value)
        node2=node2.next
    
    for each in l1:
        if (uni.count(each)==0):
            uni.append(each)
    return sorted(uni)


def intersection(llist_1, llist_2):
    # Your Solution Here
    
    l1=[]
    l2=[]
    node=llist_1.head
    
    while node:
        l1.append(node.value)
        node=node.next
    node2=llist_2.head
    
    while node2:
        l2.append(node2.value)
        node2=node2.next
        
    intersect=[]
        
    for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i]==l2[j]):
                intersect.append(l1[i])
    intersectfinal=[]
    for each in intersect:
        if intersectfinal.count(each)==0:
            intersectfinal.append(each)
    return sorted(intersectfinal)

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]   
element_2 = [6,32,4,9,6,1,11,21,1]     

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))            #returns [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]
print (intersection(linked_list_1,linked_list_2))     #returns [4, 6, 21]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))            #returns [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]
print (intersection(linked_list_3,linked_list_4))     #returns empty list
