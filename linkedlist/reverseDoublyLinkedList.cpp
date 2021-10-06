20. Reverse a Doubly Linked list.
Here is a simple method for reversing a Doubly Linked List. 
All we need to do is swap prev and next pointers for all nodes, change prev of the head (or start) and change the head pointer in the end.
* Function to reverse a Doubly Linked List */ 
 void reverse(Node **head_ref) 
{ Node *temp = NULL; Node *current = *head_ref; 
 /* swap next and prev for all nodes of doubly linked list */ 
 while (current != NULL) { temp = current->prev; current->prev = current->next; current->next = temp; current = current->prev; }
 /* Before changing the head, check for the cases like empty list and list with only one node */ 
 if(temp != NULL ) *head_ref = temp->prev; }

Time Complexity: O(N), where N denotes the number of nodes in the doubly linked list. 
Auxiliary Space: O(1) 
    We can also swap data instead of pointers to reverse the Doubly Linked List. 
    Method used for reversing array can be used to swap data. Swapping data can be costly compared to pointers if the size of the data item(s) is more. Method 2: The same question can also be done by using Stacks. Steps:
1. Keep pushing the node’s data in the stack. -> O(n) 
2. The keep popping the elements out and updating the Doubly Linked List *Function to reverse a Doubly Linked List using Stacks * Function to reverse a Doubly Linked List using Stacks */ 
  void reverse() { stack<int> st; Node* temp = head; while (temp != NULL) { st.push(temp->data); temp = temp->next; }
                  // added all the elements sequemce wise in the // st temp = head; while (temp != NULL) 
                  { temp->data = st.top(); st.pop(); temp = temp->next; }
                  // popped all the elements and the added in the // linked list, // which are in the reversed order-> } 
                  Time Complexity: O(N) 
                  Auxiliary Space: O(N)
 In this method, we traverse the linked list once and add elements to the stack, and again traverse the whole for updating all the elements. The whole takes 2n time, which is the time complexity of O(n)
