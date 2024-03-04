import smtplib

print("1.GoogleMail \n")
print("2.YahooMail \n")
print("3.Outlook \n")

service=input("Select your email provider number :-")


email=input("SENDER EMAIL :-")
password=input("ENTER THE EMAIL PASSWORD :-")
reciverEmail=input("RECIVER EMAIL :-")

subject=input("SUBJECT :-")
message=input("MESSAGE :-")


text= f"Subject: {subject}\n\n{message}"
def googleSendMail(email,reciverEmail,password,text):
    try:
       server=smtplib.SMTP("smtp.gmail.com",587)
       server.starttls()
       server.login(email , password )
       server.sendmail(email, reciverEmail,text)
       print("email has sent to the " + reciverEmail)
    except Exception as e:
        print("An error ocurred:",e)
    finally:
        server.quit()


def yahooSendMail(email,reciverEmail,password,text):
    try:
      server=smtplib.SMTP("smtp.mail.yahoo.com",587)
      server.starttls()
      server.login(email , password )
      server.sendmail(email, reciverEmail, text)
      print("email has sent to the " + reciverEmail)
    except Exception as e:
        print("An error ocurred:",e)
    finally:
        server.quit()


def outlookSendMail(email,reciverEmail,password,text):
    try:
      server=smtplib.SMTP("smtp.office365.com",587)
      server.starttls()
      server.login(email , password )
      server.sendmail(email, reciverEmail, text)
      print("email has sent to the " + reciverEmail)
    except Exception as e:
        print("An error ocurred:",e)
    finally:
        server.quit()


match service:
    case "1":
        googleSendMail(email,reciverEmail,password,text)
    case "2":
        yahooSendMail(email,reciverEmail,password,text)
    case "3":
        outlookSendMail(email,reciverEmail,password,text)
    case _:
        print("Pls provide the service number mentioned above")