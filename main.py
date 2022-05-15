# Assignment 3 Dairy Application
##import calls##
import time
   
################
##Global Variables##
#                 10        20        30        40        50
#       012345678901234567890123456789012345678901234567890123
#      "HIGH;10/06/2022;07;22;Example Entry                 "
Diary=[]

##constants##
PRIORITY_START = 0
PRIORITY_END = 4
DATE_START = 5
DATE_END = 15
STARTTIME_START = 16
STARTTIME_END = 18
ENDTIME_START = 19
ENDTIME_END = 21
DISCRIPTION_START = 22
DISCRIPTION_END = 52
DAY_START = 0
DAY_END = 2
MONTH_START = 3
MONTH_END = 5
YEAR_START = 6
YEAR_END = 10
####################

##Get_functions##

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
        Date_rawInput = input("Please enter the date of the event (dd/mm/yyyy) (type 'end' to exit)\n")
        #varify input format
        if Date_rawInput == "end":
            return False
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
        if len(DESCRIPTOR_rawInput)==0:
            print("Name length must be none zero. Please try again")
        elif len(DESCRIPTOR_rawInput)<=30:
            while len(DESCRIPTOR_rawInput)<30:
                DESCRIPTOR_rawInput=DESCRIPTOR_rawInput+' '
                break
            break
        else:
            print("Too many charicters. Please try again")
    return DESCRIPTOR_rawInput

####################################################
# GET_PRIORITY()
# ##########	
# inputs:
#   None
# outputs:
# 	PRIORITY, str:
#       The Priority of an event given by the user as a string 4 charicters long
# ##########
#   Takes the user input from a promt and validates format. 
#   The input is not case sensitive and excepts "high", "h","low" and "l".
#    Returns "HIGH" or "LOW " based on the user input 
# ##########
# Author: Timothy van den Bosch
# Date: 02/05/2022
# History
# 	Rev 1.0: 02/05/2022, Timothy van den Bosch
#        Completed function
#   Rev 1.1: 11/05/2022, Timothy van den Bosch
#       Removed the extra priority medium
####################################################
def GET_PRIORITY():
    while(1):
        #retreive date
        PRIORITY_rawInput = input("Please enter a priority for the event (High/Low)\n")
        #varify input format
        if PRIORITY_rawInput.lower() == "high" or PRIORITY_rawInput.lower() == 'h':
            PRIORITY = "HIGH"
            break
        if PRIORITY_rawInput.lower() == "low" or PRIORITY_rawInput.lower() == 'l':
            PRIORITY = "LOW "
            break
        print("Invalid input. Please try again")
    return PRIORITY

##validation##

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
                print("Warning!\n\tThe new entry overlaps with the current entry: "+entry[DISCRIPTION_START:DISCRIPTION_END]+"\n\tFrom "+entry[STARTTIME_START:STARTTIME_END]+" to "+entry[ENDTIME_START:ENDTIME_END]+" on "+entry[DATE_START:DATE_END])
                return True
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
# VALIDATE_DATE()
##########	
# inputs:
# 	date, string
#       the date in question formated as the following "dd/mm/yyyy"
# outputs:
# 	valid, bool
#       the validity of the given date
##########
# Checking for leap year and each month has correct number of days.  
##########
# Author: Anthony Mann
# 02/05/2022
# History
#	Rev1, 02/05/2022, Anthony Mann: checking for a valid date in the givin year
####################################################
def VALIDATE_DATE(date):
    year = int(date[YEAR_START:YEAR_END])
    month = int(date[MONTH_START:MONTH_END])
    day = int(date[DAY_START:DAY_END])
    if year > 2021 and year < 10000:
        if month > 0 and month < 13:
            if day <= DAYS_IN_MONTH(month, year):
                return True
            else:
                print('Warning!\n\tGiven date is invalid \n\tPlease check that the day is within the an exceptable range')
                return False
        else:
            print('Warning!\n\tGiven date is invalid \n\tPlease check that the month is within the an exceptable range')
            return False
    else:
        print('Warning!\n\tGiven date is invalid \n\tPlease check that the year is within the an exceptable range')
        return False
    
