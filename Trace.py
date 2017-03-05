#!/usr/bin/env python

__author__ = 'Sphinxs'


import sqlite3

import sys

import os


connect = sqlite3.connect('Db.db')

cursors = connect.cursor()


def clean():

    os.system('clear')

clean()


def table():

    cursors.execute('create table if not exists Dados (id integer, title text, content text)')

table()


def inser(id, title, content):

    cursors.execute("insert into Dados (id, title, content) values(?,?,?)", (id, title, content))

    connect.commit()


while True:

    try:

        id = int(input("\nInforme o id: "))

    except:

        sys.exit(1)

    title = input("\nInforme o nome: ")

    content = input("\nInforme o texto: ")

    inser(id, title, content)

    try:

        valor = input("\n1 - Reiniciar\n\n0 - Sair\n\nEscolha : ")

        clean()

        if valor == '1':

            continue

        else:

            break

    except:

        sys.exit(1)
