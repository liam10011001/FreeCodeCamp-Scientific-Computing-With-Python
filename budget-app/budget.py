class Category:

    def __init__(self, title):
        self.__title = title
        self.ledger = list()

    def get_title(self):
        return self.__title

    def get_withdraws(self):
        newLedger = []
        for transaction in self.ledger:
            if transaction["amount"] < 0:
                newLedger.append({"amount": (-1 * transaction["amount"]), "description": transaction["description"]})
        return newLedger

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": (-1 * amount), "description": desc})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance  += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.get_title())
            category.deposit(amount, "Transfer from " + self.get_title())
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
        
    def __str__(self):
        display = ""
        name_index = 15 - int(len(self.get_title())/2)
        for i in range(name_index):
            display += "*"
        display += self.get_title()
        index = name_index + len(self.get_title())
        for i in range(index, 30):
            display += "*"
        display += "\n"
        
        for transaction in self.ledger:
            desc = transaction["description"]
            amount = transaction["amount"]
            if len(desc) >= 23:
                display += desc[:23]
            else:
                display += desc
                for i in range(23 - len(desc)):
                    display += " "
                    
            amount_index = 7 - len("{amount:.2f}".format(amount=amount))
            for i in range(amount_index):
                display += " "
            display += "{amount:.2f}".format(amount=amount)
            display += "\n"

        display = display + "Total: " + "{total:.2f}".format(total=self.get_balance())
        return display


def longest_category(categories):
    maxLen = 0
    for c in categories:
        if len(c.get_title()) > maxLen:
            maxLen = len(c.get_title())
    return maxLen


def create_spend_chart(categories):
    spending = []
    totalSpending = 0
    for category in categories:
        withdraws = category.get_withdraws()
        total = 0
        for w in withdraws:
            total += w["amount"]
        spending.append({"Category": category.get_title(), "Amount": total})
        totalSpending += total

    for s in spending:
        percent = (s["Amount"] / totalSpending) * 100
        s["Percentage"] = int(percent / 10) * 10 # rounded down to the nearest 10

    display = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        if i == 100:
            display = display + str(i) + "| "
        elif i < 100 and i > 0:
            display = display + " " + str(i) + "| "
        else:
            display = display + "  " + str(i) + "| "
        for s in spending:
            if s["Percentage"] >= i:
                display += "o"
            else:
                display += " "
            display += "  "
        display += "\n"

    display += "    " #  4 space for 3 digits and (|) character
    display += "-"
    for i in range(len(spending)):
        display += "---" # 1 for name and 2 to seperate
    display += "\n"

    maxLen = longest_category(categories)
    
    for i in range(maxLen):
        display += "     " # 5 space
        for s in spending:
            if i < len(s["Category"]):
                display += s["Category"][i]
            else:
                display += " "
                    
            display += "  "
        if i < maxLen -1:
            display += "\n"
    return display


if __name__=="__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    

    print(food)
    print(clothing)
    print(create_spend_chart([food, clothing]))

