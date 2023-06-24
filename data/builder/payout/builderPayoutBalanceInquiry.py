class PayoutBalanceInquiry:
    def __init__(self,
                 merchantId,
                 additionalInfo):
        self.merchantId = merchantId
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "merchantId": self.merchantId,
            "additionalInfo": self.additionalInfo
        })


class BuilderPayoutBalanceInquiry:
    def __init__(self):
        self.merchantId = None
        self.additionalInfo = None

    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildPayoutBalanceInquiry(BuilderPayoutBalanceInquiry):
    def build(self):
        return PayoutBalanceInquiry(
            self.merchantId,
            self.additionalInfo
        )
