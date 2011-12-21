from django.db import connection

class User(object):
    def __init__(self, id = 0, fName="", lName="", username="", email=""):
        self.id = id
        self.firstName = fName
        self.lastName = lName
        self.username = username
        self.email = email
    
''' Class for accessing the DB. '''
class dbAccess(object):
    
    ''' Runs base query and returns list of models for records in db. '''
    @staticmethod
    def getUsers():
        query = '''
            select id, firstName, lastName, username, email from Users
            '''
        
        cursor = connection.cursor()
        cursor.execute(query)
        
        userList = list()
        row = cursor.fetchone()
        while(row != None):
            
            id = row[0]
            fName = row[1]
            lName = row[2]
            uName = row[3]
            email = row[4]
            
            user = User(id, fName, lName, uName, email)
            userList.append(user)
            
            row = cursor.fetchone()
        
        return userList
    
    @staticmethod
    def getUsersForChoiceField():
        query = '''
            select id, firstName, lastName from Users
            '''
        
        cursor = connection.cursor()
        cursor.execute(query)
        
        userTupleList = list()
        row = cursor.fetchone()
        while(row != None):
            
            id = row[0]
            fName = row[1]
            lName = row[2]
            
            name = ' '.join((fName, lName))
            userTupleList.append((id, name))            
            
            row = cursor.fetchone()
            
        return userTupleList    
            
            
            
            
            
            
            
            
            
            
            
            