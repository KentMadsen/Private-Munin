#!/bin/python

import mysql.connector
import os

mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

search = "/home/madsen/Logs"

files = []


def getContent(file):
    f = open(file, "r")

    contents = f.read()
    print(contents)

    f.close()

    return contents


for r, d, f in os.walk(search):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    print(f)

    sql = "INSERT INTO raw_files(parent, title, content) values(%s, %s, %s)"
    value = ( os.path.abspath(os.path.join(f, os.pardir)), f, getContent(f))

    cursor = mydb.cursor()
    cursor.execute(sql, value)

    mydb.commit()