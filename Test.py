"""
FrienDB Phonebook
by Jonathan Grube
01/25/2022

"""
from Queries import *
from Entry import *

# verify input is string, and falls within the length constraints of the DB
def check_string_in(input) :
    
    # if input cannot be converted to an integer or a float then it must be a
    # string. it is valid input for data columns: firstName, lastName, address, 
    #city, and state in DB
    
    try:
        val = int(input)
        print("You entered a number. This data should be a string!")
        return
    except ValueError:
        
        try:
            val = float(input)
            print("You entered a number. This data should be a string!")
            return
        
        except ValueError:
            
            if ((len(input) > 1) and (len(input) < 51)) :
                print("You Entered: ", input)
                return(input)
            else :
                print("This data sshould fall between 2 and 50 characters long!")
                return

# verifies input is an integer
def check_int_in(input) :
    
    try:
        val = int(input)
        return(input)
    except ValueError:
        print("This data should be an integer!")
        return

# checks that the length of state is 2 for abbreviation
def check_state_len(input) :
    if (len(input) == 2) :
        print("You Entered: ", input)
        return(input)
    else :
        print("This data should be a 2 character State abbreviation!")
        return

# checks that the length of phone is 10 for (123)456-7890  
def check_phone_len(input) :
    if (len(input) == 10) :
        print("You Entered: ", input)
        return(input)
    else :
        print("This data should be a 10 digit integer with no spaces!")
        return

# checks that zip code is 5 digits for 12345
def check_zip_len(input) :
    if (len(input) == 5) :
        print("You Entered: ", input)
        return(input)
    else :
        print("This data should be a 5 digit integer!")
        return
    
# tests entry creation, read, and deletion
def test_runner() :
    print("Testing... \n")
    testEntry = Entry("999", "Test Name", "Test Surname", "1235551234", "est St", "Teston", "NY", "12345")
    db_insert_new(testEntry)
    print("Testing display... \n")
    db_display_entry_id("999")
    print("Testing deletion... \n")
    db_delete_entry("999")
    print("Test Completed!\n")
    
    