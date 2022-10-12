from Memberships import Memberships
from Utils import Utils

class SuperMarkets:
    def __init__(self):
        self.Memberships = Memberships()
        self.mms_dict = self.return_mms_dict()


    def return_mms_dict(self):
        mms_dict = dict()
        name = ["Thomas Muller", "Alice Stefan", "Lucy Lu", "Andreas Brehme", "Ruddy Voller", "Monica Shwarz"]
        Expense = [2134.50, 4512.20, 158.40, 7596.30, 1100.00, 6741.20]


        for item in range(len(name)):
            key = name[item]
            Type, PpC, Drate, GDrate = self.Memberships.calc_type(Expense[item])
            value = [name[item], Expense[item], PpC*Expense[item], (PpC*Expense[item])/200, Type]
            mms_dict[key] = value

        return mms_dict

 



