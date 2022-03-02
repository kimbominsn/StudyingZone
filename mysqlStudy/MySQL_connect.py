import mysql.connector
import GuiDBConfig as guiConf

# conn=mysql.connector.connect(user='root', password='1234', host='127.0.0.1')
conn=mysql.connector.connect(**guiConf.dbConfig)

print(conn)
conn.close()