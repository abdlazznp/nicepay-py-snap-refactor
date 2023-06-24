class DirectDebit:
    def __init__(self,
                 partnerReferenceNo,
                 merchantId,
                 subMerchantId,
                 externalStoreId,
                 validUpTo,
                 pointOfInitiation,
                 amount,
                 urlParam,
                 additionalInfo):
        self.partnerReferenceNo = partnerReferenceNo
        self.merchantId = merchantId
        self.subMerchantId = subMerchantId,
        self.externalStoreId = externalStoreId,
        self.validUpTo = validUpTo,
        self.pointOfInitiation = pointOfInitiation,
        self.amount = amount
        self.urlParam = urlParam
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "partnerReferenceNo": self.partnerReferenceNo,
            "merchantId": self.merchantId,
            "subMerchantId": self.subMerchantId,
            "externalStoreId":  self.externalStoreId,
            "validUpTo": self.validUpTo,
            "pointOfInitiation": self.pointOfInitiation,
            "amount": self.amount,
            "urlParam": self.urlParam,
            "additionalInfo": self.additionalInfo
        })


class BuilderDirectDebit:
    def __init__(self):
        self.partnerReferenceNo = None
        self.merchantId = None
        self.subMerchantId = None
        self.externalStoreId = None
        self.validUpTo = None
        self.pointOfInitiation = None
        self.amount = None
        self.urlParam = None
        self.additionalInfo = None

    def setPartnerReferenceNo(self, partnerReferenceNo):
        self.partnerReferenceNo = partnerReferenceNo
        return self

    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        return self

    def setSubMerchantId(self, subMerchantId):
        self.subMerchantId = subMerchantId
        return self

    def setExternalStoreId(self, externalStoreId):
        self.externalStoreId = externalStoreId
        return self

    def setValidUpTo(self, validUpTo):
        self.validUpTo = validUpTo
        return self

    def setPointOfInitiation(self, pointOfInitiation):
        self.pointOfInitiation = pointOfInitiation
        return self

    def setAmount(self, amount):
        self.amount = amount
        return self

    def setUrlParam(self, urlParam):
        self.urlParam = urlParam
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildDirectDebit(BuilderDirectDebit):
    def build(self):
        return DirectDebit(
            self.partnerReferenceNo,
            self.merchantId,
            self.subMerchantId,
            self.externalStoreId,
            self.validUpTo,
            self.pointOfInitiation,
            self.amount,
            self.urlParam,
            self.additionalInfo
        )
