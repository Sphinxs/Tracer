
# -*- coding: utf-8 -*-

import sqlite3 as sl


class Db ( object ) :

    ''' Crud - Create, Read, Update & Delete '''

    def __init__ ( self, name = 'Default.db' ) :

        self.name = name

        self.con = sl.connect ( str ( self.name ) )

        self.cur = self.con.cursor ()

    def table ( self, * args ) :

        ''' Args = 'Itens', ( 'Field1 text, Field2 integer' ) '''

        try :

            self.cur.execute ( '''create table if not exists {0} ({1})'''.format ( args[0], args[1] ) )

            self.con.commit ()

        except sqlite3.Error as Er :

            raise ( 'Nenhuma tabela foi criada ou os parâmetros contém erros - {0}'.foramt ( Er ) )

    def insert ( self, * args ) :

        ''' Args = 'Name-Table', ( 'Field1', 'Field2' ), ( 'Value-Field1', 02 ) '''

        self.cur.execute ( '''insert into {0} {1} values {2}'''.format ( args[0], args[1], args[2] ) )

        self.con.commit ()

    def show ( self, tbl = None ) :

        ''' Tbl = 'Example' '''

        self.cur.execute ( '''select * from {0}'''.format ( tbl ) )

        for row in self.cur.execute ( '''select * from {0}'''.format ( tbl ) ) :

            print ( '{0}'.format ( row.join ( ' - ' ) )
