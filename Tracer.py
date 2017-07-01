
# -*- coding: utf-8 -*-

import sqlite3 as sl


class Db ( object ) :

    ''' Crud - Create, Read, Update & Delete '''

    def __init__ ( self, name = 'Default.db' ) :

        self.__name = name

        self.__con = sl.connect ( str ( self.__name ) )

        self.__cur = self.__con.cursor ()


    def table ( self, * args ) :

        ''' Args = 'Itens', ( 'Field1 text, Field2 integer' ) '''

        try :

            self.__cur.execute ( '''create table if not exists {0} ({1})'''.format ( args[0], args[1] ) )

            self.__con.commit ()

        except sl.Error as Ert :

            raise ( 'Nenhuma tabela foi criada, os parâmetros podem conter erros - {0}'.foramt ( Ert ) )

        else :

            print ( 'A tabela {0} foi criada'.format ( args[0] ) )


    def insert ( self, * args ) :

        ''' Args = 'Name-Table', ( 'Field1', 'Field2' ), ( 'Value-Field1', 02 ) '''

        try :

            self.__cur.execute ( '''insert into {0} {1} values {2}'''.format ( args[0], args[1], args[2] ) )

            self.__con.commit ()

        except sl.Error as Eri :

            raise ( 'Nenhum item foi adicionado, os parâmetros podem conter erros - {0}'.foramt ( Eri ) )

        else :

            print ( 'Informações adicionadas com sucesso' )


    def show ( self, tbl = None ) :

        ''' Tbl = 'Name-Table' '''

        try :

            for row in self.__cur.execute ( '''select * from {0}'''.format ( tbl ) ) :

                for col in row :

                    print ( '{0}'.format ( col ) ),

        except sl.Error as Ers :

            raise ( 'Nenhuma tabela foi encontrada, os parâmetros podem conter erros - {0}'.format ( Ers ) )


    def select ( self, tbl = None, cmp = None, fld = None ) :

        ''' Tbl = 'Name-Table', Cmp = Field, Fld = Value '''

        try :

            self.__query = self.__cur.execute ( '''select * from {0} where {1} = \'{2}\' '''.format ( tbl, cmp, str ( fld ) ) )

            print ( '{0}'.format ( self.__query.fetchone () ) )

        except sl.Error as Qry :

            print ( 'Erro, os parâmetros podem conter erros - {0}'.format ( Qry ) )
