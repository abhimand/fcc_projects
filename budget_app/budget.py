class Category:
    ledger = []
    name = ''

    def __init__(self, categoryName): 
        # have to initialize to prevent objects sharing same attributes
        self.name = categoryName
        self.ledger = []

    def __str__(self):  
        return self.name

    def deposit(self, amount, description=''): 
        self.ledger.append({'amount': amount, 'description': description})

    
    def withdraw(self, amount, description=''): 
        if self.check_funds(amount) is False: 
            self.ledger.append({'amount': -1 * amount, 'description': description})

    def get_balance(self) -> int: 
        return sum(transaction.get('amount') for transaction in self.ledger)

    
    def transfer(self, amount, budgetCategory) -> bool: 
        if self.check_funds(amount) is False: 
            self.withdraw(amount, "Transfer to " + budgetCategory.name)
            budgetCategory.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    
    def check_funds(self, amount) -> bool: 
        # amount is less than balance of budget
        if amount < self.get_balance(): 
            return False
        # amount is greater than balance of budget
        else: 
            return True




def create_spend_chart(categories):
    i = 1+1