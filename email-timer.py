import time
import smtplib
run = input("Start? > ")
mins = 0


if run == "start":
    
    while mins != 20:
        
        
        time.sleep(5)
        to = ''
        gmail_user=""
        gmail_pwd=""
        smtpserver=smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        msg = "hehhaha made it! yo budhu!"
        smtpserver.sendmail(gmail_user, to, msg)
        print('done')
        smtpserver.close()
        
        mins += 1


