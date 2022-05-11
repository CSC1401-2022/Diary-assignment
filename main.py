# Assignment 3 Dairy Application
##import calls##
import time
################
##Global Variables##
#                 10        20        30        40 
#       012345678901234567890123456789012345678901234567890123
Diary=["MEDIUM;10/06/2022;07;22;Testing entry one             ",
       "LOW   ;01/09/2022;12;22;Testing entry two             ",
       "HIGH  ;20/07/2023;10;15;Testing entry three           "]

##constants##
PRIORITY_START = 0
PRIORITY_END = 6
DATE_START = 7
DATE_END = 17
STARTTIME_START = 18
STARTTIME_END = 20
ENDTIME_START = 21
ENDTIME_END = 23
DISCRIPTION_START = 24
DISCRIPTION_END = 44
DAY_START = 0
DAY_END = 2
MONTH_START = 3
MONTH_END = 5
YEAR_START = 6
YEAR_END = 10
####################

####################################################
# IS_CONCURRENT_APPOINTMENT(start,end,date)
# ##########	
# inputs:
#   start, int:
#       The hour of the start time (validated)
#   end, int:
#       The hour of the end time (validated)
#   date, str[10],("dd/mm/yyyy"):
#       The date input from the user (validated)
# outputs:
# 	(unnamed), bool:
#       Wether of not the apointment is concurrent as a True/False boolean
#           If there is an apointment overlap returns True. No overlap = False
# ##########
#   Searches through Diary[] and checks for overlappong apointments between the
#   new entry and current entries. Requirse a global array of strings named Diary 
#   formated "Priority[6];Date[10];start time[2];end time[2];discription[30]"
#               (e.g "High  ;23/09/2022;09;10;CSC1401 class                 ")
# ##########
# Author: Timothy van den Bosch
# Date: 03/05/2022
# History
# 	Rev 1.0: 03/05/2022, Timothy van den Bosch
#        Completed function
####################################################

def IS_CONCURRENT_APPOINTMENT(start, end, date):
    #first check for same day entries. If the new event dosn't share a day there is no overlap
    NDay = int(date[DAY_START:DAY_END])
    NMonth = int(date[MONTH_START:MONTH_END])
    NYear = int(date[YEAR_START:YEAR_END])
    for entry in Diary: 
        EDate = entry[DATE_START:DATE_END]
        EDay = int(EDate[DAY_START:DAY_END])
        EMonth = int(EDate[MONTH_START:MONTH_END])
        EYear = int(EDate[YEAR_START:YEAR_END])
        if EYear == NYear and EMonth == NMonth and EDay == NDay:#is the same day
            #check for time overlap
            EStart = int(entry[STARTTIME_START:STARTTIME_END])
            EEnd = int(entry[ENDTIME_START:ENDTIME_END])
            if (EStart<=start<EEnd) or (start<=EStart<end):
                print("Warning!\n\tThe new entry overlaps with the current entry: "+entry[24:44]+":\n\t"+entry[18:20]+" to "+entry[21:23]+" on "+entry[7:17])
                return True
    print("No overlaps detected!")
    return False #no overlaps

####################################################
# VALIDATE_TIME(start,end,date)
# ##########	
# inputs:
#   start, int:
#       The hour of the start time (not validated)
#   end, int:
#       The hour of the end time (not validated)
#   date, str[10],("dd/mm/yyyy"):
#       The date input from the user (validated)
# outputs:
# 	(unnamed), bool:
#       The validity of the inputed time as a True/False boolean.
# ##########
#   Checks the start and end time for validity (start>=7 end<=22 and start<end).
#   Considering date and time, checks the time is in the futer. (Requirse librarie time).
#   If both checks pass outputs True. If ether fail an error is displayed and False is passed
# ##########
# Author: Timothy van den Bosch
# Date: 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################

