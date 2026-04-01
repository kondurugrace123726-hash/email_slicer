
email = input("Enter your email: ").strip()

if "@" in email:
    username, domain = email.split("@")
    print("Username:", username)
    print("Domain:", domain)
else:
    print("Invalid email format")