from abc import ABC, abstractmethod
from models import PaymentRequest, PaymentResult

class PaymentProcessor(ABC):
 
 @abstractmethod
 def process(self, request: PaymentRequest) -> PaymentResult:
     pass

 @abstractmethod
 def refund(self, transaction_id: str) -> bool:
    pass
 
 @property
 @abstractmethod
 def supported_currencies(self) -> set[str]:
    pass
