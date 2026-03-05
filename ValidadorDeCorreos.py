
email = input ("Enter your email address please: ")

if email.count("@") == 1 and "." in email.split ("@")[1]:
    print ("valid")

else:
    print ("Invalid")

        