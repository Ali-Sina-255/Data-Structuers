class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        
class Linklist:
    def __init__(self,value) -> None:
        new_node =  Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght =  1 
    
    
    def Print_lsit(self):
        
        temp = self.head
        while temp is not None:
            
            print(temp.value, "-->", end=" ")
            temp = temp.next
    
    
    def Append(self,value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght  +=1
    
    
    def Pop(self):
        if self.lenght == 0:
            return None
        temp = self.head
        pre = self.tail
        while temp.next is not None:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1
        
        if self.lenght == 0:
            self.head = None
            self.tail  = None
        return temp
        
            
    
            
first = Linklist(11)
first.Append(1)
first.Append(100)
first.Append(200)
first.Append(4234)
first.Pop()
first.Print_lsit()
