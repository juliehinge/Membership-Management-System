from MMSLog import MMSLog
from Membership import Membership
from Memberships import Memberships
from MMS import MMS
from SuperMarkets import SuperMarkets

class Session:
    def __init__(self):
        self.membership = Membership()
        self.memberships = Memberships()
        self.MMS = MMS()
        self.MMSLog = MMSLog()
        self.SuperMarkets = SuperMarkets()


    def use(self):
        self.login_info()
        choice = self.read_login()
        while(choice != 'X'):
            if choice == "L":
                self.admin_menu_choice()
                return
            else:
                self.login_info()
            choice = self.read_login()
        print("\nSession Terminated!")


    def login_info(self):
        print("Membership Management System:")
        print("L- Login")
        print("X- Exit")

    def read_login(self):
        return str(input("Command (L/X): "))


    def read_choice(self):
        return str(input("Menu Commands (C/R/U/D/V/M/X): "))


    def verify_login(self):
        """Verifies that the username and password is correct"""

        email, password = self.MMSLog.get_info()
        while (email not in ["john.smith.uts.com", "jane.tyler.uts.com"]) or password not in (["user222", "super123"]):
            print("Incorrect SuperMarket details!")
            self.read_login()
            email, password = self.MMSLog.get_info()
        split_email = email.split('.')
        name = split_email[0] + " " + split_email[1]
        return name.title(), email, password
   

    def admin_menu_choice(self):
        name, email, password = self.verify_login()


        self.admin_menu()
        print("Session Admin: " + name, end=" - ")
        choice = self.read_choice()
    
        while (choice != 'X'):    
            if choice == 'C':
                self.add_membership()
            elif choice == 'R':
                self.retrieve_memberships()
            elif choice == 'U':
                self.update_membership()
            elif choice == 'D':
                self.delete_membership()
            elif choice == 'V':
                self.view_memberships()
            elif choice == 'M':
                self.MMS_menu(name)
            else:
                self.admin_menu()
            print("Session Admin: " + name, end=" - ")
            choice = self.read_choice()
        print("\nMMS Management System:")
        self.read_login()
        print("\nSession Terminated!")
        return

    def add_membership(self):
        self.membership.add_member("created")

    def view_memberships(self):
        self.membership.view_info()

    def retrieve_memberships(self):
        self.membership.retrieve()

    def update_membership(self):
        self.membership.update()

    def delete_membership(self):
        self.membership.delete()


    def MMS_menu(self, name):
        self.MMS.MMS_use(name)



    def admin_menu(self):
        print("Admin Menu: ")
        print("C- Add Membership")
        print("R- View Membership")
        print("U- Update Membership")
        print("D- Delete Membership")
        print("V- View Memberships")
        print("M- MMS Menu")
        print("X- Logout")



if __name__ == '__main__':
    session = Session()
    session.use()

