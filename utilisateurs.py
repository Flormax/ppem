#!C:/python27/python.exe

import cgi
import MySQLdb
import sys

db = MySQLdb.connect("localhost", "toto", "", "utilisateurs")

def dismoitout(requete):
    try:
        cursor = db.cursor()
        cursor.execute(requete)
        db.commit()
    except MySQLdb.Error, e:
        print "Content-Type: text/html\n"
        print "<html>"
        print "<body>"
        print "Error %d: %s" % (e.args[0], e.args[1])
        print "</body>"
        print "</html>"
        sys.exit(1)    
        

def connectionToHost():
    try:
        db = MySQLdb.connect("localhost", "toto", "", "utilisateurs")
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")

        print "Content-Type: text/html\n"
        print "<html>"
        print "<body>"
        print "MySQL version: %s" % \
            cursor.fetchone()
        print "</body>"
        print "</html>"
        
    except MySQLdb.Error, e:
        print "Content-Type: text/html\n"
        print "<html>"
        print "<body>"
        print "Error %d: %s" % (e.args[0], e.args[1])
        print "</body>"
        print "</html>"
        sys.exit(1)


def printHead():
    print "Content-Type: text/html\n"
    print "<head>"
    print '<meta charset="UTF-8">'
    print ("<TITLE>Gestion des utilisateurs</TITLE>")
    print "</head>"
    print ("<H1>Gestion des utilisateurs</H1>")



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
    else:
        nom = ''
        prenom = ''
        email = ''
        nextAction = 'Ajouter'
    htmlForm = '<form action="utilisateurs.py" method="post">' \
        + 'Nom : <input type="text" name="nom" value="' + str(nom) + '"/><BR>' \
        + 'Prenom : <input type="text" name="prenom" value="' + str(prenom) + '"/><BR>' \
        + 'Email : <input type="text" name="email" value="' + str(email) + '"/><BR>' \
        + '<input type="hidden" name="action" value="' + nextAction + '"/>'
    if nextAction == 'EnregistrerModification':
        htmlForm += '<input type="hidden" name="id" value="' + uid + '"/>' \
        + '<input type="submit" value="Enregistrer la modification" />'        
    else:
        htmlForm += '<input type="submit" value="Ajouter" />'
    print (htmlForm)

'''def deleteUtilisateur():
    if action == 'Supprimer':
        uid = form.getvalue('id')
        sql = "DELETE FROM utilisateur WHERE not(admin) and id = " + uid
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()'''
        
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
          
        #else
            #uid  = form.getvalue('id')
            #sql = "UPDATE utilisateur SET " \
                #+ "nom = '" + nom + "', " \
                #+ "prenom = '" + prenom + "', " \
                #+ "email = '" + email + "' " \
                #+ "WHERE id = " + str(uid)
        #cursor = db.cursor()
        #cursor.execute(sql)
        #db.commit()
    
def printUtilisateur(row):
    print '<TD>' + str(row[1]) + '<TD>' + str(row[2]) + '<TD>' + str(row[3]) \
        + '<TD>' + str(row[4]) + '<TD>'
    if row[4] != 1:
        print '<a href="utilisateurs.py?action=Supprimer&id=' \
            + str(row[0]) + '">supprimer</a>'
    print "<TD>" \
        + '<a href ="utilisateurs.py?action=Modifier&id=' + str(row[0]) \
        + '">modifier</a><TR>'

def printUtilisateurs():
    cursor = db.cursor()
    cursor.execute("select * from utilisateur")
    printHead()
    print("<TABLE BORDER=1>")
    print ('<TH> nom <TH> prenom <TH> e-mail <TH> admin <TH>'
    + 'suppression  <TH> modification <TR>')
    for row in cursor.fetchall():
        printUtilisateur(row)
    print("</TABLE>")

connectionToHost()
form = cgi.FieldStorage()
action = form.getvalue('action')
printHead()
editUtilisateur()
insertUtilisateur()
#deleteUtilisateur()
printUtilisateurs()
db.close()
