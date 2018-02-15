#!/usr/bin/env python

import pymssql

dbuser = 'sa'
dbpasswd = 'Password12!'
dbhost = 'localhost\\SQL2014'
dbname = 'sqlobject_test'

def test_pymssql():
    conn = pymssql.connect(dbhost, dbuser, dbpasswd, dbname)
    conn.autocommit(True)

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE test (
            id INT IDENTITY UNIQUE NOT NULL,
            test VARCHAR(255) NOT NULL UNIQUE,
            PRIMARY KEY(id)
        )
    """)
    cursor.execute("INSERT INTO test (test) VALUES ('test1')")

    conn.autocommit(False)

    cursor2 = conn.cursor()
    cursor2.execute("INSERT INTO test (test) VALUES ('test2')")

    HAS_IDENTITY = """
       select 1
       from INFORMATION_SCHEMA.COLUMNS
       where TABLE_NAME = '%s'
       and COLUMNPROPERTY(object_id(TABLE_NAME), COLUMN_NAME, 'IsIdentity') = 1
    """

    query = HAS_IDENTITY % 'test'
    c = conn.cursor()
    c.execute(query)
    print(c.fetchone())

    conn.commit()
    conn.close()

test_pymssql()
