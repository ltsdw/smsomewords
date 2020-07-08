#! /hint/python

from os import system, path, environ

def createWriteFile(item):
    f = open(environ['DESKTOP_DIR'] + '/estudos/japonês/リスト.txt', 'a+')
    f.write(item + '\n')
    f.close()

def writeFile(item):
    f = open(environ['DESKTOP_DIR'] + '/estudos/japonês/リスト.txt', 'a')
    f.write(item + '\n')
    f.close()

def checksames(item):
    try:
        with open(environ['DESKTOP_DIR'] + '/estudos/japonês/リスト.txt') as f:
            if item not in f.read() and item != "":
                return True
            else:
                return False
    except:
        createWriteFile(item)

def appendItemQuit(lista = [""]):
    try:
        if path.getsize(environ['DESKTOP_DIR'] + '/estudos/japonês/リスト.txt'):
            for item in lista:
                if checksames(item):
                    writeFile(str(item))
        else:
            for item in lista:
                if checksames(item):
                    createWriteFile(str(item))
    except:
        for item in lista:
            if checksames(item):
                createWriteFile(str(item))
   
    quit()

