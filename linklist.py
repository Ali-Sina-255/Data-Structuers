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
            
            print(temp.value)
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
    
    
            
first = Linklist(11)
first.Append(1)
first.Append(10)
first.Print_lsit()