def VALIDATE_TIME(start, end, date):
    if not (start>=7 and end <=22 and start<end):
        print("Time not valid: Start and/or end times do not meet conditions")
        return False
    DDay = int(date[DAY_START:DAY_END])-time.localtime().tm_mday
    DMonth = int(date[MONTH_START:MONTH_END])-time.localtime().tm_mon
    DYear = int(date[YEAR_START:YEAR_END])-time.localtime().tm_year
    DStart = start-time.localtime().tm_hour
    if DYear > 0:
        return True
    if DYear==0: 
        if DMonth>0:
            return True
        if DMonth==0:
            if DDay>0:
                return True
            if DDay==0:
                if DStart > 0:
                    return True
    print("Time not valid: Given time is in the past.")            
    return False 
    
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
# Date: 02/05/2022
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




# DAYS_IN_MONTH()
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
# Date: 02/05/2022
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
# Date: 02/05/2022
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
                    break
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
# Date: 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
####################################################
def GET_DESCRIPTOR():
    while(1):
        #retreive date
        DESCRIPTOR_rawInput = input("Please enter a name for the event (30 charicters maximum)\n")
        #varify input format
        if len(DESCRIPTOR_rawInput)<=30:
            while len(DESCRIPTOR_rawInput)<30:
                DESCRIPTOR_rawInput=DESCRIPTOR_rawInput
                break
            break
        print("Too many charicters. Please try again")
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
# Date: 02/05/2022
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
# SORT_RECORD()
# ##########	
# inputs:
#   None
# outputs:
# 	None
# ##########
#   Retreaves the argument of the sort. 
#   pulls the argument from Diary with index number.
#   quantifies the argument
#   performs a bubble sort on the argument
#   Result of bubble sort is a sorted Diary variable.
#   Result is displayed using the print function
#   loops untill END is passed (case insensitive)
# ##########
# Author: Timothy van den Bosch
# Date: 03/05/2022
# History
# 	Rev 1.0: 03/05/2022, Timothy van den Bosch
#        Function complete
####################################################
def SORT_RECORD():  
    print("Sorting Diary:")
    if not(len(Diary) > 0):
        print("Diary is empty/nExiting sort:")
        return
    while(1):
        Qarg = []
        #get user input
        argument_raw = input("Would you like to sort by priority or time? (type 'end' to exit)\n")
        if argument_raw.lower()== "end":
            break
        elif argument_raw.lower()== "priority":
            #retrive relevent argument from diary. Quantify in new list to sort
            for diaryIndex in range(0,len(Diary)):
                if Diary[diaryIndex][PRIORITY_START:PRIORITY_END] == "HIGH  ":
                    Qarg.append(1)
                elif Diary[diaryIndex][PRIORITY_START:PRIORITY_END] == "MEDIUM":
                    Qarg.append(2)
                else:
                    Qarg.append(3)
        elif argument_raw.lower()== "time":
            for diaryIndex in range(0,len(Diary)):
                date = Diary[diaryIndex][DATE_START:DATE_END]
                time = Diary[diaryIndex][STARTTIME_START:STARTTIME_END]
                Qarg.append(int(date[YEAR_START:YEAR_END]+date[MONTH_START:MONTH_END] + date[DAY_START:DAY_END]+time))
        else:
            print("\n I\'m sorry that response is not recognised please try again")
            
        if len(Qarg) > 0:#perform the sort
            swaps=1
            while(swaps !=0 ):
                swaps = 0
                for index in range(1,len(Qarg)):
                    if Qarg[index]<Qarg[index-1]:
                        swaps = swaps+1
                        Diary.insert(index-1, Diary.pop(index))
                        Qarg.insert(index-1, Qarg.pop(index))
            print("Sort complete")
            PRINT_DIARY()
    print("Exiting sort:")
    

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
# Author: --
# Date: --
# History
# 	Rev --: --/--/----, --
#        --
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
            print('\n')
            print('Appointment Info: \n' + 'Date: ' +  entry[DATE_START:DATE_END], 'Start Time: ' + entry[STARTTIME_START:STARTTIME_END], 'End Time: ' + entry[ENDTIME_START:ENDTIME_END], entry[DISCRIPTION_START:DISCRIPTION_END], entry[PRIORITY_START:PRIORITY_END] )
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
        

