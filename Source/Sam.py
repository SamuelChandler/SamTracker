# A class representing me and all my relevant information
# Sam Chandler 1/4/2023

#imports
import Tasks


class Sam:
    
    #usually static
    Height = [5,11]                     #the Height of Sam [feet,inches]
    Weight = 204                        #Weight of Sam in Lbs 
    Age = 23                            #Age of Sam in Years 
    Gym_Days = ["Push", "Pull", "Leg"]  #the list of possible exercises that can be done
    Task_List = []
    
    #updated Daily
    Meals = [False,False,False] #The Meals eaten today [Breakfast, Lunch, Dinner]
    Gym_Completed = False       #tracks if I went the gym today
    Next_Gym_Day = Gym_Days[0]  #tracks the current gym day im on


    def __init__(self) -> None:
        pass

    def Add_Task(self,Name,Pri,Genre):
        self.Task_List.append(Tasks.Task(Name,Pri,Genre))
        print(self.Task_List[0].Get_Name())
        
        
        pass

sam = Sam()
sam.Add_Task("Test",1,"Default")