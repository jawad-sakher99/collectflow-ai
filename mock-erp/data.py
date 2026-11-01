DATA = {
    "alpha": {
        "name": "Alpha Distribution",
        "customers": [
            {"id": "C-001", "name": "Al Noor Supermarket", "email": "accounts@alnoor.example"},
            {"id": "C-002", "name": "Green Valley Grocers", "email": "billing@greenvalley.example"},
        ],
        "invoices": [
            {"id": "INV-1001", "customer_id": "C-001", "issue_date": "2026-08-01", "due_date": "2026-08-31", "amount": "1200.00", "currency": "USD"},
            {"id": "INV-1002", "customer_id": "C-001", "issue_date": "2026-08-10", "due_date": "2026-09-09", "amount": "800.00", "currency": "USD"},
            {"id": "INV-1004", "customer_id": "C-002", "issue_date": "2026-08-15", "due_date": "2026-09-14", "amount": "450.50", "currency": "USD"},
            {"id": "INV-1005", "customer_id": "C-002", "issue_date": "2026-08-20", "due_date": "2026-09-19", "amount": "300.00", "currency": "USD"},
            {"id": "INV-1006", "customer_id": "C-002", "issue_date": "2026-08-20", "due_date": "2026-09-19", "amount": "300.00", "currency": "USD"},
        ],
        "payments": [
            {"id": "PAY-001", "customer_id": "C-001", "date": "2026-09-01", "amount": "1200.00", "currency": "USD", "reference": "INV-1001"},
            {"id": "PAY-002", "customer_id": "C-001", "date": "2026-09-15", "amount": "300.00", "currency": "USD", "reference": "INV-1002"},
            {"id": "PAY-003", "customer_id": "C-002", "date": "2026-09-20", "amount": "750.50", "currency": "USD", "reference": "INV-1004 INV-1005"},
            {"id": "PAY-004", "customer_id": "C-002", "date": "2026-10-05", "amount": "300.00", "currency": "USD", "reference": ""},
        ],
        "allocations": [
            {"payment_id": "PAY-001", "invoice_id": "INV-1001", "amount": "1200.00"},
            {"payment_id": "PAY-002", "invoice_id": "INV-1002", "amount": "300.00"},
            {"payment_id": "PAY-003", "invoice_id": "INV-1004", "amount": "450.50"},
            {"payment_id": "PAY-003", "invoice_id": "INV-1005", "amount": "300.00"},
        ],
    },
    "beta": {
        "name": "Beta Wholesale",
        "customers": [
            {"id": "C-101", "name": "City Mart", "email": "finance@citymart.example"},
        ],
        "invoices": [
            {"id": "B-2001", "customer_id": "C-101", "issue_date": "2026-09-01", "due_date": "2026-10-01", "amount": "2500.00", "currency": "EUR"},
            {"id": "B-2002", "customer_id": "C-101", "issue_date": "2026-09-10", "due_date": "2026-10-10", "amount": "1500.00", "currency": "EUR"},
        ],
        "payments": [
            {"id": "BPAY-001", "customer_id": "C-101", "date": "2026-10-02", "amount": "2500.00", "currency": "EUR", "reference": "B-2001"},
        ],
        "allocations": [
            {"payment_id": "BPAY-001", "invoice_id": "B-2001", "amount": "2500.00"},
        ],
    },
}   