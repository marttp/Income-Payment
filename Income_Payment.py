class Employee:
    name = ""
    income = list()
    payment = list()
    nowMoney = 0

    def __init__(self, name1):
        self.name = name1

    def sumincome(self):
        allIncome = sum(self.income)
        return allIncome

    def allpayment(self):
        allPay = sum(self.payment)
        return allPay

    def receive(self, salary):
        print("Receive :", salary)
        self.income.append(salary)
        self.nowMoney += salary

    def pay(self, buy):
        if self.nowMoney - buy > 0:
            print("Buy : ", buy)
            self.nowMoney -= buy
            self.payment.append(buy)
        else:
            print("Can't pay. I don't have enough money for this.")

    def printstatmoney(self):
        print("Income :", self.income)
        print("Payment :", self.payment)
        print("Sum income :", self.sumincome())
        print("All payment :", self.allpayment())
        print("My money :", self.nowMoney)

    def menu(self):
        print("\nMenu for " + self.name)
        print("--------------------------------------------")
        print('1.I got a money / Receive a Salary')
        print('2.I want to pay')
        print('3.Check my money detail')
        print('4.Good Bye,Please clear my stat')
        print("--------------------------------------------")
        choice = int(input("Enter your choice : "))
        print("--------------------------------------------")
        if choice == 1:
            got = float(input("Insert income : "))
            self.receive(got)
        elif choice == 2:
            use = float(input("Pay : "))
            self.pay(use)
        elif choice == 3:
            self.printstatmoney()
        else:
            print("This program have only 3 menus. Please check your input types.")
        print("--------------------------------------------")


Person1 = Employee(str(input("Welcome. What's your name ? : ")))

while 1:
    Person1.menu()
