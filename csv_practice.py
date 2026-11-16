
# Reflection 1:
# Python is useful for processing large amounts of data and repeating tasks
# automatically. Excel is easier for viewing data manually and making charts.
# Python can automate cleaning and organizing files, while Excel makes it easier
# to quickly inspect information and make visual changes.

# Reflection 2:
# A business could use an append-mode log to track each day's sales.
# Append mode is useful because it adds new information without deleting
# previous records, allowing the business to keep a history of its sales.

import csv
from datetime import datetime
import os

# EXERCISE 1: Setup
# Check that the sales CSV file exists.

file_path = "data/sales.csv"

if not os.path.exists(file_path):
    print("Error: sales.csv was not found.")
    exit()

print("Exercise 1: sales.csv found successfully!")


# EXERCISE 2: Read and print raw rows

print("\nEXERCISE 2: Raw CSV Rows")

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header

print("\nEXERCISE 3: Skip the Header")

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals

print("\nEXERCISE 4: Compute Totals")

total_revenue = 0
original_count = 0

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total
        original_count += 1

        print(
            f"{product}: {quantity} units x "
            f"${price:.2f} = ${total:.2f}"
        )

print(f"Total Revenue: ${total_revenue:.2f}")


# EXERCISE 5: Filter and write

print("\nEXERCISE 5: Filter and Write")

written_count = 0

with open(file_path, "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow(
                    [product, price, quantity, round(total, 2)]
                )
                written_count += 1

print(f"Original rows: {original_count}")
print(f"Qualifying rows written: {written_count}")
print("Cleaned file saved to data/cleaned.csv")


# EXERCISE 6: csv.DictReader

print("\nEXERCISE 6: DictReader")

dict_total = 0

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader Total Revenue: ${dict_total:.2f}")

# csv.reader accesses information using column positions.
# DictReader uses column names, making it easier to understand the data.


# EXERCISE 7: Sales summary by product

print("\nEXERCISE 7: Sales Summary by Product")

sales_summary = {}

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8: Append mode log

print("\nEXERCISE 8: Append Mode Log")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(
        f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Run successfully added to data/run_log.txt")
print("\nAll 8 exercises completed!")
