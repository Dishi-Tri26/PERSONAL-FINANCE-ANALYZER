import csv
from expense_manager import DATA_FILE, ensure_file

def analyze():
    ensure_file()
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    total = 0
    categories = {}
    for row in rows:
        amount = float(row["amount"])
        total += amount
        category = row["category"]
        categories[category] = categories.get(category, 0) + amount

    highest = max(categories, key=categories.get) if categories else None
    return {"total": total, "categories": categories, "highest": highest, "count": len(rows)}
