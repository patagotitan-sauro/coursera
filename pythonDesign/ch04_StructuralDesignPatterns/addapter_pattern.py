
"""
Structural Design Patterns

In the previous section, we covered creational patterns and object-oriented programming patterns that help us 
with object-creation procedures. The next category of pattern we want to present is structural design patterns.
 A structural design pattern proposes a way of composing objects to provide new functionality.

In this section, we're going to cover the following main topics:
    The adapter pattern
    The decorator pattern
    The bridge pattern
    The facade pattern
    The flyweight pattern
    The proxy pattern
"""


class OldPaymentSystem:
    def __init__(self, currency):
        self.currency = currency
    def make_payment(self, amount):
        print(f"[OLD] Pay {amount} {self.currency}")


class NewPaymentGateway:
    def __init__(self, currency):
        self.currency = currency
    def execute_payment(self, amount):
        print(f"Execute payment of {amount} {self.currency}")


