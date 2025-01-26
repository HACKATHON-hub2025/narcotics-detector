import tkinter as tk
from tkinter import messagebox 
import sqlite3

# Function to check if the substance is narcotic or not based on the numeric range
def check_narcotic_with_range(db_name, table_name, range_start, range_end):
    try:
        # Connect to the provided database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Query to retrieve all data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if not rows:
            output_text.insert(tk.END,f"The table '{table_name}' is empty.")
            return
        
        print(f"Checking for narcotics in the '{table_name}' table based on the range [{range_start}, {range_end}]...")

        # Iterate over the rows and check if the value is within the range for narcotics
        narcotic_found = False
        for row in rows:
            # Assume the column to check is the second column (index 1) - modify as needed
            # If column contains numeric values (e.g., severity or dosage), this check applies
            column_value = row[1]  # Adjust the index if your column is different

            if column_value is not None and range_start <= column_value <= range_end:
                narcotic_found = True
                print(f"Row {row} is related to a narcotic (value {column_value} is within range).")
        
        if not narcotic_found:
            print("No narcotic-related data found within the specified range.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

# Main program
if __name__ == "__main__":
    db_name = input("Enter the path to your database file (e.g., 'my_database.db'): ").strip()
    table_name = input("Enter the table name to check for narcotics: ").strip()
    
    # Specify the numeric range that classifies narcotics (e.g., severity or dosage range)
    range_start = float(input("Enter the starting value of the range: ").strip())
    range_end = float(input("Enter the ending value of the range: ").strip())
    
    # Call the function to check the narcotics within the specified range
    check_narcotic_with_range(db_name, table_name, range_start, range_end)
