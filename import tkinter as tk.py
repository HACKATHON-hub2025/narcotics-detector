import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to check if the substance is narcotic or not based on the numeric range
def check_narcotic_with_range(db_name, table_name, range_start, range_end, output_text):
    try:
        # Connect to the provided database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Query to retrieve all data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if not rows:
            output_text.insert(tk.END, f"The table '{table_name}' is empty.\n")
            return

        # Iterate over rows to check the range
        for row in rows:
            if len(row) < 2:
                output_text.insert(tk.END, f"Row {row} does not have enough columns to check.\n")
                continue

            value = float(row[1])  # Assuming the numeric value is in the second column
            if range_start <= value <= range_end:
                output_text.insert(
                    tk.END, f"Substance '{row[0]}' with value {value} is within the range.\n"
                )
            else:
                output_text.insert(
                    tk.END, f"Substance '{row[0]}' with value {value} is out of the range.\n"
                )

        conn.close()

    except sqlite3.OperationalError as e:
        output_text.insert(tk.END, f"Database error: {str(e)}\n")
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {str(e)}\n")

# Function to create the GUI
def create_gui():
    window = tk.Tk()
    window.title("Narcotic Range Checker")

    # Database name input
    tk.Label(window, text="Database Name:").grid(row=0, column=0, sticky=tk.W, padx=10)
    db_name_entry = tk.Entry(window)
    db_name_entry.grid(row=0, column=1, padx=10)

    # Table name input
    tk.Label(window, text="Table Name:").grid(row=1, column=0, sticky=tk.W, padx=10)
    table_name_entry = tk.Entry(window)
    table_name_entry.grid(row=1, column=1, padx=10)

    # Range start input
    tk.Label(window, text="Range Start:").grid(row=2, column=0, sticky=tk.W, padx=10)
    range_start_entry = tk.Entry(window)
    range_start_entry.grid(row=2, column=1, padx=10)

    # Range end input
    tk.Label(window, text="Range End:").grid(row=3, column=0, sticky=tk.W, padx=10)
    range_end_entry = tk.Entry(window)
    range_end_entry.grid(row=3, column=1, padx=10)

    # Text widget to display the output
    output_text = tk.Text(window, height=10, width=50)
    output_text.grid(row=4, column=0, columnspan=2, pady=10)

    # Function to handle the button click
    def on_check_button_click():
        db_name = db_name_entry.get().strip()
        table_name = table_name_entry.get().strip()
        try:
            range_start = float(range_start_entry.get().strip())
            range_end = float(range_end_entry.get().strip())
            check_narcotic_with_range(db_name, table_name, range_start, range_end, output_text)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for range start and end.")

    # Button to start the check
    check_button = tk.Button(window, text="Check Narcotics", command=on_check_button_click)
    check_button.grid(row=5, column=0, columnspan=2)

    window.mainloop()

# Run the GUI application
if _name_ == "_main_":
    create_gui()