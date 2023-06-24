from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.qris import builderQrisInquiry
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testQrisInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    additionalInfo = {

    }

    bodyQrisInquiry = (
        builderQrisInquiry.BuildQrisInquiry()
        .setMerchantId("IONPAYTEST")
        .setExternalStoreId("NICEPAY")
        .setOriginalReferenceNo("IONPAYTEST08202306241053146865")
        .setOriginalPartnerReferenceNo("OrdNo20230624105312")
        .setServiceCode("51")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.toString(),
                                            bodyQrisInquiry.toString(),
                                            ConstantsEndpoints.inquiryQris())
