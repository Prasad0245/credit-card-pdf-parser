import re

def parse_hdfc(text):
    return {
        "card_holder_name": _find(text, r"Name:\s*(.*)"),
        "card_last_4": _find(text, r"XXXX XXXX XXXX (\d{4})"),
        "billing_period": _find(text, r"Statement Period:\s*(.*)"),
        "payment_due_date": _find(text, r"Payment Due Date:\s*(.*)"),
        "total_amount_due": _find_amount(text)
    }

def _find(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def _find_amount(text):
    match = re.search(
        r"Total Amount Due\s*[:₹ ]*\s*([\d,\.]+)",
        text,
        re.IGNORECASE
    )
    return match.group(1) if match else None
