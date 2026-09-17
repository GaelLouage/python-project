from models import PaymentRequest, PaymentResult, PaymentStatus
from interfaces import PaymentProcessor
from helpers import Helpers
from mapper import Mapper

from payPalProcessor import PayPalProcessor

from creditCardProcessor import CreditCardProcessor
from  bankTransferProcessor import BankTransferProcessor

from exceptions import (
 InvalidPaymentRequest,
 PaymentProcessingError,
 UnsupportedCurrency,
 PaymentError
)



class Payments:
    def GetPaymentType(payemntMethod:str) -> PaymentProcessor :
                  match payemntMethod:
                             case "PAYPAL":
                                 return PayPalProcessor()
                             case "CreditCard":
                                 return CreditCardProcessor()
                             case _:
                                 return BankTransferProcessor()
