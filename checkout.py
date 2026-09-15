from models import PaymentRequest, PaymentResult
from interfaces import PaymentProcessor
from exceptions import PaymentError, InvalidPaymentRequest
from payments import Payments
from helpers import Helpers

import re

class CheckoutService:
 def __init__(self, processors: list[PaymentProcessor]):
        self.processors = processors
    

 
 def pay(
 self,
 processor_name: str,
 request: PaymentRequest,
 ) -> PaymentResult:   
       return Payments.GetPaymentType(processor_name).process(request)

        

 
 def refund(
 self,
 processor_name: str,
 transaction_id: str,
 ) -> bool:
 # TODO
    pass




