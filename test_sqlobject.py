#! /usr/bin/env python

from sqlobject import SQLObject, StringCol
from sqlobject.tests import dbtest
from sqlobject.tests.dbtest import setupClass


class PytestOption(object):
    Database = "mssql://sa:Password12!@localhost\SQL2014/sqlobject_test?driver=pymssql&timeout=30&debug=1"
    show_sql = True
    show_sql_output = True

dbtest.conftest.option = PytestOption()


class SOTestSOTrans(SQLObject):
    class sqlmeta:
        defaultOrder = 'name'
    name = StringCol(length=10, alternateID=True, dbName='name_col')


def test_sqlo():
    setupClass(SOTestSOTrans)
    connection = SOTestSOTrans._connection
    trans = connection.transaction()
    SOTestSOTrans(name='bob')

test_sqlo()
