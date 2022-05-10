# Assignment 3 Dairy Application

Diary=[]


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
# VALIDATE_DATE()
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

def DAYS_IN_MONTH(month, year):
    thirtyOneDay = [1,3,5,7,8,10,12]
    thirtyDay = [4,6,9,11]
    if month in thirtyOneDay:
       Days = 31
       return Days
    if month in thirtyDay:
       Days = 30
       return Days
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                 return 29 
        else:
            return 28


def VALIDATE_DATE(date):
    year = int(date[6:10])
    month = int(date[3:5])
    day = int(date[:2])
    if year > 2021 and year < 10000:
        if month > 0 and month < 13:
            if day <= DAYS_IN_MONTH(month, year):
                print('Date is valid')
                return True
            else:
                print('Please Check that the Day is within Range')
                return False
        else:
            print('Check that the Month is a within Range')
            return False
    else:
        print('Check that the Year is a within Range')
        return False
    

# print(VALIDATE_DATE('29/02/1922'))
    

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
            PRIORITY = "High  "
            break
        if PRIORITY_rawInput.lower() == "medium" or PRIORITY_rawInput.lower() == 'm':
            PRIORITY = "Medium"
            break
        if PRIORITY_rawInput.lower() == "low" or PRIORITY_rawInput.lower() == 'l':
            PRIORITY = "Low   "
            break
        print("Invalid input. Please try again")
    return PRIORITY

####################################################
# ADD_RECORD()
# ##########	
# inputs:
#   None
# outputs:
# 	None
# ##########
#   Retrives event infomation from user using the GET_ functions. 
#   Validiates the retreaved event infomation using the VALIDATE_ functions
#   Creates a string describing the new event in the following format 
#       "Priority[6];Date[10];start time[2];end time[2];discription[30]"
#       (e.g "High  ;23/09/2022;09;10;CSC1401 class                 ")
#   Appends the string to array Diary[]
# ##########
# Author: Anthony Mann
# Date: 07/05/2022
# History
# 	Rev1, 07/05/2022, Anthony Mann: Creates the record for the diary entry
####################################################


def ADD_RECORD():
    while 1:
        date = GET_DATE()
        if VALIDATE_DATE(date) == True:
            break
        else:
            print("Err: Invalid Date")
        break
    descriptor = GET_DESCRIPTOR()
    priority = GET_PRIORITY()
    startTime = GET_START_TIME()
    endTime = GET_END_TIME()
    entry = [priority.rstrip() + ';' ,date + ';', str(startTime) + ';', str(endTime) + ';' , descriptor.rstrip() + ';']
    Diary.append(entry)
    PRINT_DIARY()

####################################################
# PRINT_DIARY()
# ##########	
# inputs:
#   None
# outputs:
# 	None
# ##########
#   Prints the Diary Entries in a table format. 
#   
#   
# Author: Anthony Mann
# Date: 07/05/2022
# History
# 	Rev1, 07/05/2022, Anthony Mann: Creates the record for the diary entry
####################################################

# Diary.append({"date": "23/05/1987", "StartTime": int(10), "EndTime": int(12), "Description": 'My B\'day','priority': 'High'})
# print(Diary[0]["date"])

def PRINT_DIARY():
    spaceBetween = "   "
    pHeader = "Priority"
    dHeader = "Date      "
    tSHeader = "Start"
    tEHeader = "End"
    dSHeader = "Description                     "
    header = pHeader + spaceBetween + dHeader + spaceBetween + tSHeader + spaceBetween + tEHeader + spaceBetween + dSHeader
    bar = '-' * len(pHeader) + spaceBetween + '-' * len(dHeader) + spaceBetween + '-' * len(tSHeader) + spaceBetween + '-' * len(tEHeader) + spaceBetween + '-' * len(dSHeader)
    print('\n' + header + '\n' + bar)

    if len(Diary) > 0:
        for entry in Diary:
            print(len(entry[1]))
            print( len(entry[0]))
            print(entry[0], entry[1],)
            # print('Date: ' +  entry[DATE_START:DATE_END], 'Start Time: ' + entry[STARTTIME_START:STARTTIME_END], 'End Time: ' + entry[ENDTIME_START:ENDTIME_END], entry[DISCRIPTION_START:DISCRIPTION_END], entry[PRIORITY_START:PRIORITY_END] )
    else:
        print('\n Select Add new record to create a new appointment') 


####################################################
# Menu (Not a Function)	
# ##########
#   Creates a menu using a loop that is always true unless the user exits. 
#   Each selection peforms a seperate task including:
#   Creating a new record, Sorting created records and Exiting the application.
# ##########
# Author: Anthony Mann
# Date: 02/05/2022
# History
# 	Rev1, 02/05/2022, Anthony Mann: Creates the record for the diary entry
####################################################



while 1:
    menu=True
    while menu:
           
        print("""
        1. Add Record
        2. Sort Records
        3. Exit
        """)


        Menu_Response_rawInput=input("Dear Diary, I would like to: \n")
        if Menu_Response_rawInput == "1":
            print("\n Adding A Record")
            ADD_RECORD()
        elif Menu_Response_rawInput == "2":
            print("\n Sorting Your Records")
        elif Menu_Response_rawInput == "3":
            print("\n Thanks for using Dear Diary, see you next time \n")
            break
        else:
            print("\n I\'m sorry that response is not recognised please try again")
        

