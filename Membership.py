from Utils import Utils
from Memberships import Memberships
from SuperMarkets import SuperMarkets
from MMSLog import MMSLog

class Membership:
    def __init__(self):
        # Initializing all the details about the member
        self.name = " "
        self.Email = " "
        self.Phone = " "
        self.Address = " "
        self.ID = " "
        self.expense = 0
        self.Memberships = Memberships()
        self.member_dict = self.Memberships.return_dict()
        self.SuperMarkets = SuperMarkets()
        self.mms_dict = self.SuperMarkets.return_mms_dict()


    def add_member(self, action):
        # Getting details from user and saving them
        self.name = input("Name: ")
        self.Email = input("Email: ")
        self.Phone = input("Phone: ")
        self.Address = input("Address: ")
        self.ID = input("ID: ")
        self.expense += int(input("expense: "))
        print(self.name + " record has been " + action + ".")
        self.member_dict[self.name] = [self.name, self.Email, self.Phone, self.Memberships.calc_type(self.expense)[0]]
 
     

    def return_member(self):
        return self.name, self.Email, self.Phone, self.ID, self.expense
    

    def view_info(self):
        """Print information about all members in the system plus newly added members """
        Type, PpC, Drate, GDrate = self.Memberships.calc_type(self.expense)
        Utils.membershipHeader()
        for v in self.member_dict.values():
            print(Utils.studentFormat(v[0], v[1], v[2], v[3]))
        if self.name != " " and self.name not in self.member_dict:
            print(Utils.studentFormat(self.name, self.Email, self.Phone, Type))
        Utils.membershipTableEnd()


    def retrieve(self):
        """Retrieves information about a particular member and prints that information"""

        name = input("Name: ")
        
        if name in self.member_dict.keys():
            name = self.member_dict.get(name)[0]
            Email = self.member_dict.get(name)[1]
            Phone = self.member_dict.get(name)[2]
            Type = self.member_dict.get(name)[3]
            Utils.membershipHeader()
            print(Utils.studentFormat(name, Email, Phone, Type))
            Utils.membershipTableEnd()

        else:
            print(name + " record does not exist!")


    def update(self):

        name = input("Name: ")
        print("Updating " + name + " record: ")
        self.add_member("updated")

        Type, PpC, Drate, GDrate = self.Memberships.calc_type(self.expense + self.mms_dict[name][1])
        self.member_dict.update({name: [self.name, self.Email, self.Phone, Type]})
        self.mms_dict.update({name: [name, self.expense + self.mms_dict[name][1], PpC*self.expense, (PpC*self.expense)/200, Type]})



    def delete(self):
        name = input("Name: ")
        if name in self.member_dict:
            self.member_dict.pop(name)
            print(name + " record has been deleted.")
        else: 
            print(name + " record does not exist!")
        


