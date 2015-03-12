#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import random
import string
import hashlib

def genereMdp(): #génère mdp aléatoire
    char_list = string.ascii_letters + string.digits 
    password = ""
    for i in range(10):
        index = random.randint( 0, len( char_list ) - 1 )
        password += char_list[ index ]
    return password

def hachage(mdp): #hashage mdp
    hash_object = hashlib.md5(mdp.encode())
    hash_object = hash_object.hexdigest()
    return hash_object