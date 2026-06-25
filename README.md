# Linked List:

linked list is a banch of connected components that are in a from of **Optional[ListNode]**
 => That indicate that a variable return value can either be a valid ListNode obj or None you may see it a lot in leetcode problems
.

### Older Version: ***Union[ListNode, None]***


## Node Class (that's the first that u should know)


```python
class SinglyNode:

  def __init__(self, val, next=None):
    self.val = val 
    self.next = next
```

SO THAT HOW TO CREATE A SIMPLE CLASS NODE IN PYTHON WHEN THE VAL REPRESENT THE ELEMNT ITSELF AND THE NEXT WE SET TO NONE BC WE DID NOT ANY CONNECTION FOR NOW WE GONNA SEE HOW WE CAN DO THAT

## Creating some connection(adding elements)


1.Adding some elements
```python
head = SinglyNode(1)  
A = SinglyNode(2) 
B = SinglyNode(3)
C = SinglyNode(4) 
```

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



# Do Insertion in linked List

## 1.At The Beginning

```python
def insertion(head, x):
  new_node = SinglyNode(x)
  new_node.next = head
  return new_node

head = insertion(head, 0)
traverse_by_recursion(head)
```

### So now u did an insertion at the beginning by pointing new head u should know that now u have a new head that is the new node so u should return it (see The code to undertand very well) bc it's nececiry if u want to traverse a linked list....



## 2. At The End

```python
def insertion_end(head, x):
  curr = head
  while curr.next:
    curr = curr.next
  curr.next = SinglyNode(x)

insertion_end(head, 5)
traverse_by_recursion(head)
```

### Now we did an insertion at the end of the linked list how actualy that work:
### we strat by traversing the linked list util we hit the curr is None we insert the new_node in that position (when the while loop fail) buy pointing the curr.next to the new_node



## 3. At A Specific Position

```python
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
```

## we traverse the list util we het the node that is before the place that we want to insert in it but before we just have to do some series of checks at the beginning bc that's necicery if for exmple the place that we want to insert in it is none we only have one element in the linked list or or or...... and then at the end we point the  **new_node.next  to the curr.next** and ** curr.next  to the new_node**


## also in the deletion we just have to assign the head to head.next and return haed (del at beginning ) or going to the pneultimate element and set the curr.next to None (del at the end) try to do it youself and then check the code


# 3. this his how to ount number of node in a linked list

```python
def cout_node(head):
  count = 0
  curr = head
  while curr:
    count += 1
    curr = curr.next
  return count
```


# 4 and this how to transform a linked list to array (you gonna nedd it a lot in the case if u want that)



```python
rgb(15, 89, 162) linked_list_to_array(head):
  #array = []
  #curr = head
  #while curr:
   # array.append(curr.val)
    #curr = curr.next
  #return array

def linked_list_array(head, arr, n):# n is the size
  curr = head
  for i in range(n):
      arr[i] = curr.val
      curr = curr.next
```

# 5 and this how to transform it back to linked_list

```python
def array_to_linked_list(arr, head, n):
  curr = head
  for i in range(n):
    curr.val = arr[i]
    curr = curr.next
```
