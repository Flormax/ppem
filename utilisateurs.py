#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()
import MySQLdb
import sys

db = MySQLdb.connect("localhost", "toto", "", "utilisateurs")

def printHead():
    print "Content-Type: text/html"
    print
    print '''
    <!DOCTYPE html>
    <html lang="fr">

    <head>
        <meta charset="UTF-8">
        <link href="http://localhost/ppem/css/style.css" rel="stylesheet">
        <title>Gestion des utilisateurs</title>
    </head>

    <body>
    '''

def printHeader():
    print '''
    <header>
        <div class="bienvenue">
            <p>Bienvenue ...</p>
        </div><!--
     --><div class="boutons">
            <a href="utilisateurs.py?action=deconnexion" title="Déconnexion">Se déconnecter</a>
            <a href="utilisateurs.py?action=aide" title="Documentation">Aide</a>
        </div> 
    </header>
    <section>
    '''
   #Deconnexion et Bienvenue seulement si différent de page de connexion

def printFooter():
    print '''
    </section>
    <script src="http://localhost/ppem/js/controlForm.js"></script>
    </body>
    </html>
    '''

def pageConnexion():
	if action == 'nonInscrit':
		nextAction = 'Inscription'
		h2 = '<h2>S\'inscrire</h2>'
	else:
		nextAction = 'Connexion'
		h2 = '<h2>Se connecter</h2>'
	formConnexion = '<form action="utilisateur.py" method="post">' \
		+ '<input type="hidden" name="action" value="' + nextAction + '">'
	if nextAction == 'Connexion':
		formConnexion += '<input type="email" name="email" id="email" placeholder="Votre email"><span class="erreur"></span><br>' \
			+ '<input type="password" name="mdp" id="mdp" placeholder="Votre mot de passe"><span class="erreur"></span><br>' \
			+ '<input type="checkbox" name="auto" id="auto"><label for="auto">Connexion automatique</label><br>' \
			+ '<input type="submit" value="Se connecter"><br>' \
			+ '<a href="utilisateurs.py" title="Mot de passe oublié">J\'ai oublié mon mot de passe</a><br>' \
			+ '<a href="utilisateurs.py?action=nonInscrit" title="Création de compte">Je n\'ai pas de compte</a>'
	else:
		formConnexion += '<input type="text" name="nom" id="nom" placeholder="Votre nom"><span class="erreur"></span><br>' \
			+ '<input type="text" name="prenom" id="prenom" placeholder="Votre prénom"><span class="erreur"></span><br>' \
			+ '<input type="email" name="email" id="email" placeholder="Votre email"><span class="erreur"></span><br>' \
			+ '<input type="submit" value="S\'inscrire"><br>' \
			+ '<a href="utilisateurs.py?action=inscrit" title="Connexion">J\'ai déjà un compte</a>'
	formConnexion += '</form>'
	print '<h1>Page de connexion</h1>'
	print '<div>'
	print (h2)
	print (formConnexion)
	print '</div>'

#def connexion():
	# Traitement du formulaire de connexion avec BDD
	# Création des sessions nécessaires
	# Création des cookies si connexion auto

#def deconnexion():

#def inscription():

def pageUtilisateur():
	if action == 'modifMdp':
		nextAction = 'ModifMdp'
		h2 = '<h2>Modifier mon mot de passe</h2>'
	else:
		nextAction = 'ModifEmail'
		h2 = '<h2>Modifier mon email</h2>'
	formUtilisateur = '<form action="utilisateur.py" method="post">' \
		+ '<input type="hidden" name="action" value="' + nextAction + '">'
	if nextAction == 'ModifEmail':
		formUtilisateur += '<input type="email" name="emailAvt" id="emailAvt" placeholder="Votre nouvel email"><span class="erreur"></span><br>' \
		+ '<input type="email" name="emailApr" id="emailApr" placeholder="Confirmez votre email"><span class="erreur"></span><br>' \
		+ '<input type="submit" value="Modifier">'
	else:
		formUtilisateur += '<input type="password" name="mdpAvt" id="mdpAvt" placeholder="Votre nouveau mot de passe"><span class="erreur"></span><br>' \
		+ '<input type="password" name="mdpApr" id="mdpApr" placeholder="Confirmez votre mot de passe"><span class="erreur"></span><br>' \
		+ '<input type="submit" value="Modifier">'
	formUtilisateur += '</form>'
	print '<h1>Mes informations</h1>'
	print '<div>'
	print (h2)
	print '<a href="utilisateurs.py?action=modifEmail" title="Modifier son email">Modifier l\'email</a>'
	print '<a href="utilisateurs.py?action=modifMdp" title="Modifier son mot de passe">Modifier le mot de passe</a>'
	print (formUtilisateur)
	print '</div>'

