class QrisRefund:
    def __init__(self,
                 merchantId,
                 externalStoreId,
                 originalReferenceNo,
                 originalPartnerReferenceNo,
                 partnerRefundNo,
                 refundAmount,
                 reason,
                 additionalInfo):
        self.merchantId = merchantId
        self.externalStoreId = externalStoreId
        self.originalReferenceNo = originalReferenceNo
        self.originalPartnerReferenceNo = originalPartnerReferenceNo
        self.partnerRefundNo = partnerRefundNo
        self.refundAmount = refundAmount
        self.reason = reason
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "merchantId": self.merchantId,
            "externalStoreId": self.externalStoreId,
            "originalReferenceNo": self.originalReferenceNo,
            "originalPartnerReferenceNo": self.originalPartnerReferenceNo,
            "partnerRefundNo": self.partnerRefundNo,
            "refundAmount": self.refundAmount,
            "reason": self.reason,
            "additionalInfo": self.additionalInfo
        })


class BuilderQrisRefund:
    def __init__(self):
        self.merchantId = None
        self.externalStoreId = None
        self.originalReferenceNo = None
        self.originalPartnerReferenceNo = None
        self.partnerRefundNo = None
        self.refundAmount = None
        self.reason = None
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

    def setPartnerRefundNo(self, partnerRefundNo):
        self.partnerRefundNo = partnerRefundNo
        return self

    def setRefundAmount(self, refundAmount):
        self.refundAmount = refundAmount
        return self

    def setReason(self, reason):
        self.reason = reason
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildQrisRefund(BuilderQrisRefund):
    def build(self):
        return QrisRefund(
            self.merchantId,
            self.externalStoreId,
            self.originalReferenceNo,
            self.originalPartnerReferenceNo,
            self.partnerRefundNo,
            self.refundAmount,
            self.reason,
            self.additionalInfo
        )
