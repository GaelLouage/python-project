import re

from interfaces import PaymentProcessor
from mapper import Mapper
from helpers import Helpers
from exceptions import InvalidPaymentRequest
from models import RefundRequest,PaymentRequest

class PayPalProcessor(PaymentProcessor):
 def __init__(self):
   pass
 
 @property
 def supported_currencies(self) -> set[str]:
    pass
 
 def process(self, request: PaymentRequest) -> PaymentResult:
   #implement logic
 # validation has bo set in exceptions or seperated method
         valid, message = Helpers.validation(request)
         if not valid:
            raise InvalidPaymentRequest(message)

        
         mapToResult = Mapper.payment_request_mapper(request)
         return mapToResult

 
 def refund(self, request: RefundRequest) -> bool:
     valid, message = Helpers.validation(request)
     if not valid:
           raise InvalidPaymentRequest(message)

      
     
     return True
 