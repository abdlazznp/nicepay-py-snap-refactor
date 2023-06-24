class DirectDebitRefund:
    def __init__(self,
                 partnerRefundNo,
                 merchantId,
                 subMerchantId,
                 originalPartnerReferenceNo,
                 originalReferenceNo,
                 externalStoreId,
                 reason,
                 refundAmount,
                 additionalInfo):
        self.partnerRefundNo = partnerRefundNo
        self.merchantId = merchantId
        self.subMerchantId = subMerchantId
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        self.originalReferenceNo = originalReferenceNo
        self.externalStoreId = externalStoreId
        self.reason = reason
        self.refundAmount = refundAmount
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "partnerRefundNo": self.partnerRefundNo,
            "merchantId": self.merchantId,
            "subMerchantId": self.subMerchantId,
            "originalPartnerReferenceNo": self.originalPartnerReferenceNo,
            "originalReferenceNo": self.originalReferenceNo,
            "externalStoreId": self.externalStoreId,
            "reason": self.reason,
            "refundAmount": self.refundAmount,
            "additionalInfo": self.additionalInfo
        })


class BuilderDirectDebitRefund:
    def __init__(self):
        self.partnerRefundNo = None
        self.merchantId = None
        self.subMerchantId = None
        self.originalPartnerReferenceNo = None
        self.originalReferenceNo = None
        self.externalStoreId = None
        self.reason = None
        self.refundAmount = None
        self.additionalInfo = None

    def setPartnerRefundNo(self, partnerRefundNo):
        self.partnerRefundNo = partnerRefundNo
        return self

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

    def setExternalStoreId(self, externalStoreId):
        self.externalStoreId = externalStoreId
        return self

    def setReason(self, reason):
        self.reason = reason
        return self

    def setRefundAmount(self, refundAmount):
        self.refundAmount = refundAmount
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildDirectDebitRefund(BuilderDirectDebitRefund):
    def build(self):
        return DirectDebitRefund(
            self.partnerRefundNo,
            self.merchantId,
            self.subMerchantId,
            self.originalPartnerReferenceNo,
            self.originalReferenceNo,
            self.externalStoreId,
            self.reason,
            self.refundAmount,
            self.additionalInfo
        )
