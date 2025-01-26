class SBI:
    ROI=0.07
    def __init__(self,name,mobno,aadhar,PAN,bal,pin):
        self.name=name
        self.mobno=mobno
        self.aadhar=aadhar
        self.PAN=PAN
        self.bal=bal
        self.pin=pin
    def details(self):
        print(f'Name: {self.name}')
        print(f'MobNo: {self.mobno}')
        print(f'Aadhar: {self.aadhar}')
        print(f'PAN: {self.PAN}')
        print(f'Bal: {self.bal}')
    def withdraw(self):
        if self.checkpin()==self.pin:
            amount=int(input('Enter the amount : '))
            if self.bal>amount:
                print('Amount Debited Successfully.....')
                self.bal=self.bal-amount
                print(f'Available Balance is {self.bal} ')
            else:
                print('Insufficient Funds')
        else:
            print('Invalid Pin')
    @staticmethod
    def checkpin():
        return int(input('Enter the Pin : '))
    def deposit(self):
        if self.checkpin()==self.pin:
            amount=int(input('Enter the amount : '))
            print('Amount Credited Successfully.....')
            self.bal=self.bal+amount
            print(f'Available Balance is {self.bal} ')
        else:
            print('Invalid Pin')
    def checkbal(self):
        if self.checkpin()==self.pin:
            print(f'Avilable Balance is {self.bal}')
        else:
            print('Invalid Pin')
    @classmethod
    def changeROI(cls):
        var=float(input('Enter the New ROI : '))
        cls.ROI=var
        print('ROI Updated Successfully....')
    def changepin(self):
        PIN=int(input('Enter the Pin : '))
        if self.pin==PIN:
            NewPin=int(input('Enter the New Pin :  '))
            print('New PIN Updated Successfully....')
            self.pin=NewPin
        else:
            print('Incorrect PIN')
c1=SBI('Farzeen',9293947255,267338462433,'DYSPA4962K',900000,8989)
c2=SBI('Razim',9293627263,762438273966,'IEYPA1863L',1000000,9494)
c1.checkpin()
c2.withdraw()
c1.deposit()
c2.changepin()
c1.changeROI()


        
        
