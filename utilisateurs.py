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
            <ul>
                 <li><a href="utilisateurs.py?action=deconnexion" title="Déconnexion">Déconnexion</a>
                 <li><a href="utilisateurs.py?action=aide" title="Documentation">Aide</a>
            </ul>
        </div> 
    </header>
    <section>
    '''

def printFooter():
    print '''
    </section>
    <script src="http://localhost/ppem/js/jquery.js"></script>
    <script src="http://localhost/ppem/js/parsley.js"></script>
    <script>
        $('form').parsley();
    </script>
        
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
	formConnexion = '<form action="utilisateurs.py" method="post">' \
		+ '<input type="hidden" name="action" value="' + nextAction + '">'
	if nextAction == 'Connexion':
		formConnexion += '<label for="email">Votre email</label><input type="email" name="email" id="email" placeholder="Email" required><span class="erreur"></span><br>' \
			+ '<label for="mdp">Votre mot de passe</label><input type="password" name="mdp" id="mdp" placeholder="Votre mot de passe" required><span class="erreur"></span><br>' \
			+ '<input type="checkbox" name="auto" id="auto"><label for="auto" class="auto">Connexion automatique</label><br>' \
			+ '<input type="submit" value="Se connecter"><br>' \
			+ '<a href="utilisateurs.py?action=oublie" title="Mot de passe oublié">J\'ai oublié mon mot de passe</a><br>' \
			+ '<a href="utilisateurs.py?action=nonInscrit" title="Création de compte">Je n\'ai pas de compte</a>'
	else:
		formConnexion += '<label for="nom">Votre nom</label><input type="text" name="nom" id="nom" placeholder="Nom" required><span class="erreur"></span><br>' \
			+ '<label for="prenom">Votre prénom</label><input type="text" name="prenom" id="prenom" placeholder="Prénom" required><span class="erreur"></span><br>' \
			+ '<label for="email">Votre email</label><input type="email" name="email" id="email" placeholder="Email" required><span class="erreur"></span><br>' \
			+ '<input type="submit" value="S\'inscrire"><br>' \
			+ '<a href="utilisateurs.py?action=inscrit" title="Connexion">J\'ai déjà un compte</a>'
	formConnexion += '</form>'
	print '<h1>Page de connexion</h1>'
	print '<div>'
	print (h2)
	print (formConnexion)
	print '</div>'

def pageUtilisateur():
	if action == 'modifMdp':
		nextAction = 'ModifMdp'
		h2 = '<h2>Modifier mon mot de passe</h2>'
	else:
		nextAction = 'ModifEmail'
		h2 = '<h2>Modifier mon email</h2>'
	formUtilisateur = '<form action="utilisateurs.py" method="post">' \
		+ '<input type="hidden" name="action" value="' + nextAction + '">'
	if nextAction == 'ModifEmail':
		formUtilisateur += '<label for="emailAvt">Votre nouvel email</label><input type="email" name="emailAvt" id="emailAvt" placeholder="Nouvel email" required><span class="erreur"></span><br>' \
		+ '<label for="emailApr">Confirmez le nouvel email</label><input type="email" name="emailApr" id="emailApr" placeholder="Confirmez" data-parsley-equalto="#emailAvt" required><span class="erreur"></span><br>' \
		+ '<input type="submit" value="Modifier">'
	else:
		formUtilisateur += '<label for="mdpAvt">Votre nouveau mot de passe</label><input type="password" name="mdpAvt" id="mdpAvt" placeholder="Nouveau mot de passe" required><span class="erreur"></span><br>' \
		+ '<label for="mdpApr">Confirmez le nouveau mot de passe</label><input type="password" name="mdpApr" id="mdpApr" placeholder="Confirmez" data-parsley-equalto="#mdpAvt" required><span class="erreur"></span><br>' \
		+ '<input type="submit" value="Modifier">'
	formUtilisateur += '</form>'
	print '<h1>Mes informations</h1>'
	print '<div class="page-utilisateur">'
	print (h2)
	print '<a href="utilisateurs.py?action=modifEmail" title="Modifier son email">Modifier l\'email</a>'
	print '<a href="utilisateurs.py?action=modifMdp" title="Modifier son mot de passe">Modifier le mot de passe</a>'
	print (formUtilisateur)
	print '</div>'

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
        + '<label for="nom">Nom</label><input type="text" name="nom" id="nom" placeholder="Nom" value="' + str(nom) + '"/ required><span class="erreur"></span><br>' \
        + '<label for="prenom">Prénom</label><input type="text" name="prenom" id="prenom" placeholder="Prénom" value="' + str(prenom) + '"/ required><span class="erreur"></span><br>' \
        + '<label for="email">Email</label><input type="email" name="email" id="email" placeholder="Email" value="' + str(email) + '"/ required><span class="erreur"></span><br>' \
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
#pageConnexion()

#Si session sans droits admin
#pageUtilisateur()

# Si session avec droits admin
#editUtilisateur()
#insertUtilisateur()
#deleteUtilisateur()
#printUtilisateurs()

printFooter()
db.close()
