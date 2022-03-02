import mysql.connector
import GuiDBConfig as guiConf

GUIDB='GuiDB'

conn=mysql.connector.connect(**guiConf.dbConfig)
cursor=conn.cursor()


cursor.execute("SHOW TABLES FROM guidb")
print(cursor.fetchall())


conn.close()