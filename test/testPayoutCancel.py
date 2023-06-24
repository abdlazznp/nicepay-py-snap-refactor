from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.payout import builderPayoutCancel
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutCancel:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    bodyPayoutCancel = (
        builderPayoutCancel.BuildPayoutCancel()
        .setOriginalPartnerReferenceNo("OrdNo20230624233147")
        .setOriginalReferenceNo("IONPAYTEST07202306242331506933")
        .setMerchantId("IONPAYTEST")
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.toString(),
                                            bodyPayoutCancel.toString(),
                                            ConstantsEndpoints.cancelPayout())
