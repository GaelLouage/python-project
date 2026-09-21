import re
from interfaces import PaymentProcessor
from models import PaymentRequest

class Helpers:
    @staticmethod
    def valid_email(email):
        return bool(re.search(r"^[\w.+-]+@[\w]+\.[a-z]{2,3}$", email))


    def validation(request: PaymentRequest) -> tuple[bool, str]:
        if not request.order_id.strip():
            return False, "Order ID cannot be empty or contain only whitespaces!"

        if not Helpers.valid_email(request.customer_email):
             return False, "Invalid customer email!"

        if request.amount <= 0:
             return False, "Amount has to be bigger than 0."

        if not request.currency.strip():
         return False, "Currency cannot be empty!"

          

        return True, "Success"


    def orderId_validation(paymentsRequests:list[PaymentRequest], request:PaymentRequest) -> tuple[bool, str]:
        for payment in paymentsRequests:
            if payment.order_id == request.order_id:
                      return True, "Success"


        return False, "Invalid PAYMENT order id"



    def orderId_validation(paymentsRequests:list[PaymentRequest], request:RefundRequest) -> tuple[bool, str]:
        for payment in paymentsRequests:
            if payment.order_id == request.order_id:
                      return True, "Success"

            

        return False, "Invalid REQUEST order id"

