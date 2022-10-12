from Utils import Utils

class Memberships:
    

    def __init__(self):
        self



    def calc_type(self, expense):
        """Calculates and returns information based on the expense of the member"""
        if 0 <= float(expense) < 500:
            return "Bronze", 20, 0.05, 0.1 
        elif 500 <= float(expense) < 1500 :
            return "Silver", 10, 0.1, 0.15 
        elif 1500 <= float(expense) < 3000 :
            return "Gold", 8, 0.15, 0.2 
        elif 3000 <= float(expense) < 5000 :
            return "Diamond", 6, 0.2, 0.25 
        elif float(expense) >= 5000 :
            return "Platinum", 4, 0.25, 0.3 
        


    def return_dict(self):
        """Adding members already in the system and returning them"""

        member_dict = dict()

        name = ["Thomas Muller", "Alice Stefan", "Lucy Lu", "Andreas Brehme", "Ruddy Voller", "Monica Shwarz"]
        email = ["thomas.muller@uts.com", "alice.stefan@uts.com ", "lucy.lu@uts.com ", "andreas.b@uts.com", "ruddy.v@uts.com","monica.s@uts.com"]
        phone = ["99991111", "88881111","98981100","90001222","98980000","92241188"]
        expense = [2134.5, 4512.2 , 158.4 ,7596.3, 1100.0 , 6741.2 ]

        for item in range(len(name)):
            key = name[item]
            value = [name[item], email[item], phone[item], self.calc_type(expense[item])[0]]
            member_dict[key] = value
        
        return member_dict






