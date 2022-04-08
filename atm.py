class atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def cashWithDrawl(self):
        print("enter the money u want to withdraw") 

    def balenceEnquiry (self):
        print("u have 10000/- in your bank account")    


mycard=atm("139294","0001")   
print(mycard.balenceEnquiry) 