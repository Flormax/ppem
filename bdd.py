#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import MySQLdb
import conf

db = MySQLdb.connect("localhost", "root", "", "utilisateurs")

def selectUtilisateur(id): #editUtilisateur
    cursor = db.cursor()
    cursor.execute("""SELECT *
    FROM utilisateur 
    WHERE id =%s;""",(id))
    return cursor

def deleteUtilisateur(id): #deleteUtilisateur()
    cursor = db.cursor()
    cursor.execute("""DELETE FROM utilisateur 
    WHERE not(admin) and id =%s """,(id))
    db.commit()
    conf.redirect()

def insertUtilisateur(nom, prenom, email): #insertUtilisateur()/ajout
    param=(nom, prenom, email)
    cursor = db.cursor()
    cursor.execute("""INSERT INTO `utilisateurs`.`utilisateur` (`nom`, `prenom`, `email`) 
    VALUES (%s, %s, %s);""",(param))
    db.commit()
    conf.redirect()

def updateUtilisateur(nom, prenom, email, id): #insertUtilisateur()/modif
    param=(nom, prenom, email, id)
    cursor = db.cursor()
    cursor.execute("""UPDATE `utilisateurs`.`utilisateur` 
    SET `nom` =%s, `prenom` = %s, `email` =%s 
    WHERE `utilisateur`.`id` =%s;""",(param))
    db.commit()
    conf.redirect()

def selectUtilisateur(): #printUtilisateur()
    cursor = db.cursor()
    cursor.execute("select * from utilisateur") 
    return cursor  

def update(mdp, email): #sendMail()
    param=(mdp, email)
    cursor = db.cursor()
    cursor.execute("""UPDATE `utilisateurs`.`utilisateur` 
    SET `mdp` = %s 
    WHERE `utilisateur`.`email` =%s;""",(param))
    db.commit()

def insert(nom, prenom, email, mdp): #sendMail()
    param=(nom, prenom, email, mdp)
    cursor = db.cursor()
    cursor.execute("""INSERT INTO `utilisateurs`.`utilisateur` (`nom`, `prenom`, `email`, `mdp`) 
    VALUES (%s, %s, %s, %s);""",(param))
    db.commit()

def changeMdp(id, mdp): #modifMDP pageUtilisateur()
    param=(mdp, id)
    cursor = db.cursor()
    cursor.execute("""UPDATE `utilisateurs`.`utilisateur` 
    SET `mdp` = %s 
    WHERE `utilisateur`.`id` =%s;""",(param))
    db.commit()
    conf.redirect()
    
def changeEmail(id, email): #modifEMAIL pageUtilisateur()
    param=(email, id)
    cursor = db.cursor()
    cursor.execute("""UPDATE `utilisateurs`.`utilisateur` 
    SET `email` = %s 
    WHERE `utilisateur`.`id` =%s;""",(param))
    db.commit()
    conf.redirect()
    