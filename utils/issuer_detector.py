def detect_issuer(text):
    text = text.upper()

    if "HDFC BANK" in text:
        return "HDFC"
    elif "ICICI BANK" in text:
        return "ICICI"
    elif "SBI CARD" in text:
        return "SBI"
    elif "AXIS BANK" in text:
        return "AXIS"
    elif "AMERICAN EXPRESS" in text:
        return "AMEX"
    else:
        return "UNKNOWN"
