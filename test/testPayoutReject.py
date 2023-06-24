from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.payout import builderPayoutReject
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutReject:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    bodyPayoutReject = (
        builderPayoutReject.BuildPayoutReject()
        .setOriginalPartnerReferenceNo("OrdNo20230624233147")
        .setOriginalReferenceNo("IONPAYTEST07202306242331506933")
        .setMerchantId("IONPAYTEST")
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.toString(),
                                            bodyPayoutReject.toString(),
                                            ConstantsEndpoints.rejectPayout())
