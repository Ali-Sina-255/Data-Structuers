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
    
    def Perpend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.lenght += 1
        return  True
    
    def Pop_first(self):
        if self.lenght == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.lenght -= 1
            
            if self.lenght ==0:
                
                self.tail = None
                
            return temp
    
    
    def Get(self, index):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
        
        
        
        
first = Linklist(11)
first.Append(1)
first.Append(100)
first.Append(200)
first.Append(4234)
first.Perpend(0)
# first.Perpend(0.121)
first.Pop_first()
# first.Pop()
first.Perpend(0)
print(first.Get(3))
first.Print_lsit()
