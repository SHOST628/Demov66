import smtplib

smtp = smtplib.SMTP()
smtp.connect("smtp.tech-trans.com",25)
smtp.ehlo()
smtp.login("ttsz","24945000")
smtp.sendmail("test@tech-trans.com","599531369@qq.com","test")
smtp.quit()