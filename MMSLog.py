from Utils import Utils
from SuperMarkets import SuperMarkets
from SuperMarket import SuperMarket

class MMSLog:
    def __init__(self):
        self.SuperMarkets = SuperMarkets()
        self.SuperMarket = SuperMarket()
        self.name = " "
        self.MMS_record = []
        self.MMS_name_list = []
        self.MMS_log =[]
        self.mms_dict = self.SuperMarkets.return_mms_dict()


    def get_info(self):
        """Getting password and email from user"""

        email = str(input("Email: "))
        email = email.replace('@', '.')
        password = input("Password: ")
        return email, password
               

    def MMS_archieve(self, name): 
        num =str(len(self.MMS_record)+1)
        print("MMS record is created as:" + name + num)
        self.MMS_name_list.append(name + num)
        self.MMS_record.append(num)



    def MMS_show(self):
        print("MMS Archive:")
        Utils.logHeader()
        for num, name in zip(self.MMS_record, self.MMS_name_list):
            print(Utils.logFormat("MMS " + str(num), name))
        Utils.logTableEnd()
        

    def MMS_retrieve(self):
        """Retrieves the supermarket log depending on  which user is using the system"""

        record = dict()
        RecordID = input("RecordID: ")
        record[RecordID] = self.mms_dict
        self.MMS_log.append(record[RecordID])
        

        if len(self.MMS_record) == 0:
            print("No MMS is recorded as: "+ RecordID)
        else:
            print("MMS Report: ")
            Utils.slipHeader()

            for v in record[RecordID].values():
                print(Utils.slipFormat(v[0], v[1], v[2], int(v[3]), v[4]))
            Utils.slipTableEnd()
            self.SuperMarket.view_total(record[RecordID].values())


