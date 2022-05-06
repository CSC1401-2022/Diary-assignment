# Assignment 3 Dairy Application

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
# Validate_Date()
##########	
# inputs:
# 	Date_rawInput, string
# outputs:
# 	name, type
##########
# Checking for leap year and each month has correct number of days.  
##########
# Author: Anthony Mann
# 02/05/2022
# History
#	Rev1, 02/05/2022, Anthony Mann: checking for a valid date in the givin year
####################################################



def Add_Record():
    newDate = GET_DATE()
    validDate = Validate_Date()
    priority = GET_PRIORITY()
    startTime = GET_START_TIME()
    endTime = GET_END_TIME()
    desc = GET_DESCRIPTOR()
    # isValidDate = False
    if validDate == True:
        priority
        startTime
        endTime
        desc
        newRecord = f'{priority};{newDate};{startTime};{endTime};{desc};'
        Diary.append(newRecord)
        return newRecord
    else:
        print("Not Valid")
    

def Validate_Date():
    newDate = GET_DATE()
    day = newDate[0:2]
    month = newDate[3:5]
    year = newDate[6:10]
    if int(day) <= 31 and int(month) == 1 or  int(month) == 3 or  int(month) == 5 or  int(month) == 7 or  int(month) == 8 or  int(month) == 10 or  int(month) == 12: 
        print(month)
        print('Is a 31 day month')
        # isValidDate = True
        print(f'{day}/{month}/{year}')
        return  day, month, year

    elif int(day) <= 30 and int(month) == 4 or  int(month) == 6 or  int(month) == 9 or  int(month) == 11:
        print(month)
        print('Is a 30 day month')
        # isValidDate = True
        return  f'{day}/{month}/{year}'

    elif int(day) <= 29 and int(year) % 4 == 0 and int(month) == 2:
        print(year)
        print(month)
        print('It is Leap year Febuary')
        # isValidDate = True
        return  f'{day}/{month}/{year}'

    elif int(day) <= 28 and int(year)  and int(month) == 2:
        print(year)
        print(month)
        print('It is NOT Leap year Febuary')
        isValidDate = True 
        return  f'{day}/{month}/{year}'

    if int(month) >12 or int(month) <1:
        print('Invalid Month, Please Try again')
        isValidDate = False
    elif int(day) >31 or int(day) <1:
        print('Invalid Day, Please Try again')
        isValidDate = False
    else:
        'Please Check your Date and Try again'
        isValidDate = False
    return isValidDate 





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

def GET_DESCRIPTOR():
    while(1):
        #retreive date
        DESCRIPTOR_rawInput = input("Please enter a name for the event (30 charictors maximum)\n")
        #varify input format
        if len(DESCRIPTOR_rawInput)<31:
            while len(DESCRIPTOR_rawInput)<30:
                DESCRIPTOR_rawInput=DESCRIPTOR_rawInput
                break
            break
        print("To many charicters. Please try again")
    
    return DESCRIPTOR_rawInput

def GET_PRIORITY():
    while(1):
        #retreive date
        PRIORITY_rawInput = input("Please enter a priority for the event (High,Medium,Low)\n")
        #varify input format
        if PRIORITY_rawInput.lower() == "high" or PRIORITY_rawInput.lower() == 'h':
            PRIORITY = "High"
            break
        if PRIORITY_rawInput.lower() == "medium" or PRIORITY_rawInput.lower() == 'm':
            PRIORITY = "Medium"
            break
        if PRIORITY_rawInput.lower() == "low" or PRIORITY_rawInput.lower() == 'l':
            PRIORITY = "Low"
            break
        print("Invalid input. Please try again")
    return PRIORITY


Diary=[]



# Diary.append({"date": '23/05/1987', 'StartTime': int(10), 'EndTime': int(12), 'Description': 'My B\'day','priority': 'High'})
while 1:
    menu=True
    while menu:
        print(Diary)
        if len(Diary) > 0:
            for entry in Diary:
                print('\n')
                # print('Appointment Info: \n' + 'Date: ' +  str(entry['date' ]), 'Start Time: ' + str(entry['StartTime']), 'End Time: ' + str(entry['EndTime']), entry['Description'], entry['priority'] )
                # print(entry['date' ])
        
        print('\n Select Add new record to create a new appointment')        
        print("""
        1. Add Record
        2. Sort Records
        3. Exit
        """)


        Menu_Response_rawInput=input("Dear Diary, I would like to: \n")
        if Menu_Response_rawInput == "1":
            print('\n Adding A Record')

            Add_Record()
        elif Menu_Response_rawInput == '2':
            print('\n Sorting Your Records')
        elif Menu_Response_rawInput == '3':
            print('\n Thanks for using Dear Diary, see you next time \n')
            break
        else:
            print('\n I\'m sorry that response is not recognised please try again')
        

