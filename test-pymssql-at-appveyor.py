#!/usr/bin/env python

dbuser = 'sa'
dbpasswd = 'Password12!'
dbhost = 'localhost\\SQL2014'
dbname = 'sqlobject_test'

import pymssql
conn = pymssql.connect(dbhost, dbuser, dbpasswd, dbname)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE test (
        id INT NOT NULL,
        test VARCHAR(255) NOT NULL,
        PRIMARY KEY(id)
    )
""")
cursor.execute("INSERT INTO test (id, test) VALUES (1, 'test1')")

conn.commit()
conn.close()
