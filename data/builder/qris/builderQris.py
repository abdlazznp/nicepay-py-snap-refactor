class Qris:
    def __init__(self,
                 merchantId,
                 partnerReferenceNo,
                 storeId,
                 validityPeriod,
                 amount,
                 additionalInfo):
        self.merchantId = merchantId
        self.partnerReferenceNo = partnerReferenceNo
        self.storeId = storeId
        self.validityPeriod = validityPeriod
        self.amount = amount
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "merchantId": self.merchantId,
            "partnerReferenceNo": self.partnerReferenceNo,
            "storeId": self.storeId,
            "validityPeriod": self.validityPeriod,
            "amount": self.amount,
            "additionalInfo": self.additionalInfo
        })


class BuilderQris:
    def __init__(self):
        self.merchantId = None
        self.partnerReferenceNo = None
        self.storeId = None
        self.validityPeriod = None
        self.amount = None
        self.additionalInfo = None

    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        return self

    def setPartnerReferenceNo(self, partnerReferenceNo):
        self.partnerReferenceNo = partnerReferenceNo
        return self

    def setStoreId(self, storeId):
        self.storeId = storeId
        return self

    def setValidityPeriod(self, validityPeriod):
        self.validityPeriod = validityPeriod
        return self

    def setAmount(self, amount):
        self.amount = amount
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildQris(BuilderQris):
    def build(self):
        return Qris(
            self.merchantId,
            self.partnerReferenceNo,
            self.storeId,
            self.validityPeriod,
            self.amount,
            self.additionalInfo
        )
