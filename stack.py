class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack :
    def __init__(self,data):
        new_node = Node(data)
        self.top = new_node
        self.hieght = 1 
           
    def Print_list(self):
        if self.hieght == 0 :
            print("stack is empty")
        else:
            
            temp = self.top
            while temp is not None:
        
                print(temp.data, end=" ")
                temp = temp.next
        
    def Append(self, data):
        new_node = Node(data)
        if self.hieght == 0 :
            self.top == new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.hieght += 1 
    
    
    def Pop(self):
        
        if self.hieght == 0 :
            print("Stack is empty you cont remover ")
        else:
            temp = self.top
            self.top = self.top.next
            print("this value is removes",temp)
            temp.next = None

            self.hieght -= 1 
            return temp.data
        
    
        
mystack = Stack(1)
mystack.Append(4)
mystack.Append(4)
mystack.Append(4)
mystack.Append(4)

mystack.Pop()
mystack.Print_list()