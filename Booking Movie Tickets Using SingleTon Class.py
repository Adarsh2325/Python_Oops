def SingleTon(arg):
    L=[]
    def inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return inner
@SingleTon
class Movie1():
    def __init__(self):
        self.totaltic=200
    def booking(self):
        reqtic=int(input('Enter no. of Tickets : '))
        if reqtic<=self.totaltic:
            print('Ticket Booked Successfully.....')
            self.totaltic=self.totaltic-reqtic
            print(f'Available Ticket is {self.totaltic}')
        else:
            print('Tickets Not Available')
def bookmyshow():
    user = Movie1()
    user.booking()
user1 = bookmyshow()
print('----------------------------')
user2 = bookmyshow()

