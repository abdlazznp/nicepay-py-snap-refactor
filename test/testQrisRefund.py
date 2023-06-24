from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.qris import builderQrisRefund
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
class testQrisRefund:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    refundAmount = {
        "value": "1000.00",
        "currency": "IDR"
    }

    additionalInfo = {
        "cancelType": "1"
    }

    bodyQrisInquiry = (
        builderQrisRefund.BuildQrisRefund()
        .setMerchantId("IONPAYTEST")
        .setExternalStoreId("NICEPAY")
        .setOriginalReferenceNo("IONPAYTEST08202306241053146865")
        .setOriginalPartnerReferenceNo("OrdNo20230624105312")
        .setPartnerRefundNo("51")
        .setRefundAmount(refundAmount)
        .setReason("Test Refund QRIS SNAP")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.toString(),
                                            bodyQrisInquiry.toString(),
                                            ConstantsEndpoints.refundQris())
    