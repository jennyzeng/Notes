"""
Some basic linkedList practices
"""
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def __str__(self):
		myString = ""
		temp = self
		while temp != None:
			myString += str(temp.data) + "-->"
			temp = temp.next
		myString += "None"
		return myString

"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list

# Sample Input

NULL , data = 1
1 --> NULL , data = 2

# Sample Output

1 --> NULL
1 --> 2 --> NULL

"""


def InsertTail(head, data):
    if head == None:
        return Node(data)
    else:
        temp = head
        while (temp.next!= None):
            temp = temp.next
        temp.next = Node(data)
    return head

#
# head = InsertTail(None, 1)
# head = InsertTail(head, 2)

"""
 InsertTail Node at the begining of a linked list
 head input could be None as well for empty list

# Sample Input

NULL , data = 1
1 --> NULL , data = 2

# Sample Output

1 --> NULL
2 --> 1 --> NULL
"""

def InsertHead(head, data):
	if head == None:
		return Node(data)
	else:
		head = Node(data, head)
		return head


"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list

# Sample Input

NULL, data = 3, position = 0
3 --> NULL, data = 4, position = 0

# Sample Output

3 --> NULL
4 --> 3 --> NULL
"""


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position=0):
	if head == None:
		return Node(data, head)
	elif position == 0:
		head = Node(data, head)
		return head
	elif position == 1:
		head.next = Node(data, head.next)
		return head
	else:
		head.next = InsertNth(head.next, data, position - 1)
		return head

head = InsertNth(None, 3, 0)
head = InsertNth(head, 5, 1)
head = InsertNth(head, 4, 2)
head = InsertNth(head, 2, 3)
head = InsertNth(head, 10, 1)
print(head)

"""
 Delete Node at a given position in a linked list

#Sample Input

1 --> 2 --> 3 --> NULL, position = 0
1 --> NULL , position = 0

#Sample Output

2 --> 3 --> NULL
NULL

"""


def Delete(head, position):
	if head == None:
		return None
	elif position == 0:
		head = head.next
	else:
		head.next = Delete(head.next, position-1)
	return head

head = InsertHead(None,3)
head = InsertHead(head, 2)
head = InsertHead(head, 1)
head = Delete(head, 0)

"""
 Print elements of a linked list in reverse order as standard output
Sample Input

1 --> 2 --> NULL
2 --> 1 --> 4 --> 5 --> NULL

Sample Output

2
1
5
4
1
2

"""
def ReversePrint(head):
	if head == None:
		return
	elif head.next == None:
		print(head.data)
		return
	else:
		ReversePrint(head.next)
		print(head.data)


"""
 Reverse a linked list
 head could be None as well for empty list

 return back the head of the linked list in the below method.

Sample Input

NULL
2 --> 3 --> NULL

Sample Output

NULL
3 --> 2 --> NULL
"""


def Reverse(head):
	result = Node(head.data)
	temp = head.next
	while temp != None:
		result = Node(temp.data, result)
		temp = temp.next
	return result


"""
 Merge two linked list
 head could be None as well for empty list

Sample Input

NULL, 1 --> NULL
1 --> 2 --> NULL, 1 --> 2 --> NULL

Sample Output

0
1
"""


def CompareLists(headA, headB):
	if headA == None and headB == None:
		return 1
	elif headA.next == None and headB.next == None:
		return int(headA.data == headB.data)
	elif headA.next == None or headB.next == None:
		return 0
	else:
		return int(headA.data == headB.data and CompareLists(headA.next, headB.next))
