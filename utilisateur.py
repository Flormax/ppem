#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import html, conf
import cgi
import cgitb
cgitb.enable()

def pageUtilisateur():
    if action == 'modifMdp':
        nextAction = 'modifMdp'
        h2 = '<h2>Modifier mon mot de passe</h2>'
    else:
        nextAction = 'modifEmail'
        h2 = '<h2>Modifier mon email</h2>'
    formUtilisateur = '<form action="conf.py" method="post">' \
        + '<input type="hidden" name="action" value="' + nextAction + '">'
    if nextAction == 'modifEmail':
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
    print '<a href="conf.py?action=modifEmail" title="Modifier son email">Modifier l\'email</a>'
    print '<a href="conf.py?action=modifMdp" title="Modifier son mot de passe">Modifier le mot de passe</a>'
    print (formUtilisateur)
    print '</div>'

conf.redirect()
form = cgi.FieldStorage()
action = form.getvalue('action')
html.printHeader()
pageUtilisateur()
html.printFooter()
