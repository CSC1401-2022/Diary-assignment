# Assignment 3 Dairy Application

####################################################
# GET_DATE()
# ##########	
# inputs:
#   None
# outputs:
# 	Date_rawInput, str:
#       The Date given by the user in the following format (dd/mm/yyyy)
# ##########
#   Takes the user input from a promt and validates format before returning.
# ##########
# Author: Timothy van den Bosch
# Date of 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################
def GET_DATE():
    while(1):
        Valid = True
        #retreive date
        Date_rawInput = input("Please enter the date of the event (dd/mm/yyyy)\n")
        #varify input format
        if len(Date_rawInput)==10:
            for x in [0,1,3,4,6,7,8,9]:
                if not(ord(Date_rawInput[x]) in range(48,58)):
                    Valid = False
            for x in [2,5]:
                if not(ord(Date_rawInput[x]) == 47):
                    Valid = False
        else:
            Valid = False
        if Valid == True:
            break
        print("Invalid input format. Please try again")
    return Date_rawInput

####################################################
# GET_START_TIME()
# ##########	
# inputs:
#   None
# outputs:
# 	Start_Time_rawInput, int:
#       The start time of an event given by the user as a number
# ##########
#   Takes the user input from a promt and validates format (i.e. is a at most a 2 diget number) before returning.
# ##########
# Author: Timothy van den Bosch
# Date of 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################
def GET_START_TIME():
    while(1):
        Valid = True
        #retreive date
        Start_Time_rawInput = input("Please enter the start time of the event (7 to 21)\n")
        #varify input format
        if len(Start_Time_rawInput)<3 and len(Start_Time_rawInput)>0 :
            for x in Start_Time_rawInput:
                if not(ord(x) in range(48,58)):
                    Valid = False
        else:
            Valid = False
        if Valid == True:
            break
        print("Invalid input format. Please try again")
    return int(Start_Time_rawInput)

####################################################
# GET_END_TIME()
# ##########	
# inputs:
#   None
# outputs:
# 	End_Time_rawInput, int:
#       The end time of an event given by the user as a number
# ##########
#   Takes the user input from a promt and validates format (i.e. is a at most a 2 diget number) before returning.
# ##########
# Author: Timothy van den Bosch
# Date of 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################
def GET_END_TIME():
    while(1):
        Valid = True
        #retreive date
        End_Time_rawInput = input("Please enter the end time of the event (8 to 22)\n")
        #varify input format
        if len(End_Time_rawInput)<3 and len(End_Time_rawInput)>0 :
            for x in End_Time_rawInput:
                if not(ord(x) in range(48,58)):
                    Valid = False
        else:
            Valid = False
        if Valid == True:
            break
        print("Invalid input format. Please try again")
    return int(End_Time_rawInput)

####################################################
# GET_DESCRIPTOR()
# ##########	
# inputs:
#   None
# outputs:
# 	DESCRIPTOR_rawInput, str:
#       The discription of an event given by the user as a string 30 charicters long
# ##########
#   Takes the user input from a promt and validates format (i.e. is <=30 charicters long).
#   It will append spaces until the string is exactly 30 charicters long before returning.
# ##########
# Author: Timothy van den Bosch
# Date of 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################
def GET_DESCRIPTOR():
    while(1):
        #retreive date
        DESCRIPTOR_rawInput = input("Please enter a name for the event (30 charicters maximum)\n")
        #varify input format
        if len(DESCRIPTOR_rawInput)<31:
            while len(DESCRIPTOR_rawInput)<30:
                DESCRIPTOR_rawInput=DESCRIPTOR_rawInput + ' '
            break
        print("To many charicters. Please try again")
    return DESCRIPTOR_rawInput

####################################################
# GET_PRIORITY()
# ##########	
# inputs:
#   None
# outputs:
# 	PRIORITY, str:
#       The Priority of an event given by the user as a string 6 charicters long
# ##########
#   Takes the user input from a promt and validates format. The input is not case sensitive and excepts "high", "h","medium", "h","low" and "l".
#    Returns "HIGH  ", "MEDIUM" or "LOW   " based on the user input 
# ##########
# Author: Timothy van den Bosch
# Date of 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################
def GET_PRIORITY():
    while(1):
        #retreive date
        PRIORITY_rawInput = input("Please enter a priority for the event (High,Medium,Low)\n")
        #varify input format
        if PRIORITY_rawInput.lower() == "high" or PRIORITY_rawInput.lower() == 'h':
            PRIORITY = "HIGH  "
            break
        if PRIORITY_rawInput.lower() == "medium" or PRIORITY_rawInput.lower() == 'm':
            PRIORITY = "MEDIUM"
            break
        if PRIORITY_rawInput.lower() == "low" or PRIORITY_rawInput.lower() == 'l':
            PRIORITY = "LOW   "
            break
        print("Invalid input. Please try again")
    return PRIORITY


Diary=[]
Diary.append({"date": '23/05/1987', 'StartTime': int(10), 'EndTime': int(12), 'Description': 'My B\'day','priority': 'High'})

menu=True
while menu:
    if len(Diary) > 0:
        for entry in Diary:
            print('\n')
            print('Appointment Info: \n' + 'Date: ' +  entry['date' ], 'Start Time: ' + str(entry['StartTime']), 'End Time: ' + str(entry['EndTime']), entry['Description'], entry['priority'] )
    else:
        print('\n Select Add new record to create a new appointment')        
    print("""
    1. Add Record
    2. Sort Records
    3. Exit
    """)


    Menu_Response_rawInput=input("Dear Diary, I would like to: \n")
    if Menu_Response_rawInput == "1":
        # GET_DATE()
        # GET_START_TIME()
        # GET_END_TIME()
        # GET_DESCRIPTOR()
        # GET_PRIORITY()
        print('\n Adding A Record')
    elif Menu_Response_rawInput == '2':
        print('\n Sorting Your Records')
    elif Menu_Response_rawInput == '3':
        break
    else:
        print('\n I\'m sorry that response is not recognised please try again')
        