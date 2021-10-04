## Linked List

### Information

A linked list is a data structure where each element is called a node and where each node holds two types of information:
1) a field that could contain some data related to the node
2) a pointer or reference to the next element in the list

### Can we reverse a linked list in less than O(n) ?

It is not possible to revert a linked list in less than O(n) as the complexity grows linearly with the number of nodes in the linked list.
One needs to pass through each node to update the reference. Do note that this could be done in one forward pass.

Double linked list can be reversed with a time complexity of O(1) as only the head and the tail of the linked list require an inversion.