####################################################
# DAYS_IN_MONTH(month, year)
##########	
# inputs:
# 	month, int:
#       The month on which to check
#   year, int
#       The year of the month in question (is only considerd for Febuary)
# outputs:
# 	Days, int:
#       The number of days in the given month (considering the year)
##########
#   Checks the month and returns the number of days in the given month
#   if the month given is Febuary considers the year input to determain if its a leep year
#       number of days reurned is adjusted acordingly.
##########
# Author: Anthony Mann
# 02/05/2022
# History
#	Rev1, 02/05/2022, Anthony Mann: 
#       Function complete
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
        
##main operational functions##
 
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
#   Rev 1.1: 11/05/2022, Timothy van den Bosch
#       Removed the extra priority medium
####################################################
def SORT_RECORD():  
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
                if Diary[diaryIndex][PRIORITY_START:PRIORITY_END] == "HIGH":
                    Qarg.append(1)
                else:
                    Qarg.append(2)
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
#   loop, bool
#       The loop condition. False - runs once
#                           True - runs indefinitely
# outputs:
# 	None
# ##########
#   Retrives event infomation from user using the GET_ functions. 
#   Validiates the retreaved event infomation using the VALIDATE_ functions
#   Creates a string describing the new event in the following format 
#       "Priority[4];Date[10];start time[2];end time[2];discription[30]"
#       (e.g "HIGH;23/09/2022;09;10;CSC1401 class                 ")
#   Appends the string to array Diary[]
# ##########
# Author: Anthony Mann
# Date: 07/05/2022
# History
# 	Rev 1.0: 07/05/2022, Anthony Mann
#        Creates the record for the diary entry
#   Rev 1.1: 11/05/2022, Timothy van den Bosch
#           nested get date and time to allow for re-entry 
#               of date when time given is in the past
#           Added an exit condition to the date retrieval for leaveing the ADD_RECORD state
#           Added a condition to the main loop- can be made to run once by passing False (used in editing records)
####################################################
def ADD_RECORD(loop):
    LOOP=True;
    while LOOP:
        while 1:
            while 1:
                while 1:
                    date = GET_DATE()
                    if date == False:
                        return False #used to catch early exit (used in editing records)
                    if VALIDATE_DATE(date) == True:
                        break
            
                startTime = GET_START_TIME()
                endTime = GET_END_TIME()
                if VALIDATE_TIME(startTime,endTime,date) == True: 
                    break
            if IS_CONCURRENT_APPOINTMENT(startTime,endTime,date) == False:
                break
    
        descriptor = GET_DESCRIPTOR()
        priority = GET_PRIORITY()
        strStartTime = str(startTime)
        if len(strStartTime) < 2:
            strStartTime = '0' + strStartTime
    
        strEndTime = str(endTime)
        if len(strEndTime) < 2:
            strEndTime = '0' + strEndTime
    
        Diary.append(priority+';' + date+';' + strStartTime+';' + strEndTime+';' + descriptor)
        PRINT_DIARY()
        LOOP=loop

####################################################
# PRINT_DIARY()
# ##########	
# inputs:
#   None
# outputs:
# 	None
# ##########
#   Prints the Diary Entries in a table format. 
# ##########    
# Author: Anthony Mann
# Date: 07/05/2022
# History
# 	Rev1, 07/05/2022, Anthony Mann: 
#       Function complete
####################################################
def PRINT_DIARY():
    if len(Diary) > 0:
        print("Index    Priority   Date         Start   End   Description")
        print("-----    --------   ----------   -----   ---   --------------------------------")
        for index in range(0,len(Diary)):
            strIndex = str(index)
            while len(strIndex)<5:
                strIndex=strIndex+" "
            print(strIndex+"    "+Diary[index][PRIORITY_START:PRIORITY_END]+"       "+ Diary[index][DATE_START:DATE_END] +"   " + Diary[index][STARTTIME_START:STARTTIME_END], "     " + Diary[index][ENDTIME_START:ENDTIME_END] + "    " +Diary[index][DISCRIPTION_START:DISCRIPTION_END])
    else:
        print('\n No entries in Diary\n Please select Add Record to create a new appointment')        

