#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Envoiemail():
    try:

        msg = MIMEMultipart()
        msg['From'] = input('E-MAIL DU DESTINATEUR : ')
        msg['To'] = input('E-MAIL DU DESTINATAIRE : ')
        msg['Subject'] = input('OBJET : ')
        message = input('MESSAGE : ')
        password = input('MOT DE PASSE : ')
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(msg['From'], password)
        mailserver.sendmail(msg['From'], msg['To'], msg.as_string())
        mailserver.quit()

        print("\n \t\t\tEMAIL ENVOYE AVEC SUCCES")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)

# if __name__ == '__main__':
#     Envoiemail()