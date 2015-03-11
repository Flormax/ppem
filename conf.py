#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import html, mail, bdd, admin, sys, os
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

def actionTraitement():
    if action == 'connexion':
        connexion()
    elif action == 'deconnexion':
        deconnexion()
    elif action == 'inscription':
        mail.sendMail(action)
    elif action == 'envoieMdp':
        mail.sendMail(action)
    elif action == 'modifMdp':
        bdd.modifMdp(sess.data['id'], form.getvalue('mdpApr'))
    elif action == 'modifEmail':
        bdd.modifEmail(sess.data['id'], form.getvalue('emailApr'))
    elif action == 'enregistrerModification':
        admin.modifUtilisateur()
    elif action == 'ajouter':
        admin.modifUtilisateur()
    elif action == 'supprimer':
        bdd.deleteUtilisateur(form.getvalue('id'))

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
        sql = "SELECT admin, id FROM utilisateur WHERE email = '" + email + "' AND mdp = '" + mdp + "';"
        
        cursor = db.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        if row is not None:
            sess.data['connecte'] = True
            sess.data['admin'] = row[0]
            sess.data['id'] = rox[1]
            redirect()
        else:
            print('Location:connexion.py')     
                
def redirect():
    connecte = sess.data.get('connecte')
    admin = sess.data.get('admin')
    
    if connecte and admin:
        print('Location:admin.py')
    elif connecte:
        print('Location:utilisateur.py')
    else:
        print('Location:connexion.py')

if action is not None:
    actionTraitement()
 
html.printHead()
   
db.close()
sess.close()