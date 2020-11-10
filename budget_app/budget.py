class Category:
    ledger = []
    name = ''

    def __init__(self, categoryName): 
        # have to initialize to prevent objects sharing same attributes
        self.name = categoryName
        self.ledger = []

    def __str__(self):  
        topLine = '*' * 30
        topLine = topLine[:15] + self.name + topLine[15:]
        start = 0 
        end = len(topLine) + 1
        while len(topLine) >= 30: 
            start += 1
            end -= 1
            topLine = topLine[start:end]
        return topLine




        


# "*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
#         ```
# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
# ```

    def deposit(self, amount, description=''): 
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''): 
        if self.check_funds(amount) is True: 
            self.ledger.append({'amount': -1 * amount, 'description': description})
            return True
        return False

    def get_balance(self) -> int: 
        return sum(transaction.get('amount') for transaction in self.ledger)
    
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
    i = 1+1