## singly linked list & Doubly linked list (reverse conection)

class SinglyNode: # => defind your class 

  def __init__(self, val, next=None):
    self.val = val #=> the value of each node we gonna use
    self.next = next #= > next value (pointer point to a spicific value) for exemple 1 -> 2 -> 3 -> 4 the 1.next is 2..... also this attribue is an Optional[ListNode] Check the README if u don't understand

  def __str__(self):
     return str(self.val) # return str inside of obj
  


# After Creating the Class we gonna traverse that list by pointing a reference head (the strating) every Singly_linked_list or Doubly (type of linked list) should have  strating point u can name it whatever u want (head for exemple)

head = SinglyNode(1) # 1 
A = SinglyNode(2) # 2
B = SinglyNode(3) # 3
C = SinglyNode(4) # 4

head.next = A # 1 - > 2
A.next = B # 1 -> 2 -> 3 be shure bc we don't want to lose the connection btw the components (we gonna see how to fix that)
B.next = C # 1 -> 2 -> 3 -> 4

print(head.next) # 2 bc the value next to one is 2

## Traverse the list 1 -> 2 -> 3 -> 4

curr = head # we do that bc we don't want to lose our connection


while curr: # => Traversing 
  print(curr)
  curr = curr.next # Recursion but in another way

## The time complexity it's actualy O(k) k represent the elements in the list bc we iterate for each elements util the while loop stops: O(n)
## The space complexity is O(1) bc we don't use any extr spaces for now just traversing and pointing


## Traversing the linked list using while loop and recursion both are the same
def traverse_linked_list(head):
  curr = head

  while curr:
    print(curr.val, end="")
    if curr.next is not None:
      print(" -> ", end="")
    curr = curr.next
  print()


def traverse_by_recursion(head):
  if head is None:
    return
  print(head.val, end="")
  if head.next is not None:
    print(" -> ", end="")
  traverse_by_recursion(head.next)



## U can also do insertion in linked list at beginning or end or in a specefic pos

# 1. at The beginning
## U just have to point the new_node.next to the head 

def insertion(head, x):
  new_node = SinglyNode(x) # the new_node
  new_node.next = head # pointing the new_node.next to the head bc we want to insert at the beginning of the linked list.
  return new_node

head = insertion(head, 0)
traverse_by_recursion(head)


# 2. at the end
def ins_end(head, x):
  last_v = head
  while last_v.next:
    last_v = last_v.next # traversing util we het the curr is none
  last_v.next = SinglyNode(x) # the while loop stop so that mean that the curr.next (last_v.next) is None
  # So we point the curr.next to the next node

ins_end(head, 6)
traverse_by_recursion(head)


# 3. at a specifique position
def insert(head, pos, val):

    if pos < 1:
      return head # just one element that we have

    if pos == 1: # insert at beginning
      new_node = SinglyNode(val)
      new_node.next = head
      return new_node

    curr = head # we don't want to lose connection
    i = 1
    while i < pos - 1 and curr: # Traverse to the end 
      curr = curr.next
      i += 1

    if not curr:
      return head

    new_node = SinglyNode(val)
    new_node.next = curr.next # Updating the linkedlist
    curr.next = new_node # Updating the linkedlist

    return head

head = insert(head, 3, 2)
traverse_by_recursion(head)



## and now we gonna see how to delete a node from beginning or end or specific pos

# 1. at beginning (head)

def del_head(head):
  if not head:
    return None

  temp = head
  head = head.next # the head now is the take the value of here next element by assinement (deleted the head)

  temp = None

  return head # new head (head.next)

head = del_head(head)
traverse_by_recursion(head)

# 2. at the end

def del_end(head):
  if not head:
    return None

  if not head.next:
    head = None
    return head

  curr = head
  while curr.next.next: # we do that bc want to stop at the pneultimate element
    curr = curr.next

  curr.next = None
  return head

head = del_end(head)
traverse_by_recursion(head)

## Counting the num of node ecist in the linked list
def cout_node(head):
  count = 0
  curr = head
  while curr:
    count += 1
    curr = curr.next
  return count



