from data.builder.snap import builderAccessToken
from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.virtualAccount import builderVirtualAccountInquiry
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()


class testVirtualAccountInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    totalAmount = {"value": "10000.00",
                   "currency": "IDR"
                   }

    additionalInfo = {"tXidVA": "IONPAYTEST02202306232221286791"
                      }

    bodyInquiryVA = (
        builderVirtualAccountInquiry.BuildInquiryVA()
        .setPartnerServiceId("")
        .setCustomerNo("")
        .setVirtualAccountNo("111111102221286791")
        .setInquiryRequestId("")
        .setTotalAmount(totalAmount)
        .setTrxId("IONPAYTEST1348844834384834")
        .setAdditionalInfo(additionalInfo)
        .build()
    )
    result = SnapService.serviceTransaction(bodyCreateToken.toString(),
                                            bodyInquiryVA.toString(),
                                            ConstantsEndpoints.inquiryVA())
