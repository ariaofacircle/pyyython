# 3 tries for a password

for x in range(3):
    passw = input("Password: ")
    if passw == "Yes":
        print("Opened.")
        break
else:
    print("Access Denied")
