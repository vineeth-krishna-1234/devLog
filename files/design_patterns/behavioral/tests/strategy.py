import unittest
from io import StringIO
from contextlib import redirect_stdout
from design_patterns.behavioral.strategy import (
    CreditCard,
    Payment,
    PayPal,
    BankTransfer,
    Purchase,
)


class TestPaymentMethods(unittest.TestCase):

    def setUp(self):
        self.amount = 100
        self.currency = "USD"

    def test_credit_card_payment(self):
        payment = CreditCard(self.amount, self.currency)

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            payment.make_payment()
        output = f.getvalue().strip()

        self.assertEqual(
            output, f"Paid {self.amount} {self.currency} using credit card"
        )

    def test_paypal_payment(self):
        payment = PayPal(self.amount, self.currency)

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            payment.make_payment()
        output = f.getvalue().strip()

        self.assertEqual(output, f"Paid {self.amount} {self.currency} using Paypal")

    def test_bank_transfer_payment(self):
        payment = BankTransfer(self.amount, self.currency)

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            payment.make_payment()
        output = f.getvalue().strip()

        self.assertEqual(
            output, f"Paid {self.amount} {self.currency} using Bank Transfer"
        )

    def test_purchase_with_credit_card(self):
        payment_method = CreditCard(self.amount, self.currency)
        purchase = Purchase(payment_method)

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            purchase.pay()
        output = f.getvalue().strip()

        self.assertEqual(
            output, f"Paid {self.amount} {self.currency} using credit card"
        )

    def test_purchase_with_paypal(self):
        payment_method = PayPal(self.amount, self.currency)
        purchase = Purchase(payment_method)

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            purchase.pay()
        output = f.getvalue().strip()

        self.assertEqual(output, f"Paid {self.amount} {self.currency} using Paypal")

    def test_purchase_with_bank_transfer(self):
        payment_method = BankTransfer(self.amount, self.currency)
        purchase = Purchase(payment_method)

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            purchase.pay()
        output = f.getvalue().strip()

        self.assertEqual(
            output, f"Paid {self.amount} {self.currency} using Bank Transfer"
        )

    def test_change_payment_method(self):
        payment_method = CreditCard(self.amount, self.currency)
        purchase = Purchase(payment_method)

        # Change to PayPal
        purchase.set_payment_method(PayPal(self.amount, self.currency))

        # Capture the print output
        f = StringIO()
        with redirect_stdout(f):
            purchase.pay()
        output = f.getvalue().strip()

        self.assertEqual(output, f"Paid {self.amount} {self.currency} using Paypal")


if __name__ == "__main__":
    unittest.main()
