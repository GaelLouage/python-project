class PaymentError(Exception):
 pass

class InvalidPaymentRequest(PaymentError):
 pass

class PaymentProcessingError(PaymentError):
 pass

class UnsupportedCurrency(PaymentError):
 pass