from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open('admin.key', 'wb') as f:
#         f.write(key)

admin = input("Enter key... ")

if admin != "admin":
    print("Get out Imposter!!!")
    exit

def load_key():
    file = open('admin.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()

def view():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():                     #f.readlines() -- for reading line a single line
            data = lines.rstrip()                       #lines.rstrip() -- for ignoring new line at the end of the file
            user, passw = data.split("|")               #data.split() -- is spliting the string and storing every part in a list.
            passw = Fernet(key).decrypt(passw.encode()).decode()   #decrypt pass with the key
            print(f"username: {user}\npassword: {passw}\n---------------\n")

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter password: ")
    pwd = Fernet(key).encrypt(pwd.encode()).decode()    #encrypt password with the key

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("would you like to add a new password or view a existing password? (view, add), press 'q' to quit ").lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
