from Utils import Utils
from SuperMarkets import SuperMarkets
from Memberships import Memberships

class SuperMarket:
    def __init__(self):
        self.SuperMarkets = SuperMarkets()
        self.mms_dict = self.SuperMarkets.return_mms_dict()
        self.Memberships = Memberships()

    def view_MMS_Report(self):
        print("MMS Report: ")
        Utils.slipHeader()
        for v in self.mms_dict.values():
            print(Utils.slipFormat(v[0], v[1], v[2], int(v[3]), v[4]))
        Utils.slipTableEnd()



    def view_total(self, _dict):
        """Function to calculate and view the total details for all members
        registered in the system"""
        total_expense = 0
        total_credit = 0
        total_dollars = 0
        total_drate = 0
        total_Gdrate = 0
        total_ppc = 0

        for v in self.mms_dict.values():
            total_expense += v[1]
            total_dollars += int(v[3])
            Type, PpC, DRate, GDrate = self.Memberships.calc_type(v[1])
            total_ppc += PpC
            total_credit += PpC * v[1]
            total_drate += DRate
            total_Gdrate += GDrate

        titles = ["Total expense", "Total credits", "Total dollars", "Average pay per credit", "Average deduction rate", "Average gas deduction rate"]
        li = [total_expense, total_credit, total_dollars, total_ppc/len(self.mms_dict.values()), total_drate/len(self.mms_dict.values()), total_Gdrate/len(self.mms_dict.values())]
        print("")
        Utils.totalsTableHeaderAndEnd()
        for title, item in zip(titles,li):
            print(Utils.totalsFormat(title, item))
        Utils.totalsTableHeaderAndEnd()

       



    def return_slip(self):
        name = input("Name: ")
        if name in self.mms_dict:
            print("Slip Details:")
            n = self.mms_dict.get(name)[0]
            e = self.mms_dict.get(name)[1]
            c = self.mms_dict.get(name)[2]
            d = self.mms_dict.get(name)[3]
            t = self.mms_dict.get(name)[4]
            Utils.slipHeader()
            print(Utils.slipFormat(n, e, c, int(d), t))
            Utils.slipTableEnd()
        else:
            print("Slip details does not exist for "+name + "!")
        



