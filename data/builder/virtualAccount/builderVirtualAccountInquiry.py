class InquiryVA:
    def __init__(self,
                 partnerServiceId,
                 customerNo,
                 virtualAccountNo,
                 inquiryRequestId,
                 totalAmount,
                 trxId,
                 additionalInfo):
        self.partnerServiceId = partnerServiceId
        self.customerNo = customerNo
        self.virtualAccountNo = virtualAccountNo
        self.inquiryRequestId = inquiryRequestId
        self.totalAmount = totalAmount
        self.trxId = trxId
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "partnerServiceId": self.partnerServiceId,
            "customerNo": self.customerNo,
            "virtualAccountNo": self.virtualAccountNo,
            "inquiryRequestId": self.inquiryRequestId,
            "totalAmount": self.totalAmount,
            "trxId": self.trxId,
            "additionalInfo": self.additionalInfo
        })


class BuilderInquiryVA:
    def __init__(self):
        self.partnerServiceId = None
        self.customerNo = None
        self.virtualAccountNo = None
        self.inquiryRequestId = None
        self.totalAmount = None
        self.trxId = None
        self.additionalInfo = None

    def setPartnerServiceId(self, partnerServiceId):
        self.partnerServiceId = partnerServiceId
        return self

    def setCustomerNo(self, customerNo):
        self.customerNo = customerNo
        return self

    def setVirtualAccountNo(self, virtualAccountNo):
        self.virtualAccountNo = virtualAccountNo
        return self

    def setInquiryRequestId(self, inquiryRequestId):
        self.inquiryRequestId = inquiryRequestId
        return self

    def setTotalAmount(self, totalAmount):
        self.totalAmount = totalAmount
        return self

    def setTrxId(self, trxId):
        self.trxId = trxId
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self


class BuildInquiryVA(BuilderInquiryVA):
    def build(self):
        return InquiryVA(
            self.partnerServiceId,
            self.customerNo,
            self.virtualAccountNo,
            self.inquiryRequestId,
            self.totalAmount,
            self.trxId,
            self.additionalInfo
        )
