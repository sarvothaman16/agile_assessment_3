import csv

products = [
    {
        "Product ID": 101,
        "Product Name": "Laptop",
        "Category": "Electronics",
        "Opening Stock": 100,
        "Units Sold": 60,
        "Units Returned": 5,
        "Supplier Lead Time": 7,
        "Unit Cost": 40000,
        "Selling Price": 55000,
        "Sales History": [50, 55, 60]
    },
    {
        "Product ID": 102,
        "Product Name": "Mobile",
        "Category": "Electronics",
        "Opening Stock": 120,
        "Units Sold": 90,
        "Units Returned": 4,
        "Supplier Lead Time": 5,
        "Unit Cost": 15000,
        "Selling Price": 22000,
        "Sales History": [80, 85, 90]
    },
    {
        "Product ID": 103,
        "Product Name": "Chair",
        "Category": "Furniture",
        "Opening Stock": 80,
        "Units Sold": 25,
        "Units Returned": 2,
        "Supplier Lead Time": 10,
        "Unit Cost": 1800,
        "Selling Price": 3000,
        "Sales History": [20, 22, 25]
    },
    {
        "Product ID": 104,
        "Product Name": "Table",
        "Category": "Furniture",
        "Opening Stock": 70,
        "Units Sold": 45,
        "Units Returned": 3,
        "Supplier Lead Time": 8,
        "Unit Cost": 3500,
        "Selling Price": 5500,
        "Sales History": [35, 40, 45]
    },
    {
        "Product ID": 105,
        "Product Name": "Notebook",
        "Category": "Stationery",
        "Opening Stock": 200,
        "Units Sold": 150,
        "Units Returned": 10,
        "Supplier Lead Time": 3,
        "Unit Cost": 40,
        "Selling Price": 70,
        "Sales History": [130, 140, 150]
    }
]

category_profit = {}

print("\n------ INVENTORY REPORT ------")

for p in products:

    current_stock = p["Opening Stock"] - p["Units Sold"] + p["Units Returned"]

    profit = (p["Selling Price"] - p["Unit Cost"]) * p["Units Sold"]

    turnover = p["Units Sold"] / p["Opening Stock"]

    prediction = sum(p["Sales History"]) / len(p["Sales History"])

    p["Current Stock"] = current_stock
    p["Profit"] = profit
    p["Turnover"] = turnover
    p["Prediction"] = prediction

    print("\nProduct:", p["Product Name"])
    print("Current Stock =", current_stock)
    print("Profit =", profit)
    print("Inventory Turnover =", round(turnover,2))
    print("Predicted Next Month Demand =", round(prediction))

    if current_stock < 20:
        print("** Immediate Reorder Required **")

    category_profit[p["Category"]] = category_profit.get(p["Category"],0) + profit

highest = max(products, key=lambda x:x["Profit"])

print("\nHighest Profit Product:", highest["Product Name"],
      "Profit =", highest["Profit"])

print("\nCategory Wise Profit")
for c,p in category_profit.items():
    print(c,"=",p)

products.sort(key=lambda x:x["Profit"], reverse=True)

print("\nProducts Sorted by Profit")
for p in products:
    print(p["Product Name"], ":", p["Profit"])

# Export CSV
with open("inventory_report.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Product ID","Product Name","Category","Current Stock","Profit"])

    for p in products:
        writer.writerow([
            p["Product ID"],
            p["Product Name"],
            p["Category"],
            p["Current Stock"],
            p["Profit"]
        ])

print("\nCSV File Created Successfully")

print("\nTop Five Profitable Products")

with open("inventory_report.csv","r") as file:
    reader = csv.reader(file)
    next(reader)

    rows = list(reader)

rows.sort(key=lambda x:int(x[4]), reverse=True)

for row in rows[:5]:
    print(row)
