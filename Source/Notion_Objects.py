class Grocery_Item():

    name = str
    type = str
    collected = bool

    def __init__(self,n,t,c):
        self.name = n
        self.type = t
        self.collected = c

    def display(self):
        print(self.name,self.type,self.collected)