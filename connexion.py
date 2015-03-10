#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import html, conf
import cgi
import cgitb
cgitb.enable()

def pageConnexion():
    if action == 'nonInscrit':
        nextAction = 'Inscription'
        h2 = '<h2>S\'inscrire</h2>'
    else:
        nextAction = 'connexion'
        h2 = '<h2>Se connecter</h2>'
    formConnexion = '<form action="conf.py" method="post">' \
        + '<input type="hidden" name="action" value="' + nextAction + '">'
    if nextAction == 'connexion':
        formConnexion += '<label for="email">Votre email</label><input type="email" name="email" id="email" placeholder="Email" required><span class="erreur"></span><br>' \
            + '<label for="mdp">Votre mot de passe</label><input type="password" name="mdp" id="mdp" placeholder="Votre mot de passe" required><span class="erreur"></span><br>' \
            + '<input type="checkbox" name="auto" id="auto"><label for="auto" class="auto">Connexion automatique</label><br>' \
            + '<input type="submit" value="Se connecter"><br>' \
            + '<a href="connexion.py?action=oublie" title="Mot de passe oublié">J\'ai oublié mon mot de passe</a><br>' \
            + '<a href="connexion.py?action=nonInscrit" title="Création de compte">Je n\'ai pas de compte</a>'
    else:
        formConnexion += '<label for="nom">Votre nom</label><input type="text" name="nom" id="nom" placeholder="Nom" required><span class="erreur"></span><br>' \
            + '<label for="prenom">Votre prénom</label><input type="text" name="prenom" id="prenom" placeholder="Prénom" required><span class="erreur"></span><br>' \
            + '<label for="email">Votre email</label><input type="email" name="email" id="email" placeholder="Email" required><span class="erreur"></span><br>' \
            + '<input type="submit" value="S\'inscrire"><br>' \
            + '<a href="connexion.py?action=inscrit" title="Connexion">J\'ai déjà un compte</a>'
    formConnexion += '</form>'
    print '<h1>Page de connexion</h1>'
    print '<div>'
    print (h2)
    print (formConnexion)
    print '</div>'
    
conf.redirect
form = cgi.FieldStorage()
action = form.getvalue('action')
html.printHead()
html.printHeader()
pageConnexion()
html.printFooter()