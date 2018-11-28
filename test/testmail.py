import smtplib

smtp = smtplib.SMTP()
smtp.connect("smtp.tech-trans.com", 25)
smtp.ehlo()
smtp.login("ttsz", "24945000")
smtp.sendmail("smtp.tech-trans.com", "Sincave.Zhang@tech-trans.com", "test")
smtp.quit()