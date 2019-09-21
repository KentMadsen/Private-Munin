#!/bin/python

import mysql.connector
import os

mydb = mysql.connector.connect(
   # host="",
  #  user="",
 #   passwd="",
#    database=""
)

search = "D:\\DataSets\\usenetcorpus\\"

files = []


#def getContent(file):
#    f = open(file, "r",  encoding="utf-8", errors="ignore")
#
#    contents = f.read()

#    f.close()

#    return contents


#for r, d, f in os.walk(search):
 #   for file in f:
  #      full = os.path.join(r, file)
   #     parent = os.path.abspath(os.path.join(full, os.pardir))

    #    sql = "INSERT INTO dailymail_stories(directory, name, content) values(%s, %s, %s)"
     #   value = (parent, file, getContent(full))

      #  cursor = mydb.cursor()
       # cursor.execute(sql, value)

        #mydb.commit()


# sql = "INSERT INTO usenet_corpus(name, content) values( %s, %s )"

# cursor = mydb.cursor()
# cursor.execute(sql, value)

# mydb.commit()

def getContent(file):
    f = open(file, "r",  encoding="utf-8", errors="ignore")

    # Reads the first line
    line = f.readline()

    buffer = None

    current_pos = 0
    records = []

    while line:

        if buffer is None:
            buffer = line
        else:
            buffer = buffer + line

        if "---END.OF.DOCUMENT---" in line:
            value = (file, buffer)

            records.append(value)

            buffer = None

            current_pos = current_pos + 1

            if (current_pos % 10000) == 0:
                print(current_pos)

            if current_pos < 32880000:
                records = []

            if len(records) > 10000 and current_pos > 32880000:
                sql = """INSERT INTO usenet_corpus(name, content) values( %s, %s )"""

                cursor = mydb.cursor()
                cursor.executemany(sql, records)

                mydb.commit()

                records = []

        line = f.readline()

    if len(records) != 0:
        sql = """INSERT INTO usenet_corpus(name, content) values( %s, %s )"""

        cursor = mydb.cursor()
        cursor.executemany(sql, records)

        mydb.commit()


    f.close()



for r, d, f in os.walk(search):
    for file in f:
        full = os.path.join(r, file)
        parent = os.path.abspath(os.path.join(full, os.pardir))

        getContent(full)

        #sql = "INSERT INTO dailymail_stories(directory, name, content) values(%s, %s, %s)"
        #value = (parent, file, getContent(full))

        #cursor = mydb.cursor()
        #cursor.execute(sql, value)

        #mydb.commit()