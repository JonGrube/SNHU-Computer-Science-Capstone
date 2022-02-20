"""
FrienDB Phonebook
by Jonathan Grube
01/25/2022

"""

class Entry:
    
    # Entry class to store and verify data before sending to DB
    # FIXME add automatic idNum from DB
    
    def __init__(self, idNum, nameFirst, nameLast, phoneNum, address, city, state, zipCode):
        self.idNum = idNum
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.phoneNum = phoneNum
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        
    #getters
    #def get_id(self) :
        #FIXME return ID # from DB
        
    def get_ID(self) :
        return(self.idNum)
        
    def get_first_name(self) :
        return(self.nameFirst)
    
    def get_last_name(self) :
        return(self.nameLast)
    
    def get_phone(self) :
        return(self.phoneNum)
    
    def get_address(self) :
        return(self.address)
    
    def get_city(self) :
        return(self.city)
    
    def get_state(self) :
        return(self.state)
    
    def get_zip(self) :
        return(self.zipCode)
    
    #setters
    def set_first_name(self, x) :
        self.nameFirst = x
    
    def set_last_name(self, x) :
        self.nameLast = x
    
    def set_phone(self, x) :
        self.phoneNum = x
    
    def set_address(self, x) :
        self.address = x
    
    def set_city(self, x) :
        self.city = x
    
    def set_state(self, x) :
        self.state = x
    
    def set_zip(self, x) :
        self.zipCode = x
        