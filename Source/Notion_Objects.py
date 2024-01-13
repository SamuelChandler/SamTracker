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


class Personal_Task():

    name = str
    catagory = str
    status = str

    def __init__(self,n,c,s):
        self.name = n
        self.catagory = c
        self.status = s

    def display(self):
        print(self.name,self.catagory,self.status)

    