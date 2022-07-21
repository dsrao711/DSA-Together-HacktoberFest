# Binary Tree

- At most there can be 2 nodes in a Binary tree

- Binary search tree is a special case of Binary tree where order of nodes is very important 
  If the node is lesser than the parent , then it is stored in the left , else on the right

- Binary trees are used for set implementation 

- Search operations:

Each element has to be searched one by one in Linear data strcuture 
But for hierarchal ds like Tree , searching is better 
For searching an element out of n = 8

Linear  : 8 iterations
Tree    : 3 iterations -> (log8 to the base 2 =  3)

- Search complexity : O(logn)
- Insert complexity : O(logn)

## Complete Binary Tree

[![comp.png](https://i.postimg.cc/tghf6VHB/comp.png)](https://postimg.cc/d7V4P33C)

## Perfect Binary Tree

[![perfect.png](https://i.postimg.cc/QttfmjYT/perfect.png)](https://postimg.cc/B8r5Qf0S)

## Best and worst case 

[![Screenshot-2021-05-26-211811.png](https://i.postimg.cc/T25zvcQW/Screenshot-2021-05-26-211811.png)](https://postimg.cc/G9r7kGWc)

## Balanced Binary Tree 

[![121.png](https://i.postimg.cc/13WJgy1Z/121.png)](https://postimg.cc/k2bxz35j)

Diff = |height of left subtree - height of right subtree|