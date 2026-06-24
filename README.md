# Linked List:

linked list is a banch of connected components that are in a from of **Optional[ListNode]**
 => That indicate that a variable return value can either be a valid ListNode obj or None you may see it a lot in leetcode problems
.

### Older Version: ***Union[ListNode, None]***


## Node Class (that's the first that u should know)


'''python
class SinglyNode:

  def __init__(self, val, next=None):
    self.val = val 
    self.next = next
'''

SO THAT HOW TO CREATE A SIMPLE CLASS NODE IN PYTHON WHEN THE VAL REPRESENT THE ELEMNT ITSELF AND THE NEXT WE SET TO NONE BC WE DID NOT ANY CONNECTION FOR NOW WE GONNA SEE HOW WE CAN DO THAT

## Creating some connection(adding elements)


1.Adding some elements
'''python
head = SinglyNode(1)  
A = SinglyNode(2) 
B = SinglyNode(3)
C = SinglyNode(4) 
'''

2.Create connection

```python
head.next = A
A.next = B
B.next = C
```

WE CAN ALSO TRAVERSE THE LIST (SEE  ALL THE ELEMENTS) WE CAN DO THAT BY POINTING AT THE FIRST CURR TO HEAD SO WE DON'T WANT TO LOSE OUR CONNECTION AND THENA WHILE LOOP  EACH TIME WE UPDATE THE CURR TO THE CURR.NEXT U CAN ALSO USE RECURSION IT IS THE SAME

```python
curr = head

while curr:
  print(curr)
  curr = curr.next
```


## display the linked list also time complexity of O(n)

```python
def display(head):
  display = [] # Store the elements here
  curr = head
  while curr:
    display.append(str(curr.val))
    curr = curr.next
  print(' -> '.join(display)) # for a nice representation 

display(Head)
```

OUTPUT IS:  1 -> 2 -> 3 -> 4
            ^
            |
           head 

AND BY RECURSION:

```python
def traverse_by_recursion(head):
  if head is None:
    return
  print(head.val, end="")
  if head.next is not None:
    print(" -> ", end="")
  traverse_by_recursion(head.next)
```

***IT IS THE SAME AS ABOVE***

## we can also reduce the space complexity in the first display there is another way to do that

```python
def traverse_linked_list(head):
  curr = head

  while curr:
    print(curr.val, end="")
    if curr.next is not None:
      print(" -> ", end="")
    curr = curr.next
  print()
```



