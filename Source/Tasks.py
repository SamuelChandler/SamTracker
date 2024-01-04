
class Task:
    
    Name = str
    Priority = int
    Genre = str

    def __init__(self,N,P,G) -> None:
        self.Name = N
        self.Priority = P
        self.Genre = G
        pass

    def Get_Name(self):
        return self.Name