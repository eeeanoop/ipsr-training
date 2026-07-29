
'''
Given linkelist 
Remove nth node and return head
6

'''

from typing import Optional

class LinkedListNode:
  def __init__(self, val: int = 0, next: Optional['LinkedListNode'] = None):
    self.val = val
    self.next = next

def populate_linked_list(input_values: list[int]) -> LinkedListNode:

  dummy =  LinkedListNode(0, None)
  current_node = dummy 
  
  for i in input_values:
    current_node.next = LinkedListNode(i, None)
    current_node = current_node.next
  return dummy.next


def print_linked_list(head: LinkedListNode):

  current = head

  while current != None:
    print (current.val)
    current = current.next
  
def remove_nth_node_from_end(head: LinkedListNode, n: int):
  dummy = LinkedListNode(0,head)
  current = dummy
  fast_pointer = dummy

  for _ in range(n):
    fast_pointer = fast_pointer.next

  while fast_pointer.next is not None:
    current = current.next
    fast_pointer = fast_pointer.next

  current.next = current.next.next     

  # print(current.val)
  return dummy.next
    
  

  
  
  




#  None # 0XAA
# is not => memory comparison
# != value comparison

class CustomObject:
  def __eq__(self, other):
    return True

def test_method():
  obj = CustomObject()
  if obj is not None:
    print('Not None 1')

  if obj != None:
     print('Not None 2')
  
  
# test_method()
    
print_linked_list(populate_linked_list([9,8,7,6,5,4,3,2,1,0]))
print()
print_linked_list(remove_nth_node_from_end(populate_linked_list([9,8,7,6,5,4,3,2,1,0]), n=1))


