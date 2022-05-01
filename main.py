# Assignment 3 Dairy Application

def GET_DATE():
    
    while(1):
        Valid = True
        #retreive date
        User_Date_Input = input("Please enter the date of the event (dd/mm/yyyy)\n")
        #varify input format
        if len(User_Date_Input)==10:
            for x in [0,1,3,4,6,7,8,9]:
                if not(ord(User_Date_Input[x]) in range(48,58)):
                    Valid = False
            for x in [2,5]:
                if not(ord(User_Date_Input[x]) == 47):
                    Valid = False
        else:
            Valid = False
        print(Valid)
        if Valid == True:
            break
        print("Invalid input format. Please try again")
    return User_Date_Input

    
GET_DATE()
