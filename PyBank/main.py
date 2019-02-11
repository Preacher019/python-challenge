import os
import csv

budget_csv = os.path.join("../Resources", "budget_data.csv")

with open(budget_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"date is {', '.join(row)}")