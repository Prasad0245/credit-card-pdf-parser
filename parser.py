from utils.pdf_reader import extract_text
from utils.issuer_detector import detect_issuer

from issuers.hdfc import parse_hdfc
from issuers.icici import parse_icici
from issuers.sbi import parse_sbi
from issuers.axis import parse_axis
from issuers.amex import parse_amex

import json
import sys


def parse_statement(pdf_path):
    text = extract_text(pdf_path)
    issuer = detect_issuer(text)

    if issuer == "HDFC":
        data = parse_hdfc(text)
    elif issuer == "ICICI":
        data = parse_icici(text)
    elif issuer == "SBI":
        data = parse_sbi(text)
    elif issuer == "AXIS":
        data = parse_axis(text)
    elif issuer == "AMEX":
        data = parse_amex(text)
    else:
        raise Exception("Unsupported Credit Card Issuer")

    data["issuer"] = issuer
    return data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <statement.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    result = parse_statement(pdf_path)

    print(json.dumps(result, indent=4))
