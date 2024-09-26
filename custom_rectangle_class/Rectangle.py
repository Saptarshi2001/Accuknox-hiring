class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.index=0
        
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        if self.index==0:
            self.index+=1
            return {'length':self.length}
        elif self.index==1:
            self.index+=1
            return {'width':self.width}
        else:
            raise StopIteration



    
    


lst=['length','width']
lb={}
rect=Rectangle(2,3)
for i in rect:
    print(i)


