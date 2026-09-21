from models import PaymentRequest, PaymentResult, RefundRequest
from interfaces import PaymentProcessor
from exceptions import PaymentError, InvalidPaymentRequest
from payments import Payments
from helpers import Helpers

import re

class CheckoutService:
 def __init__(self, paymentsRequests:list[PaymentRequest]):
        self.paymentsRequests = paymentsRequests


 
 def pay(
 self,
 processor_name: str,
 request: PaymentRequest,
 ) -> PaymentResult:   
      value, message = Helpers.orderId_validation(self.paymentsRequests, request)
      if not value:
            raise InvalidPaymentRequest(message)

      return Payments.GetPaymentType(processor_name).process(request)

        

 
 def refund(
 self,
 processor_name: str,
 request: RefundRequest,
 ) -> bool:
      value, message = Helpers.orderId_validation(self.paymentsRequests, request)
      if not value:
            raise InvalidPaymentRequest(message)


      return Payments.GetPaymentType(processor_name).refund(request)




