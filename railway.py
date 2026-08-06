trains = [
    {
        "Train Number": 101,
        "Route": "Chennai - Bangalore",
        "Total Seats": 500,
        "Booked Seats": 450,
        "Waiting List": 60,
        "Ticket Fare": 650,
        "Cancellation": 20,
        "Distance": 360
    },
    {
        "Train Number": 102,
        "Route": "Chennai - Madurai",
        "Total Seats": 600,
        "Booked Seats": 280,
        "Waiting List": 15,
        "Ticket Fare": 550,
        "Cancellation": 10,
        "Distance": 460
    },
    {
        "Train Number": 103,
        "Route": "Coimbatore - Chennai",
        "Total Seats": 450,
        "Booked Seats": 430,
        "Waiting List": 80,
        "Ticket Fare": 750,
        "Cancellation": 15,
        "Distance": 500
    },
    {
        "Train Number": 104,
        "Route": "Trichy - Chennai",
        "Total Seats": 400,
        "Booked Seats": 180,
        "Waiting List": 5,
        "Ticket Fare": 450,
        "Cancellation": 8,
        "Distance": 330
    },
    {
        "Train Number": 105,
        "Route": "Salem - Chennai",
        "Total Seats": 350,
        "Booked Seats": 330,
        "Waiting List": 35,
        "Ticket Fare": 500,
        "Cancellation": 12,
        "Distance": 340
    }
]

print("\n========== RAILWAY ANALYTICS REPORT ==========")

for train in trains:

    occupancy = (train["Booked Seats"] / train["Total Seats"]) * 100

    actual_revenue = (train["Booked Seats"] - train["Cancellation"]) * train["Ticket Fare"]

    revenue_per_km = actual_revenue / train["Distance"]

    train["Occupancy"] = occupancy
    train["Revenue"] = actual_revenue
    train["RevenuePerKM"] = revenue_per_km

    print("\nTrain Number :", train["Train Number"])
    print("Route :", train["Route"])
    print("Occupancy Ratio : {:.2f}%".format(occupancy))
    print("Actual Revenue : ₹", actual_revenue)
    print("Revenue per KM : ₹{:.2f}".format(revenue_per_km))

    if train["Waiting List"] > 30:
        print("Status : High Demand Train")

    if train["Booked Seats"] > train["Total Seats"]:
        print("Status : Overbooked")

print("\n----- Trains with Occupancy Below 50% -----")
for train in trains:
    if train["Occupancy"] < 50:
        print(train["Route"], "-", "{:.2f}%".format(train["Occupancy"]))

max_train = max(trains, key=lambda x: x["Revenue"])

print("\nRoute with Maximum Revenue")
print(max_train["Route"], "₹", max_train["Revenue"])

trains.sort(key=lambda x: x["Revenue"], reverse=True)

print("\n----- Trains Sorted by Revenue -----")
for train in trains:
    print(train["Route"], "₹", train["Revenue"])

# Generate report

with open("railway_report.txt", "w") as file:

    file.write("SMART RAILWAY RESERVATION REPORT\n\n")

    for train in trains:
        file.write(
            f"{train['Train Number']} | "
            f"{train['Route']} | "
            f"Revenue = ₹{train['Revenue']} | "
            f"Occupancy = {train['Occupancy']:.2f}%\n"
        )

print("\nReport Generated Successfully.")

print("\nReading Report File...\n")

with open("railway_report.txt", "r") as file:
    print(file.read())

print("Top Three Revenue Generating Trains")

for train in trains[:3]:
    print(train["Route"], "₹", train["Revenue"])
