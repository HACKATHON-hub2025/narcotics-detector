import sqlite3

# Function to load and display database content
def load_database(db_name):
    try:
        # Connect to the provided database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # List tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if not tables:
            print("No tables found in the database.")
            return

        print(f"Tables found in the database '{db_name}':")
        for table in tables:
            print(f"- {table[0]}")
        
        # Let the user select a table to view its content
        table_name = input("Enter the table name to view its content: ")
        
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            if rows:
                print(f"Content of '{table_name}':")
                for row in rows:
                    print(row)
            else:
                print(f"The table '{table_name}' is empty.")
        except sqlite3.OperationalError:
            print(f"Table '{table_name}' does not exist.")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    db_name = input("Enter the path to your database file (e.g., 'my_database.db'): ").strip()
    load_database(db_name)
