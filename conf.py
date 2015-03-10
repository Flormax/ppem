#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import sys, os
import session
import MySQLdb
import cgi
import cgitb
cgitb.enable()

sys.path.append(os.environ['DOCUMENT_ROOT'])
sess = session.Session(expires=365*24*60*60, cookie_path='/')
db = MySQLdb.connect("localhost", "toto", "", "utilisateurs")

form = cgi.FieldStorage()
action = form.getvalue('action')

if action in locals(): #Si la variable action est présente (non vide)
    action()

def action():
    if action == 'connexion':
        connexion()
    if action == 'deconnexion':
        deconnexion()

def deconnexion():
    sess.data['connecte'] = False
    sess.data['admin'] = ''
    print('Location:connexion.py')
        
def connexion():
    email = form.getvalue('email')
    mdp = form.getvalue('mdp')
    
    if (email == None or mdp == None):
        print('Location:connexion.py')
    else:
        sql = "SELECT admin FROM utilisateur WHERE email = '" + email + "' AND mdp = '" + mdp + "';"
        
        cursor = db.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is not None:
            sess.data['connecte'] = True
            sess.data['admin'] = row[0]
            redirect()
                
def redirect():
    connecte = sess.data.get('connecte')
    admin = sess.data.get('admin')
    
    if connecte and admin:
        print('Location:admin.py')
    elif connecte:
        print('Location:utilisateur.py')
    else:
        print('Location:connexion.py')
        
db.close()
sess.close()
