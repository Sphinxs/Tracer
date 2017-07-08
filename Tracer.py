
# -*- coding: utf-8 -*-

import sqlite3 as lite


class Db :

    ''' Crud - Create, Read, Update & Delete '''

    def __init__ ( self, name = 'Default.db' ) :

        self.__name = name

        self.__con = lite.connect ( str ( self.__name ) )

        self.__cur = self.__con.cursor ()


    def table ( self, * args ) :

        ''' * Args = 'Table-Name', ( 'Field1 text, Field2 integer, Field3 real ... ' ) '''

        try :

            self.__cur.execute ( '''create table if not exists {0} ({1})'''.format ( args[0], args[1] ) )

            self.__con.commit ()

        except lite.Error as Ert :

            raise Exception ( Ert + '\t - Check the parameters' )

        else :

            print ( '{0} Was created'.format ( args[0] ) )


    def insert ( self, * args ) :

        ''' * Args = 'Table-Name', ( 'Field1', 'Field2', 'Field3' ), ( 'Value-01', 02, 0.3 ) '''

        try :

            self.__cur.execute ( '''insert into {0} {1} values {2}'''.format ( args[0], args[1], args[2] ) )

            self.__con.commit ()

        except lite.Error as Eri :

            raise Exception ( Eri + '\t - Check the parameters' )

        else :

            print ( 'Was adds in - {0}'.format ( args[0] ) )


    def show ( self, tbl = None ) :

        ''' Tbl = 'Table-Name' '''

        try :

            for row in self.__cur.execute ( '''select * from {0}'''.format ( str ( tbl ) ) ) :

                print ( '\n' )

                print ( ' '.join ( '{} '.format ( c ) for i, c in enumerate ( row, 1 ) ) )

            else :
                
                print ( '\n' )

        except lite.Error as Ers :

            raise Exception ( Ers + '\t - Check the parameter' )

    def select ( self, tbl = None, cmp = None, fld = None ) :

        ''' Tbl = 'Table-Name', Cmp = Field, Fld = Value '''

        try :

            self.__query = self.__cur.execute ( '''select * from {0} where {1} = \'{2}\''''.format ( str ( tbl ), str ( cmp ), str ( fld ) ) )

            print ( ' '.join ( '{} '.format( c ) for i, c in enumerate ( self.__query.fetchone () ) ) )

        except lite.Error as Erq :

            raise Exception ( Erq + '\t - Check the parameters' )
