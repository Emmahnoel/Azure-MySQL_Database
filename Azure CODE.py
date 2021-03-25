#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'emmah.mysql.database.azure.com',
  'user':'emmah@emmah',
  'password':'Oziomahnoel1999',
  'database':'lfp2018'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Read data
  cursor.execute("SELECT * FROM lfp2018;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  for row in rows:
  	print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")


# In[4]:


import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'emmah.mysql.database.azure.com',
  'user':'emmah@emmah',
  'password':'Oziomahnoel1999',
  'database':'lfp2018'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Update a data row in the table
  cursor.execute("UPDATE lfp2018 SET State = %s WHERE id = %s;", (13, "EKITI"))
  print("Updated",cursor.rowcount,"row(s) of data.")

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")
    


# In[5]:


import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'emmah.mysql.database.azure.com',
  'user':'emmah@emmah',
  'password':'Oziomahnoel1999',
  'database':'lfp2018'
}

 #Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Read data
  cursor.execute("SELECT * FROM LFP2018 WHERE State = 'EKITI';")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  for row in rows:
  	print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")


# In[ ]:




