from Utils import Utils
from MMSLog import MMSLog
from SuperMarket import SuperMarket
from SuperMarkets import SuperMarkets
from Membership import Membership

class MMS:
    def __init__(self):
        self.MMSLog = MMSLog()
        self.SuperMarket = SuperMarket()
        self.SuperMarkets = SuperMarkets()
        self.membership = Membership()

    def MMS_menu(self):
        print("MMS Menu: ")
        print("F- Find Slip Details")
        print("V- View MMS Report")
        print("A- Archive MMS Report")
        print("R- Retrieve MMS Report")
        print("S- Show MMS Log")
        print("X- Close")


    def MMS_use(self, name):
        """Calls functions depending on what the user wants to do"""
        self.MMS_menu()
        print("Session Admin: " + name, end=" - ")
        choice = self.read_choice()
    
        while (choice != 'X'):    
            if choice == 'F':
                self.find_slip_details()
            elif choice == 'V':
                self.view()
            elif choice == 'A':
                self.archieve(name)
            elif choice == 'R':
                self.mmsretrieve()
            elif choice == 'S':
                self.show()
            else:
                self.MMS_menu()
            print("Session Admin: " + name, end=" - ")
            choice = self.read_choice()
        print("\nSuperMarket Menu:")


    def read_choice(self):
        return str(input("Menu Commands (F/V/A/R/S/X): "))

    def find_slip_details(self):
        self.SuperMarket.return_slip()
        

    def view(self):
        self.SuperMarket.view_MMS_Report()
        self.SuperMarket.view_total(self.SuperMarkets.return_mms_dict())


    def archieve(self, name):
        self.MMSLog.MMS_archieve(name)

    def show(self):
        self.MMSLog.MMS_show()


    def mmsretrieve(self):
        self.MMSLog.MMS_retrieve()


