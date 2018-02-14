#! /usr/bin/env python

from sqlobject import SQLObject, StringCol

__connection__ = "mssql://sa:Password12!@localhost\SQL2014/sqlobject_test?driver=pymssql&timeout=30&debug=1"

class Test(SQLObject):
    test = StringCol()

Test.createTable()

conn = Test._connection
txn = conn.transaction()
txn.commit()

Test(test='test1', connection=txn)
txn.rollback()
print(list(Test.select()))

Test(test='test1', connection=txn)
txn.commit()
print(list(Test.select()))

conn.close()
