from checkout import CheckoutService
from interfaces import PaymentProcessor, PaymentRequest, PaymentResult

#to create a list in python

paymentProcessorList: list[PaymentProcessor] = []
paymentProcessorList.append(PaymentRequest("1",5.4,"€","test@hotmail.com"))
paymentProcessorList.append(PaymentRequest("2",585.4,"€","test2@hotmail.com"))
paymentProcessorList.append(PaymentRequest("3",9845.4,"€","test3@hotmail.com"))



try:
  
  checkoutService = CheckoutService(paymentProcessorList)
  checkoutServiceResult = checkoutService.pay("PAYPAL",PaymentRequest("1",5.4,"€","test@hotmail.com"))
  refundResult = checkoutService.refund("PAYPAL",PaymentRequest("1",5.4,"€","test@hotmail.com"))
  print(checkoutServiceResult.message)
  print(refundResult)

except NameError:
  
  print(F"An exception occurred {NameError}")


