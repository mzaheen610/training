class converter:
    def __init__(self) -> None:
        pass

    def convert_inr_dollar(self,amount):
        dollarAmount = amount/83
        return dollarAmount

    def convert_dollar_inr(self,amount):
        inrAmount = amount*83
        return inrAmount

def convertCurrency(amount,currentCurrency,toCurrency):
    convert = converter()
    if currentCurrency == "INR" and toCurrency == "USD":
        print("Converted value:",convert.convert_inr_dollar(amount), toCurrency)
    elif currentCurrency == "USD" and toCurrency == "INR":
        print("Converted value:",convert.convert_dollar_inr(amount), toCurrency)

convertCurrency(50000,"INR","USD")
convertCurrency(500,"USD","INR")


