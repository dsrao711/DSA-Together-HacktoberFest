# Implementing stacks 

def CreateStack():
  stack = []
  return stack


def isEmpty(stack):
  if(len(stack) == 0):
    print("Stack is empty.")
  else:
    print("Stack is not empty.") 
      
def size(stack):
  return len(stack)

    
def push(stack, newElement):
  stack.append(newElement)
  print(newElement, "is added into the stack.")
   
def pop(stack):
  print(stack.pop(), "is deleted from the stack.")

     
def topElement(stack):
  return stack[len(stack) - 1]

def PrintStack(stack):
    print(' '.join(stack))

# test the code                
MyStack = CreateStack()

push(MyStack, 10)
push(MyStack, 20)
push(MyStack, 30)
push(MyStack, 40)

pop(MyStack)
isEmpty(MyStack)
