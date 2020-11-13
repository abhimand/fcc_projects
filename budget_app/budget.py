class Category:
    ledger = []
    name = ''
    withdrawAmt = 0

    def __init__(self, categoryName): 
        # have to initialize to prevent objects sharing same attributes
        self.name = categoryName
        self.ledger = []
        self.withdrawAmt = 0

    def __str__(self):  
        # build first line with star centered name
        string = self.name.center(30, '*') + '\n'
        # list all transactions in ledger
        for dic in self.ledger:
            # format amount to two decimal points
            num = "{:.2f}".format(dic['amount'])
            des = dic['description'].ljust(30)
            amt = str(num).rjust(30)
            lenAmt = 30 - len(str(num))
            string += des[0:lenAmt - 1] + ' ' + amt[lenAmt:30] + '\n'
        string += 'Total: ' + str(self.get_balance())
        return string

    # add amount and description to ledger
    def deposit(self, amount, description=''): 
        self.ledger.append({'amount': amount, 'description': description})

    # add withdrawal to ledger, but with negative attached
    # check if we have enough money to do withdrawl
    def withdraw(self, amount, description=''): 
        if self.check_funds(amount) is True: 
            self.withdrawAmt += amount
            self.ledger.append({'amount': -1 * amount, 'description': description})
            return True
        return False

    # how much money do we have?
    def get_balance(self) -> int: 
        return sum(transaction.get('amount') for transaction in self.ledger)
    
    # transfer from one category to another
    def transfer(self, amount, budgetCategory) -> bool: 
        if self.check_funds(amount) is True: 
            self.withdraw(amount, "Transfer to " + budgetCategory.name)
            budgetCategory.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    
    def check_funds(self, amount) -> bool: 
        # if amount is less than balance of budget return 
        return amount <= self.get_balance()

def create_spend_chart(categories):
    # first line
    line = 'Percentage spent by category\n'
    # calculate percentages and create dictionary
    withdrawTotal = sum(cat.withdrawAmt for cat in categories)
    percentages = []
    for cat in categories:
        percentage = (cat.withdrawAmt/withdrawTotal) * 100
        percentages.append(percentage)
    # build graph
    num = 100
    while num != -10:
        # add vertical line
        line += str(num) + '| '
        # for each category percentage in the cat dictionary
        for percent in percentages:
            if percent > int(num): 
                line += 'o  '
            else:
                line += '   '
        num -= 10
        # add space except for 100 which has a extra digit
        line += '\n '
        # add a extra space if 0 for margin adjusting
        if num == 0: 
            line += ' '

    # might need to adjust
    # cut off line
    line += '   -' + '---' * len(percentages)

    # get longest string
    length = 0
    for cat in categories: 
        if len(cat.name) > length: 
            length = len(cat.name)
    # add empty space to ends of other names
    catNames = []
    for cat in categories: 
        catNames.append(cat.name.ljust(length, ' '))
    # keep putting character until end of longest string
    # put char, if no char, put space
    for index in range(length):
        line += '\n     '
        for name in catNames :
            line += name[index] + '  '
    return line
    

# expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "



    
    