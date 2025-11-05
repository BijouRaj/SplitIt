from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List 
from models.bill import Bill 
from models.item import Item 
from models.person import Person 

app = FastAPI(title= "SplitIt API") 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # later replace with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bills = {} 
items = [] 
people = []

@app.get("/")
def root():
    return {"message": "SplitIt API running"}

@app.post("/upload-receipt")
async def upload_receipt(file: UploadFile = File(...)):
    mock_items = [
        {"name": "Fish", "price": 10.0},
        {"name": "Chicken", "price": 19.84}
    ]
    return {"items": mock_items}

@app.post("/create-bill")
async def create_bill(
    overall: float = Form(...),
    subtotal: float = Form(...),
    tax: float = Form(...),
    tip: float = Form(...)
):
    bill = Bill(overall, subtotal, tax, tip)
    bills["current"] = bill
    return {"message": "bill created", "tip_amount": bill.tipCost}

@app.post("/add-people")
async def add_people(names: List[str]):
    if "current" not in bills:
        return {"error": "No bill found"}
    global people 
    people = [Person(name, bills["current"]) for name in names]
    return {"message": "people added successfully", "people": [p.name for p in people]}

@app.post("/assign-items")
async def assign_items(assignments: List[dict]):
    if not people:
        return {"error": "no people found"}
    for assignment in assignments:
        person_name = assignment["person"]
        item = Item(assignment["item"], float(assignment["price"]))
        match = next((p for p in people if p.name == person_name), None)
        if match:
            match.addItem(item)
    response = [
        {"name": p.name, "subtotal": round(p.bill, 2)} for p in people
    ]
    return {"assigned": response}

@app.get("/final-totals")
def final_totals():
    if not people:
        return {"error": "no people"}
    results = []
    for p in people:
        p.final()
        results.append({
            "name": p.name,
            "items": list(p.order.keys()),
            "subtotal": round(p.bill, 2),
            "total_with_tax_tip": round(p.myTotal, 2)
        })
    return {"totals": results}