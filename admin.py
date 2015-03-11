#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import html, conf, bdd
import cgi
import cgitb
cgitb.enable()

def editUtilisateur():
    if action == 'modifier':
        uid = form.getvalue('id')
        selectUtilisateur(uid)
        row = cursor.fetchone()
        nom = row[1]
        prenom = row[2]
        email = row[3]
        nextAction = 'enregistrerModification'
        h2 = '<h2>Modifier un utilisateur</h2>'
    else:
    	h2 = '<h2>Ajouter un utilisateur</h2>'
        nom = ''
        prenom = ''
        email = ''
        nextAction = 'ajouter'
    htmlForm = '<form action="conf.py" method="post">' \
        + '<label for="nom">Nom</label><input type="text" name="nom" id="nom" placeholder="Nom" value="' + str(nom) + '"/ required><span class="erreur"></span><br>' \
        + '<label for="prenom">Prénom</label><input type="text" name="prenom" id="prenom" placeholder="Prénom" value="' + str(prenom) + '"/ required><span class="erreur"></span><br>' \
        + '<label for="email">Email</label><input type="email" name="email" id="email" placeholder="Email" value="' + str(email) + '"/ required><span class="erreur"></span><br>' \
        + '<input type="hidden" name="action" value="' + nextAction + '"/>'
    if nextAction == 'enregistrerModification':
        htmlForm += '<input type="hidden" name="id" value="' + uid + '"/>' \
        + '<input type="submit" value="Enregistrer la modification" /><br>' \
        + '<a href="admin.py" title="Ajouter un utilisateur">Ajouter un utilisateur</a>'       
    else:
        htmlForm += '<input type="submit" value="Ajouter" />'
    htmlForm += '</form>'
    print '<h1>Gestion des utilisateurs</h1>'
    print '<div>'
    print (h2)
    print (htmlForm)
    print '</div>'
         
def modifUtilisateur():
    if action == 'ajouter' or action == "enregistrerModification":
        nom = form.getvalue('nom')
        prenom = form.getvalue('prenom')
        email = form.getvalue('email')
        if (nom == None or prenom == None or email == None):
            return
        if action == 'ajouter' :
            bdd.insertUtilisateur(nom, prenom, email)
        else:
            uid = form.getvalue('id')
            bdd.updateUtilisateur(nom, prenom, email, uid)
    
conf.redirect()
form = cgi.FieldStorage()
action = form.getvalue('action')
html.printHeader()
html.printUtilisateurs()
html.printUtilisateur(row)
editUtilisateur()
deleteUtilisateur()
insertUtilisateur()
html.printFooter()

