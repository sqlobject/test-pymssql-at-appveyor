#!/usr/bin/env python

dbuser = 'sa'
dbpasswd = 'Password12!'
dbhost = 'localhost\\SQL2014'
dbname = 'sqlobject_test'

import pymssql
conn = pymssql.connect(dbhost, dbuser, dbpasswd, dbname)
conn.close()
