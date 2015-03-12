#!C:/python27/python.exe
# -*- coding: utf-8 -*-

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
                 <li><a href="conf.py?action=deconnexion" title="Déconnexion">Déconnexion</a>
                 <li><a href="conf.py?action=aide" title="Documentation">Aide</a>
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
 
def printUtilisateur(row):
    print '<tr><td>' + str(row[1]) + '</td><td>' + str(row[2]) + '</td><td>' + str(row[3]) \
        + '</td><td>' + str(row[4]) + '</td>'
    if row[4] != 1:
        print '<td><a href="utilisateurs.py?action=supprimer&amp;id=' \
            + str(row[0]) + '">Supprimer</a>'
    print "</td><td>" \
        + '<a href ="conf.py?action=modifier&amp;id=' + str(row[0]) \
        + '">Modifier</a></td></tr>'
        
def printUtilisateurs():
    bdd.selectAllUtilisateur()
    print '<h2>Liste des utilisateurs</h2>'
    print("<table>")
    print ('<thead><tr><th>Nom</th> <th> Prénom</th> <th> Email</th> <th> Admin</th> <th>'
    + 'Suppression</th>  <th> Modification</th></tr></thead><tbody>')
    for row in cursor.fetchall():
        printUtilisateur(row)
    print("</tbody></table>")