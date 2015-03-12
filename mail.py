#!C:/python27/python.exe
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import bdd, conf

def sendMail(action): #mail inscription + mdp oublié
    if action == 'envoieMdp':
        email=form.getvalue('email')
        newPassword=genereMdp()
        mdp_hach = hachage(newPassword)
        bdd.updateMdpOublie(mdp_hach, email)
        sendMdp(email, newPassword, 'Bonjour, votre nouveau mot de passe est ', 'Mot de passe oublié')
    if action == 'inscription':
        email=form.getvalue('email')
        nom=form.getvalue('nom')
        prenom=form.getvalue('prenom')
        newPassword=genereMdp()
        mdp_hach = hachage(newPassword)
        bdd.insertInscription(nom, prenom, email, mdp_hach)
        sendMdp(email, newPassword, 'Bonjour, votre mot de passe est ', 'Inscription')
    conf.redirect()

def sendMdp(destinataire, mdp, text, sujet):
    msg = MIMEMultipart()
    msg['From'] = 'mdpoublieM2L@gmail.com'
    msg['To'] = destinataire
    msg['Subject'] = sujet
    message = text + mdp
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('mdpoublieM2L@gmail.com', 'osefdumdp')
    mailserver.sendmail('mdpoubliem2l@gmail.com', destinataire, msg.as_string())
    mailserver.quit()