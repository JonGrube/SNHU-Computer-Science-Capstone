"""
FrienDB Phonebook
by Jonathan Grube
01/25/2022

"""

import pyodbc
from Test import *

# add new entry to database
def db_insert_new(entry) :
    
    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
    
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Friend(ID_number, first_name, last_name, phone, address, city, state, zip_code) VALUES(?, ?, ?, ?, ?, ?, ?, ?);",
                   (entry.get_ID(), entry.get_first_name(), entry.get_last_name(), entry.get_phone(), entry.get_address(), entry.get_city(), entry.get_state(), entry.get_zip())
                   )
    connect.commit()    
    db_display_all()

# display all entries from database
def db_display_all() :
    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
    
    cursor = connect.cursor()
    cursor.execute("SELECT * from Friend")
    
    for row in cursor:
        print(f"~ {row}")

# finds the highest ID_number for the new entry object
def db_next_id() :
    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
    
    cursor = connect.cursor()
    cursor.execute("SELECT ID_number from Friend WHERE ID_number = (SELECT MAX(ID_number) FROM Friend)")
    
    for row in cursor:
        
        if(len(row) == 1) :
            nextNumber = (row[0] + 1)
            return(nextNumber)
        
        elif(len(row) == 2) :
            nextNumber = ((row[0] * 10) + row[1] + 1)
            return(nextNumber)
        
        elif(len(row) == 3) :
            nextNumber = ((row[0] * 100) + (row[1] * 10) + row[2] + 1)
            return(nextNumber)

# update an existing entry     
def db_update_entry(entryUp) :
    while 1 :
        
        # choose which field to edit
        print("1. First Name\n2. Last Name\n3. Phone Number\n4. Street Address\n5. City\n6. State\n7. Zip Code\nQ to Quit\n")
        editSel = input("Selct Field to Change: ")
        idInt = int(entryUp)
        
        if(editSel == "1") :
            
            while(1) :
                newName = input("New First Name: ")
                if(check_string_in(newName) == newName) :
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET first_name = ? WHERE ID_number = ?;",
                                   (newName, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a string!")
            break
        
        elif(editSel == "2") :
            while(1) :
                newName = input("New Last Name: ")
                if(check_string_in(newName) == newName) :
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET last_name = ? WHERE ID_number = ?;",
                                   (newName, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a string!")
            break
        
        elif(editSel == "3") :
            
            while(1) :
                newPhoneIn = input("New Phone (10 Digit ##########): ")
                if((check_int_in(newPhoneIn) == newPhoneIn) and (check_phone_len(newPhoneIn) == newPhoneIn)) :
                    newPhone = int(newPhoneIn)
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET phone = ? WHERE ID_number = ?;",
                                   (newPhone, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a 10-Digit Phone Number!")
            break
        elif(editSel == "4") :
            while(1) :
                newAddr = input("New Address: ")
                if(check_string_in(newAddr) == newAddr) :
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET address = ? WHERE ID_number = ?;",
                                   (newAddr, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a string!")
            break
        
        elif(editSel == "5") :
            
            while(1) :
                newCity = input("New City: ")
                if(check_string_in(newCity) == newCity) :
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET city = ? WHERE ID_number = ?;",
                                   (newCity, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a string!")
            break
            
        elif(editSel == "6") :
            
            while(1) :
                
                newState = input("New State (2 Letter Abbreviation): ")
                if((check_string_in(newState) == newState) and (check_state_len(newState) == newState)) :
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET state = ? WHERE ID_number = ?;",
                                   (newState, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a 2-Letter State abbreviation!")
            break
            
        elif(editSel == "7") :
            
            while(1) :
                newZipIn = input("New Zip Code (5 Digit #####): ")
                if((check_int_in(newZipIn) == newZipIn) and (check_zip_len(newZipIn) == newZipIn)) :
                    newZip = int(newZipIn)
                    #send to db
                    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
                    
                    cursor = connect.cursor()
                    cursor.execute("UPDATE Friend SET zip_code = ? WHERE ID_number = ?;",
                                   (newZip, idInt)
                                   )
                    connect.commit()
                    db_display_entry_id(entryUp)
                    
                    break
                else :
                    print("This data must be a 5-Digit Zip Code (#####)!")
            break
            
        elif(editSel == "q" or editSel == "Q") :
            break
        
        else :
            print("Make a Selection 1-7 or Q")

# displays entry of input's ID_number
def db_display_entry_id(input) :
    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
    
    cursor = connect.cursor()
    cursor.execute("SELECT * from Friend WHERE ID_number = " + input)
    
    for row in cursor:
        print(f"~ {row}")

# search entry by name    
def db_search_name(strSearch) :
    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
    
    cursor = connect.cursor()
    inString = str(strSearch)
    cursor.execute("SELECT * from Friend WHERE first_name LIKE %?%", (inString))
    
    for row in cursor:
        print(f"~ {row}")

# delete entry by ID_number        
def db_delete_entry(idSup) :
    connect = pyodbc.connect("Driver={SQL Server}; Server=LAPTOP-16FU2QAS; Database=FrienDB; Trusted_ConnectioSn=yes;")
    
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Friend WHERE ID_number = " + idSup)

    connect.commit()    
    db_display_all()