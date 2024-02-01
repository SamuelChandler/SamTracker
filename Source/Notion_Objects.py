class Grocery_Item():

    name = str
    type = str
    collected = bool

    def __init__(self,n,t,c):
        self.name = n
        self.type = t
        self.collected = c

    #prints to cmd the atributes, broken
    def display(self):
        print(self.name,self.type,self.collected)

    #formats to data dictionary for post to notion
    def to_Data(self,db_ID):

        data = {
            "parent": { "database_id": db_ID },
            "properties": {
                "Name": { "title": [ { "text": { "content": self.name}}]},
                "Collected" : { "checkbox": self.collected},
                "Type":{"select":{"name": self.type}}
            }
        }

        return data


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

    def to_Data():
        pass #formats to data dictionary for post to notion

class School_Task():

    name = str
    course = str
    status = str
    type = str

    def __init__(self,n,c,s,t):
        self.name = n
        self.course = c
        self.status = s
        self.type = t

    def display(self):
        print(self.name,self.course,self.status,self.type)

    def to_Data():
        pass #formats to data dictionary for post to notion
