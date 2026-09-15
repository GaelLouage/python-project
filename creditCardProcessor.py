import re
from interfaces import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
 def __init__(self):
 # TODO
     pass

 @property
 def supported_currencies(self) -> set[str]:
 # TODO
    pass
 
 def process(self, request: PaymentRequest) -> PaymentResult:
 # TODO
    pass

 def refund(self, transaction_id: str) -> bool:
 # TODO
    pass
 
