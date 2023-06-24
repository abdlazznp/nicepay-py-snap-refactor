class PayoutCancel:
    def __init__(self,
                 originalPartnerReferenceNo,
                 originalReferenceNo,
                 merchantId):
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        self.originalReferenceNo = originalReferenceNo
        self.merchantId = merchantId

    def toString(self):
        return ({
            "originalPartnerReferenceNo": self.originalPartnerReferenceNo,
            "originalReferenceNo": self.originalReferenceNo,
            "merchantId": self.merchantId
        })


class BuilderPayoutCancel:
    def __init__(self):
        self.originalPartnerReferenceNo = None
        self.originalReferenceNo = None
        self.merchantId = None

    def setOriginalPartnerReferenceNo(self, originalPartnerReferenceNo):
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        return self

    def setOriginalReferenceNo(self, originalReferenceNo):
        self.originalReferenceNo = originalReferenceNo
        return self

    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        return self


class BuildPayoutCancel(BuilderPayoutCancel):
    def build(self):
        return PayoutCancel(
            self.originalPartnerReferenceNo,
            self.originalReferenceNo,
            self.merchantId
        )
