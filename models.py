from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

class PaymentStatus(Enum):
 PENDING = "pending"
 SUCCESS = "success"
 FAILED = "failed"

@dataclass
class PaymentRequest:
 order_id: str
 amount: Decimal
 currency: str
 customer_email: str
 
@dataclass
class PaymentResult:
 status: PaymentStatus
 transaction_id: str | None = None
 message: str | None = None


@dataclass
class RefundRequest:
 order_id: str
 amount: Decimal
 currency: str
 customer_email: str