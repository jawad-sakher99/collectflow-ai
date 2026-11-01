from fastapi import FastAPI, HTTPException

from data import DATA

app = FastAPI(title="Mock ERP")


def get_company(company_id: str):
    company = DATA.get(company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/companies")
def list_companies():
    return [{"id": cid, "name": c["name"]} for cid, c in DATA.items()]


@app.get("/companies/{company_id}/customers")
def list_customers(company_id: str):
    return get_company(company_id)["customers"]


@app.get("/companies/{company_id}/invoices")
def list_invoices(company_id: str):
    return get_company(company_id)["invoices"]


@app.get("/companies/{company_id}/payments")
def list_payments(company_id: str):
    return get_company(company_id)["payments"]


@app.get("/companies/{company_id}/allocations")
def list_allocations(company_id: str):
    return get_company(company_id)["allocations"]