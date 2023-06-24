class DirectDebitInquiry:
    def __init__(self,
                 merchantId,
                 subMerchantId,
                 originalPartnerReferenceNo,
                 originalReferenceNo,
                 serviceCode,
                 transactionDate,
                 amount,
                 additionalInfo):
        self.merchantId = merchantId
        self.subMerchantId = subMerchantId
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        self.originalReferenceNo = originalReferenceNo
        self.serviceCode = serviceCode
        self.transactionDate = transactionDate
        self.amount = amount
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "merchantId": self.merchantId,
            "subMerchantId": self.subMerchantId,
            "originalPartnerReferenceNo": self.originalPartnerReferenceNo,
            "originalReferenceNo": self.originalReferenceNo,
            "serviceCode": self.serviceCode,
            "transactionDate": self.transactionDate,
            "amount": self.amount,
            "additionalInfo": self.additionalInfo
        })


class BuilderDirectDebitInquiry:
    def __init__(self):
        self.merchantId = None
        self.subMerchantId = None
        self.originalPartnerReferenceNo = None
        self.originalReferenceNo = None
        self.serviceCode = None
        self.transactionDate = None
        self.amount = None
        self.additionalInfo = None

    def setMerchantId(self, merchantId):
        self.merchantId = merchantId
        return self

    def setSubMerchantId(self, subMerchantId):
        self.subMerchantId = subMerchantId
        return self

    def setOriginalPartnerReferenceNo(self, originalPartnerReferenceNo):
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        return self

    def setOriginalReferenceNo(self, originalReferenceNo):
        self.originalReferenceNo = originalReferenceNo
        return self

    def setServiceCode(self, serviceCode):
        self.serviceCode = serviceCode
        return self

    def setTransactionDate(self, transactionDate):
        self.transactionDate = transactionDate
        return self

    def setAmount(self, amount):
        self.amount = amount
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildDirectDebitInquiry(BuilderDirectDebitInquiry):
    def build(self):
        return DirectDebitInquiry(
            self.merchantId,
            self.subMerchantId,
            self.originalPartnerReferenceNo,
            self.originalReferenceNo,
            self.serviceCode,
            self.transactionDate,
            self.amount,
            self.additionalInfo
        )
