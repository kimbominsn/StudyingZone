import mysql.connector
import GuiDBConfig as guiConf

class MySQL():
    USERDB='UserDB'

#------------------------------------------------------
    def connect(self):
        # connect by unpacking dictionary credentials
        conn = mysql.connector.connect(**guiConf.dbConfig)
    
        # create cursor 
        cursor = conn.cursor()    
            
        return conn, cursor
    
    #------------------------------------------------------    
    def close(self, cursor, conn):        
        # close cursor
        cursor.close()
                
        # close connection to MySQL
        conn.close()    

    #------------------------------------------------------        
    def showDBs(self):
        # connect to MySQL
        conn, cursor = self.connect()        
        
        # print results
        cursor.execute("SHOW DATABASES")
        print(cursor)
        print(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)
                   
    #------------------------------------------------------
    def createUserDB(self):
        # connect to MySQL
        conn, cursor = self.connect()
        
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MySQL.USERDB))
        except mysql.connector.Error as err:
            print("Failed to create DB: {}".format(err))        

        # close cursor and connection
        self.close(cursor, conn) 

    #------------------------------------------------------
    def dropUserDB(self):
        # connect to MySQL
        conn, cursor = self.connect()
        try:
            cursor.execute(
                "DROP DATABASE {}".format(MySQL.USERDB))
        except mysql.connector.Error as err:
            print("Failed to drop DB: {}".format(err))        

        # close cursor and connection
        self.close(cursor, conn) 
             
    #------------------------------------------------------        
    def useUserDB(self, cursor):
        '''Expects open connection.'''
        # select DB
        cursor.execute("USE Userdb")

        #------------------------------------------------------
    def createTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
    
        self.useGuiDB(cursor)
        
        # create Table inside DB
        cursor.execute("CREATE TABLE Books (       \
              Book_ID INT NOT NULL AUTO_INCREMENT, \
              Book_Title VARCHAR(25) NOT NULL,     \
              Book_Page INT NOT NULL,              \
              PRIMARY KEY (Book_ID)                \
            ) ENGINE=InnoDB")
        
        # create second Table inside DB
        cursor.execute("CREATE TABLE Quotations ( \
                Quote_ID INT AUTO_INCREMENT,      \
                Quotation VARCHAR(250),           \
                Books_Book_ID INT,                \
                PRIMARY KEY (Quote_ID),           \
                FOREIGN KEY (Books_Book_ID)       \
                    REFERENCES Books(Book_ID)     \
                    ON DELETE CASCADE             \
            ) ENGINE=InnoDB")   
            
        # close cursor and connection
        self.close(cursor, conn) 

    #------------------------------------------------------
    def showTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
    
        # show Tables from guidb DB
        cursor.execute("SHOW TABLES FROM Userdb") 
        print(cursor.fetchall())
        
        # close cursor and connection
        self.close(cursor, conn)          


            #------------------------------------------------------        
    def insertUsers(self, salt):
        # connect to MySQL
        conn, cursor = self.connect()
        
        self.useUserDB(cursor)
        
        # insert data
        cursor.execute("INSERT INTO user_key (Salt_key) VALUES (%s)", (salt))

        UserID = cursor.lastrowid 
        # commit transaction
        conn.commit()

        # close cursor and connection
        self.close(cursor, conn)

        return UserID


        #------------------------------------------------------        
    def showUsers(self):
        # connect to MySQL
        conn, cursor = self.connect()    
        
        self.useUserDB(cursor)    
        
        # print results
        cursor.execute("SELECT * FROM user_key")
        allUsers = cursor.fetchall()
        print(allUsers)

        # close cursor and connection
        self.close(cursor, conn)   
        
        return allUsers   

     #------------------------------------------------------        
    def showColumns(self):
        # connect to MySQL
        conn, cursor = self.connect()   
        
        self.useUserDB(cursor)      
         
        # execute command
        cursor.execute("SHOW COLUMNS FROM userdb")
        print(cursor.fetchall())
        
        print('\n Pretty Print:\n--------------') 
        from pprint import pprint
        # execute command
        cursor.execute("SHOW COLUMNS FROM user_key")
        pprint(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn) 

       #------------------------------------------------------        
    def showData(self):
        # connect to MySQL
        conn, cursor = self.connect()   
        
        self.useUserDB(cursor)      
         
        # execute command
        cursor.execute("SELECT * FROM user_key")
        print(cursor.fetchall())
        
        # close cursor and connection
        self.close(cursor, conn) 

    #------------------------------------------------------        
    def findSalt(self, id):
        # connect to MySQL
        conn, cursor = self.connect()   
        
        self.useUserDB(cursor)      
         
        # execute command
        cursor.execute("SELECT Salt_key FROM user_key WHERE User_ID = (%s)",id)
        salt = cursor.fetchall()[0][0]
        # print("Primary key=" + str(primKey))

        # cursor.execute("SELECT * FROM quotations WHERE Books_Book_ID = (%s)", (primKey,))
        # print(cursor.fetchall())
        
        # close cursor and connection
        self.close(cursor, conn) 

        return salt
    