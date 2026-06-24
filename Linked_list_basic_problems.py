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



