PROBLEM : Given a stream of characters, find the first non-repeating character from stream. You need to tell the first non-repeating character in O(1) time at any moment. 
  The idea is to use a DLL (Doubly Linked List) to efficiently get the first non-repeating character from a stream. 
  The DLL contains all non-repeating characters in order, i.eThe head of the DLL contains the first non-repeating character, the second node contains the second non-repeating and so on. 
  We also maintain two arrays: one array is to maintain characters that are already visited two or more times, we call it repeated[], 
The other array is an array of pointers to linked list nodes, we call it inDLL[]. 
The size of both arrays is equal to alphabet size which is typically
  1. Create an empty DLL. Also create two arrays inDLL[] and repeated[] of size 
  inDLL is an array of pointers to DLL nodes. repeated[] is a boolean array, repeated[x] is true if x is repeated two or more times, otherwise false. 
  inDLL[x] contains a pointer to a DLL node if character x is present in DLL, otherwise NULL. 
  2. Initialize all entries of inDLL[] as NULL and repeated[] as false. 
  3. To get the first non-repeating character, return character at head of DLL. 
  4. Following are steps to process a new character ‘x’ in a stream. ○ If repeated[x] is true, ignore this character (x is already repeated two or more times in the stream) ○ If repeated[x] is false and inDLL[x] is NULL (x is seen for the first time). 
  Append x to DLL and store address of new DLL node in inDLL[x]. ○ If repeated[x] is false and inDLL[x] is not NULL (x is seen a second time). 
  Get the DLL node of x using inDLL[x] and remove the node. Also, mark inDLL[x] as NULL and repeated[x] as true. 
  Note that appending a new node to DLL is O(1) operation if we maintain tail pointer. Removing a node from DLL is also O(1). 
  So both operations, addition of new character and finding first non-repeating character take O(1) time.

MAX_CHAR = 256
 
def findFirstNonRepeating():
 
    # inDLL[x] contains pointer to a DLL node if x is present
    # in DLL. If x is not present, then inDLL[x] is NULL
    inDLL = [] * MAX_CHAR
 
    # repeated[x] is true if x is repeated two or more times.
    # If x is not seen so far or x is seen only once. then
    # repeated[x] is false
    repeated = [False] * MAX_CHAR
 
    # Let us consider following stream and see the process
    stream = "geekforgeekandgeeksandquizfor"
    for i in range(len(stream)):
        x = stream[i]
        print ("Reading " + x + " from stream")
 
        # We process this character only if it has not occurred
        # or occurred only once. repeated[x] is true if x is
        # repeated twice or more.s
        if not repeated[ord(x)]:
 
            # If the character is not in DLL, then add this
            # at the end of DLL
            if not x in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)
                repeated[ord(x)] = True
 
        if len(inDLL) != 0:
            print ("First non-repeating character so far is ")
            print (str(inDLL[0]))
 
# Driver program
findFirstNonRepeating()
