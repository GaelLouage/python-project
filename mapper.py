import re
from models import PaymentResult, PaymentRequest, PaymentStatus

class Mapper:
    @staticmethod
    def payment_request_mapper(request: PaymentRequest) -> PaymentResult:
        return PaymentResult(
            status=PaymentStatus.SUCCESS,
            transaction_id=request.order_id,
            message=f"order_id {request.order_id}\nstatus: {PaymentStatus.SUCCESS}"
        )
