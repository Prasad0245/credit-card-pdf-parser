# Credit Card Statement Parser

## Overview
A Python-based PDF parser that extracts key information from credit card statements across multiple issuers.  
The solution is designed to handle real-world PDF layouts using issuer-specific parsing logic.

---

## Supported Issuers
- HDFC Bank  
- ICICI Bank  
- SBI Card  
- Axis Bank  
- American Express  

---

## Extracted Fields
- Card Holder Name  
- Card Last 4 Digits  
- Billing Period  
- Payment Due Date  
- Total Amount Due  

---

## Tech Stack
- Python 3  
- pdfplumber  
- Regex  

---

## How to Run
```bash
pip install -r requirements.txt
python parser.py samples/icici.pdf
