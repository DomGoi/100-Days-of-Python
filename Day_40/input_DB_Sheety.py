import sheety



f_name=input("What is your first name?").title().strip()
l_name=input("What is your last name?").title().strip()
mail_1=input("What is your mail?").strip()
mail_2=input("Please confirm your email").strip()

while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

sheety.post_user_sheety(f_name, l_name, mail_1)


