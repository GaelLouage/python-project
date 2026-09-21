from checkout import CheckoutService
from interfaces import PaymentProcessor, PaymentRequest, PaymentResult

#to create a list in python
paymentRequests: list[PaymentRequest] =[]
paymentRequests.append(PaymentRequest("1",5.4,"€","test@hotmail.com"))
paymentRequests.append(PaymentRequest("2",585.4,"€","test2@hotmail.com"))
paymentRequests.append(PaymentRequest("3",9845.4,"€","test3@hotmail.com"))



try:
  
  checkoutService = CheckoutService(paymentRequests)
  checkoutServiceResult = checkoutService.pay("PAYPAL",paymentRequests[0])
  refundResult = checkoutService.refund("PAYPAL",PaymentRequest("2",5.4,"€","test@hotmail.com"))
  print(checkoutServiceResult.message)
  print(refundResult)

except NameError:
  
  print(F"An exception occurred {NameError}")


