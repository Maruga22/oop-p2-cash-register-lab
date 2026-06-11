#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Validate discount
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        """
        Adds item to register, updates total and transaction history
        """
        for _ in range(quantity):
            self.items.append(item)

        # Update total
        self.total += price * quantity

        # Store transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Applies discount to total
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply discount
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        display_total = int(self.total) if float(self.total).is_integer() else self.total
        print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        """
        Removes last transaction and adjusts total and items
        """
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        # Adjust total
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        # Remove item occurrences
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.reverse()
                self.items.remove(last_transaction["item"])
                self.items.reverse()
            
          