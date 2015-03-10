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