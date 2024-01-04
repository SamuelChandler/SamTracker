
class Sam:
    
    #usually static
    Height = [5,11] #the Height of Sam [feet,inches]
    Weight = 204    #Weight of Sam in Lbs 
    Age = 23        #Age of Sam in Years 
    Gym_Days = ["Push", "Pull", "Leg"] #the list of possible excercises that can be done

    
    #updated Daily
    Meals = [False,False,False] #The Meals eaten today [Breakfast, Lunch, Dinner]
    Gym_Completed = False
    Next_Gym_Day = Gym_Days[0]

    def __init__(self) -> None:
        print(self.Next_Gym_Day)
        
        pass

sam = Sam()