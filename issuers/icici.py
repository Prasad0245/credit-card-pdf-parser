import re

def parse_icici(text):
    return {
        "card_holder_name": _find_name(text),
        "card_last_4": _find(text, r"\d{4}XXXXXXXX(\d{4})"),
        "billing_period": _find(text, r"Statement period\s*:\s*(.*)"),
        "payment_due_date": _find(text, r"PAYMENT DUE DATE\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})"),
        "total_amount_due": _find_amount(text)
    }

def _find_name(text):
    match = re.search(r"MR\s+([A-Z ]+)\n", text)
    return match.group(1).strip() if match else None

def _find(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def _find_amount(text):
    match = re.search(
        r"Total Amount due\s*[₹` ]*\s*([\d,\.]+)",
        text,
        re.IGNORECASE
    )
    return match.group(1) if match else None
