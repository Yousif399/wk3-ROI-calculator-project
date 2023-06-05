class Roi():
    def __init__(self):
        pass

    
    def rent_income(self):
        income = int(input('please enter how much are you willing to rent this property ? '))
        return income

    def expenses(self):
        tax = int(input('please enter how much taxes you pay ? '))
        insurance = int(input('please enter how much insurance you pay ? '))
        vacancy = int(self.rent_income() * (5/100))
        repairs = int(input('please enter how much do you pay for repairs ? '))
        property_manager = int(input('please enter how much do you pay for property manager ? '))
        mortgage = int(input('please enter how much mortgage you pay ? '))
        total = tax + insurance +vacancy + repairs + property_manager + mortgage
        return total 
    def cash_flow(self):
        cash = self.rent_income() - self.expenses()
        #i want my annuel cash flow
        return cash * 12

    def return_on_cash(self):
        down_payment = int(input('please enter the amount of your down payment ? '))
        closing_cost = int(input('please enter the amount you paid for closing the deal ? '))
        rehab_budget = int(input('please enter the amount you paid for rehabilitation ? '))
        total_invesm = down_payment + closing_cost + rehab_budget
        roi = (self.cash_flow() / total_invesm) * 100
        if roi > 10:
            print(f'your ROI is {roi} % which is good based on the current market')
        else:
            print(f'your ROI is {roi} % which is not really good rate you need to think about it twice')
        return roi 

roi_calculator = Roi()
roi_calculator.return_on_cash()