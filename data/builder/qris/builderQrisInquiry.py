class QrisInquiry:
    def __init__(self,
                 merchantId,
                 externalStoreId,
                 originalReferenceNo,
                 originalPartnerReferenceNo,
                 serviceCode,
                 additionalInfo):
        self.merchantId = merchantId
        self.externalStoreId = externalStoreId
        self.originalReferenceNo = originalReferenceNo
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        self.serviceCode = serviceCode
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "merchantId": self.merchantId,
            "externalStoreId": self.externalStoreId,
            "originalReferenceNo": self.originalReferenceNo,
            "originalPartnerReferenceNo": self.originalPartnerReferenceNo,
            "serviceCode": self.serviceCode,
            "additionalInfo": self.additionalInfo
        })


class BuilderQrisInquiry:
    def __init__(self):
        self.merchantId = None
        self.externalStoreId = None
        self.originalReferenceNo = None
        self.originalPartnerReferenceNo = None
        self.serviceCode = None
        self.additionalInfo = None

    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        return self

    def setExternalStoreId(self, externalStoreId):
        self.externalStoreId = externalStoreId
        return self

    def setOriginalReferenceNo(self, originalReferenceNo):
        self.originalReferenceNo = originalReferenceNo
        return self

    def setOriginalPartnerReferenceNo(self, originalPartnerReferenceNo):
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        return self

    def setServiceCode(self, serviceCode):
        self.serviceCode = serviceCode
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildQrisInquiry(BuilderQrisInquiry):
    def build(self):
        return QrisInquiry(
            self.merchantId,
            self.externalStoreId,
            self.originalReferenceNo,
            self.originalPartnerReferenceNo,
            self.serviceCode,
            self.additionalInfo
        )
