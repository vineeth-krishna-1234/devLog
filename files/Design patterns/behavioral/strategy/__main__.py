from abc import ABC, abstractmethod


class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @abstractmethod
    def make_payment(self):
        pass


class CreditCard(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def make_payment(self):
        print(f"Paid {self.amount} {self.currency} using credit card")


class PayPal(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def make_payment(self):
        print(f"Paid {self.amount} {self.currency} using Paypal")


class BankTransfer(Payment):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def make_payment(self):
        print(f"Paid {self.amount} {self.currency} using Bank Transfer")


class Purchase:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def pay(self):
        self.payment_method.make_payment()

    def view_bill(self):
        print("Your bill:")


if __name__ == "__main__":
    new_purchase = Purchase(payment_method=PayPal(amount=100, currency="USD"))
    new_purchase.pay()