#def modifMail():

#def modifMdp():

def editUtilisateur():
    if action == 'Modifier':
        uid = form.getvalue('id')
        cursor = db.cursor()
        cursor.execute("select * from utilisateur where id = " + str(uid))
        row = cursor.fetchone()
        nom = row[1]
        prenom = row[2]
        email = row[3]
        nextAction = 'EnregistrerModification'
        h2 = '<h2>Modifier un utilisateur</h2>'
    else:
    	h2 = '<h2>Ajouter un utilisateur</h2>'
        nom = ''
        prenom = ''
        email = ''
        nextAction = 'Ajouter'
    htmlForm = '<form action="utilisateurs.py" method="post">' \
        + '<input type="text" name="nom" id="nom" placeholder="Nom" value="' + str(nom) + '"/><span class="erreur"></span><br>' \
        + '<input type="text" name="prenom" id="prenom" placeholder="Prénom" value="' + str(prenom) + '"/><span class="erreur"></span><br>' \
        + '<input type="email" name="email" id="email" placeholder="Email" value="' + str(email) + '"/><span class="erreur"></span><br>' \
        + '<input type="hidden" name="action" value="' + nextAction + '"/>'
    if nextAction == 'EnregistrerModification':
        htmlForm += '<input type="hidden" name="id" value="' + uid + '"/>' \
        + '<input type="submit" value="Enregistrer la modification" /><br>' \
        + '<a href="utilisateurs.py" title="Ajouter un utilisateur">Ajouter un utilisateur</a>'       
    else:
        htmlForm += '<input type="submit" value="Ajouter" />'
    htmlForm += '</form>'
    print '<h1>Gestion des utilisateurs</h1>'
    print '<div>'
    print (h2)
    print (htmlForm)
    print '</div>'

def deleteUtilisateur():
    if action == 'Supprimer':
        uid = form.getvalue('id')
        sql = "DELETE FROM utilisateur WHERE not(admin) and id = " + uid
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        
def insertUtilisateur():
    if action == 'Ajouter' or action == "EnregistrerModification":
        nom = form.getvalue('nom')
        prenom = form.getvalue('prenom')
        email = form.getvalue('email')
        if (nom == None or prenom == None or email == None):
            return
        if action == 'Ajouter' :
            sql = "INSERT INTO utilisateur(nom, prenom, email) VALUES ('" \
                + nom + "', '" \
                + prenom + "', '" \
                + email + "');"
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        '''else:
            uid  = form.getvalue('id')
            sql = "UPDATE utilisateur SET " \
                + "nom = '" + nom + "', " \
                + "prenom = '" + prenom + "', " \
                + "email = '" + email + "' " \
                + "WHERE id = " + str(uid)
	    cursor = db.cursor()
	    cursor.execute(sql)
	    db.commit()'''
    
def printUtilisateur(row):
    print '<tr><td>' + str(row[1]) + '</td><td>' + str(row[2]) + '</td><td>' + str(row[3]) \
        + '</td><td>' + str(row[4]) + '</td>'
    if row[4] != 1:
        print '<td><a href="utilisateurs.py?action=Supprimer&amp;id=' \
            + str(row[0]) + '">Supprimer</a>'
    print "</td><td>" \
        + '<a href ="utilisateurs.py?action=Modifier&amp;id=' + str(row[0]) \
        + '">Modifier</a></td></tr>'

def printUtilisateurs():
    cursor = db.cursor()
    cursor.execute("select * from utilisateur")
    print '<h2>Liste des utilisateurs</h2>'
    print("<table>")
    print ('<thead><tr><th>Nom</th> <th> Prénom</th> <th> Email</th> <th> Admin</th> <th>'
    + 'Suppression</th>  <th> Modification</th></tr></thead><tbody>')
    for row in cursor.fetchall():
        printUtilisateur(row)
    print("</tbody></table>")


form = cgi.FieldStorage()
action = form.getvalue('action')
printHead()
printHeader()

# Si cookies / sessions vides
pageConnexion()
#traitementConnexion()

#Si session sans droits admin
#pageUtilisateur()

# Si session avec droits admin
#editUtilisateur()
#insertUtilisateur()
#deleteUtilisateur()
#printUtilisateurs()

printFooter()
db.close()