####################################################
# EDIT_RECORD()
# ##########	
# inputs:
#   None
# outputs:
# 	None
# ##########
#   edits a record. selection by user prompts.
#   can edit indavidual items or the entir entry.
#   Has date, time and concurancy checks 
# ##########    
# Author: Timothy van den Bosch
# Date: 11/05/2022
# History
# 	Rev1, 07/05/2022, Timothy van den Bosch: 
#       Function complete
#################################################### 
# def EDIT_RECORD():
#     while 1:
#         #get inputs
#         valid = False
#         while valid == False:
#             valid = True
#             raw_input=input("Please enter the Index of the entry to edit ('end' to exit to menu)\n")
#             if raw_input.lower()=="end":
#                 print("Exiting to menu")
#                 return #exit function
#             for x in raw_input:
#                 if not(ord(x) in range(48,58)):
#                     valid = False
#                     print("Invalid input format. Please try again")
#                     break
#             index = int(raw_input)
#             if index >= len(Diary):
#                 valid = False
#                 print("Invalid input. Index excieds Diary size")
        
#         #input valid
#         old_entry = Diary.pop(index)#pull out the entry to edit
#         print("What would you like to edit?")
#         print("""
#         1. Priority
#         2. Time
#         3. Discription
#         4. All
#         """)
#         raw_input=input("\n")
#         if raw_input == '1':
#             print("Editing Priority")
#             #get the new value
#             priority = GET_PRIORITY()
#             #update the poped entry with new data
#             old_entry = priority +';'+ old_entry[DATE_START:]
#             #re-insert into diary
#             Diary.insert(index, old_entry)
#             PRINT_DIARY()
#         elif raw_input == "2":
#             print("Editing Time")
#             while 1:#check concurrentsy
#                 while 1:#get time and validate
#                     while 1:#get new date and validate
#                         date = GET_DATE()
#                         if date == False:
#                             return False
#                         if VALIDATE_DATE(date) == True:
#                             break
                
#                     startTime = GET_START_TIME()
#                     endTime = GET_END_TIME()
#                     if VALIDATE_TIME(startTime,endTime,date) == True: 
#                         break
#                 if IS_CONCURRENT_APPOINTMENT(startTime,endTime,date) == False:
#                     break
#             #broke out of loops - inputs are valid
#             strStartTime = str(startTime)
#             if len(strStartTime) < 2:
#                 strStartTime = '0' + strStartTime
#             strEndTime = str(endTime)
#             if len(strEndTime) < 2:
#                 strEndTime = '0' + strEndTime
#             #update the poped entry with new data
#             old_entry = old_entry[:DATE_START]+date+';'+strStartTime+';'+strEndTime+';'+old_entry[DISCRIPTION_START:]
#             #re-insert into diary
#             Diary.insert(index, old_entry)
#             PRINT_DIARY()
#         elif raw_input == "3":
#             #get the new value
#             print("\n Editing Discription")
#             discription = GET_DESCRIPTOR()
#             #update the poped entry with new data
#             old_entry = old_entry[:DISCRIPTION_START]+discription
#             #re-insert into diary
#             Diary.insert(index, old_entry)
#             PRINT_DIARY()
#         elif raw_input == "4":
#             #everything is being replaced - delete entry and add a new one
#             print("\n Editing All")
#             if ADD_RECORD(False) == False:#if addition is aborted early re-insert old data
#                 print("Edit aborted!")
#                 Diary.insert(index, old_entry)
#         else:
#             print("\n I\'m sorry that response is not recognised please try again")

