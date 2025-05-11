__Author__ = "Mouza Alameri"
__Date__ = "11/05/2025"

from colorama import Fore, Style, init
init(autoreset=True)

class User:
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd

    def show_pwd(self):
        print(Fore.YELLOW + "Homegirl you don't got access to all of that.")

class SuperAdmin(User):
    def show_pwd(self):
        print(Fore.GREEN + f"Password: {self.pwd}")

class GuestUser(User):
    def show_pwd(self):
        print(Fore.RED + "Not Authorized to view password.")

class SecurityOfficer(User):
    def show_pwd(self):
        if len(self.pwd) >= 12 and any(char.isdigit() for char in self.pwd):
            print(Fore.GREEN + "Password meets security standards.")
        else:
            print(Fore.RED + "Password is weak. Must be at least 12 characters and contain a number.")

role = input("Select role (user, guestuser, superadmin, securityofficer): ").lower()
password = input("Enter your password: ")
username = "anonymous"

if role == "superadmin":
    user = SuperAdmin(username, password)
elif role == "guestuser":
    user = GuestUser(username, password)
elif role == "securityofficer":
    user = SecurityOfficer(username, password)
else:
    user = User(username, password)

user.show_pwd()
