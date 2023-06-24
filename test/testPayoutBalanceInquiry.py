from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.payout import builderPayoutBalanceInquiry
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutBalanceInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    additionalInfo = {

    }

    bodyPayoutApprove = (
        builderPayoutBalanceInquiry.BuildPayoutBalanceInquiry()
        .setMerchantId("IONPAYTEST")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.toString(),
                                            bodyPayoutApprove.toString(),
                                            ConstantsEndpoints.balanceInquiryPayout())