####################################################
# REMOVE_RECORDS()
# ##########	
# inputs:
#   None
# outputs:
# 	None
# ##########
#   removes records. selection by user prompts.
#   can 'clean' records. (i.e. deletes records that are in the past) 
# ##########    
# Author: Timothy van den Bosch
# Date: 11/05/2022
# History
# 	Rev1, 07/05/2022, Timothy van den Bosch: 
#       Function complete
#################################################### 
# def REMOVE_RECORDS():
#     while 1:
#         valid = False
#         while valid == False:
#             valid = True
#             raw_input=input("Please enter the Index of the entry to delete \n\t'clean' to remove dates that have past\n\t'end' to exit to menu\n")
#             if raw_input.lower()=="end":
#                 print("Exiting to menu")
#                 return
#             elif raw_input.lower()=="clean":
#                 break
#             else:
#                 for x in raw_input:
#                     if not(ord(x) in range(48,58)):
#                         valid = False
#                         print("Invalid input format. Please try again")
#                         break
#                 if valid ==True:
#                     index = int(raw_input)
#                     if index >= len(Diary):
#                         valid = False
#                         print("Invalid input. Index excieds Diary size")
#         #input valid
#         if raw_input.lower()=="clean":
#             for index in range(0, len(Diary)-1):
#                 date = Diary[index][DATE_START:DATE_END]
#                 start = int(Diary[index][STARTTIME_START:STARTTIME_END])
#                 DDay = int(date[DAY_START:DAY_END])-time.localtime().tm_mday
#                 DMonth = int(date[MONTH_START:MONTH_END])-time.localtime().tm_mon
#                 DYear = int(date[YEAR_START:YEAR_END])-time.localtime().tm_year
#                 DStart = start-time.localtime().tm_hour
#                 past = True
#                 if DYear > 0:
#                     past = False
#                 if DYear==0: 
#                     if DMonth>0:
#                         past = False
#                     if DMonth==0:
#                         if DDay>0:
#                             past = False
#                         if DDay==0:
#                             if DStart > 0:
#                                 past = False
#                 if past == True:
#                     Diary.pop(index)
#         else:
#             print("Delete entry?")
#             print("Index    Priority   Date         Start   End   Description")
#             print("-----    --------   ----------   -----   ---   --------------------------------")
#             strIndex = str(index)
#             while len(strIndex)<5:
#                 strIndex=strIndex+" "
#             print(strIndex+"    "+Diary[index][PRIORITY_START:PRIORITY_END]+"       "+ Diary[index][DATE_START:DATE_END] +"   " + Diary[index][STARTTIME_START:STARTTIME_END], "     " + Diary[index][ENDTIME_START:ENDTIME_END] + "    " +Diary[index][DISCRIPTION_START:DISCRIPTION_END])
#             raw_input=input("Y/N?\n")
#             if raw_input.lower() == "yes" or raw_input.lower() == "y" :
#                 Diary.pop(index)
#                 print("Entry deleted")
#             else:
#                 print("Delete aborted")
#         PRINT_DIARY()
    
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
# 	Rev1, 02/05/2022, Anthony Mann: 
#       Function complete
####################################################
while 1:
    PRINT_DIARY()
    print("""
    1. Add Record
    2. Edit Records
    3. Remove Records
    4. Sort Records
    5. Exit
    """)
    
    Menu_Response_rawInput=input("Dear Diary, I would like to: \n")
    if Menu_Response_rawInput == "1":
        print("\n Adding A Record")
        ADD_RECORD(True)
    elif Menu_Response_rawInput == "2":
        print("\n Editing Your Records")
        print("Feature temporarily disabled")
        #EDIT_RECORD()
    elif Menu_Response_rawInput == "3":
        print("\n Delete Rocords")
        print("Feature temporarily disabled")
       # REMOVE_RECORDS()
    elif Menu_Response_rawInput == "4":
        print("\n Sorting Your Records")
        SORT_RECORD()
    elif Menu_Response_rawInput == "5":
        print("\n Thanks for using Dear Diary, see you next time \n")
        break
    else:
        print("\n I\'m sorry that response is not recognised please try again")
        

