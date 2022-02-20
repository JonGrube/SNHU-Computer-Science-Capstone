"""
FrienDB Phonebook
by Jonathan Grube
01/25/2022

"""

import pyodbc
from sys import exit
from Test import *
from Entry import *
from Queries import *

# main loop

while 1:
    
    #main menu
    print("MAIN MENU\n \n1. New Entry \n2. Display Entries \n3. Edit Entry ")
    print("4. Search by Name \n5. Delete Entry \nQ. Quit")
    menuOpt = input("Select by Number ")

    # handle user input for main menu
    # NEW ENTRY
    if menuOpt == "1":
        print("New Entry\n")
        
        newEntry = Entry(db_next_id(), "New", "Entry", 1235551234, "New St", "New York", "NY", 12345)
        #collect entry data
        #user supplies data for new entry
        #loop until valid input is taken
        while 1:
            
            while 1:
                nameOne = input("Enter First Name: ")
                # verify string and length using Test.py, which will return nameOne (input)
                if (check_string_in(nameOne) == nameOne) :
                    newEntry.nameFirst = nameOne
                    break
            
            while 1:
                nameTwo = input("Enter Last Name: ")
                if (check_string_in(nameTwo) == nameTwo) :
                    newEntry.nameLast = nameTwo
                    break
            
            while 1:
                phoneNumber = input("Enter Phone Number (##########): ")
                if (check_int_in(phoneNumber) == phoneNumber) :
                    if (check_phone_len(phoneNumber) == phoneNumber) :
                        newEntry.phoneNum = phoneNumber
                        break

            while 1:
                address = input("Enter Street Address: ")
                if (check_string_in(address) == address) :
                    newEntry.address = address
                    break
                
            while 1:
                city = input("Enter City Name: ")
                if (check_string_in(city) == city) :
                    newEntry.city = city
                    break
                
            while 1:
                state = input("Enter State (Two Letter): ")
                if (check_string_in(state) == state) :
                    if (check_state_len(state) == state) :
                        newEntry.state = state
                        break
            
            while 1:
                zipcode = input("Enter Zip Code (#####)")
                if (check_int_in(zipcode) == zipcode) :
                    if (check_zip_len(zipcode) == zipcode) :
                        newEntry.zipCode = zipcode
                        break
            
            print("\nSUBMIT ENTRY: ")
            print("First Name: ", nameOne)
            print("Last Name: ", nameTwo)
            print("Phone Number: ", phoneNumber)
            print("Address: ", address)
            print("City", city)
            print("State", state)
            print("Zip Code: ", zipcode)
            
            final = input("\nConfirm New Entry\n1. CONFIRM\n2. RESTART")
            
            if (final == "1") :
                db_insert_new(newEntry)
                break
        
                
    elif menuOpt == "2":
        print("Display Entries\n")
        #display all query which can be altered to do any kind of searching
        db_display_all()
        
    elif menuOpt == "3":
        
        while 1:
            takeIn = input("Enter ID_number to Edit Entry (Q to go back): ")
            if (input == "q" or input == "Q") :
                break
            
            elif(check_int_in(takeIn) == takeIn) :
                db_display_entry_id(takeIn)
                
                #double checking to make sure nothing bad happens
                while 1 :
                    editConf = input("Would you like to Edit this Entry?\n'Y' for Yes or 'N' for No: ")
                    if (editConf == "y" or editConf == "Y") :
                        db_update_entry(takeIn)
                        
                    elif (editConf == "N" or 'n') :
                        break
                    else :
                        print("Enter Y or N (Yes or No)")
                
            else :
                print("This data must be an Entry ID_number (between 1 and 3 digits)!\n")
                break
                      
    elif menuOpt == "4":
        
        print("Search by Name\n")
        
        #while 1:
            #nameSearch = input("Enter Name to Search: ")
            #fixme add name search
        
    elif menuOpt == "5":
        print("Delete Entry\n")
        
        while 1:
            takeIn = input("Enter ID_number to Delete (Q to go back): ")
            if (input == "q" or input == "Q") :
                break
            
            elif(check_int_in(takeIn) == takeIn) :
                db_display_entry_id(takeIn)
                
                #double checking so that nothing bad happens
                while 1 :
                    editConf = input("Would you like to Delete this Entry?\n'Y' for Yes or 'N' for No: ")
                    if (editConf == "y" or editConf == "Y") :
                        db_delete_entry(takeIn)
                        break
                        
                    elif (editConf == "N" or 'n') :
                        break
                    else :
                        print("Enter Y or N (Yes or No)")
                
            else :
                print("This data must be an Entry ID_number (between 1 and 3 digits)!\n")
                break
     #upper or lowercase q will go back or terminate program   
    elif menuOpt == "q":
        print("Quit\n")
        exit()
    elif menuOpt == "Q":
        print("Quit")
        exit()
        
    #hidden automated test menu option
    elif menuOpt == "test":
        print("Running Tests...\n")
        test_runner()
        
    else :
        print("Invalid Entry! ~must be a number 1-7 or Q to Quit~")
