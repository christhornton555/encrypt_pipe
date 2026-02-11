# Generates a small csv of dummy data for testing purposes

import csv
import random
from datetime import date, timedelta

def generate_dummy_data(filename='dummy_data.csv', num_rows=10):
    start_date = date(2025, 1, 1)
    end_date = date(2025, 12, 31)
    employees = [10001, 10002, 10003, 10004, 10005]

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Employee', 'Cost']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for _ in range(num_rows):
            # Generate random date
            days_between = (end_date - start_date).days
            random_days = random.randrange(days_between + 1)
            random_date = start_date + timedelta(days=random_days)
            
            # Generate random employee
            employee = random.choice(employees)
            
            # Generate random cost
            cost = round(random.uniform(100.00, 1000.00), 2)
            
            writer.writerow([random_date, employee, cost])

if __name__ == '__main__':
    generate_dummy_data()
    print("dummy_data.csv has been generated.")
