import sqlite3

db_path = "../sql/lawn-mowing.db"


def db_load():
    table_names = [
        "Booking",
        "Booking_service",
        "Customer",
        "Employee",
        "Job",
        "service_type",
    ]

    tables_data = {}

    # Connect to the SQLite database file
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for table in table_names:
        cursor.execute("SELECT * FROM {table}")

        headers = [description[0] for description in cursor.description]

        # Retrieve all row entries
        rows = cursor.fetchall()

        # Combine headers and rows into a 2D list matrix
        matrix_2d = [headers] + [list(row) for row in rows]
        tables_data = matrix_2d
        conn.close()
    return tables_data


def customer_menu(user, password, table):
    pass


def employee_menu(user, password):
    pass


def admin_menu(password):
    admin_pass = "seventeen38"
    if password != admin_pass:
        print("Incorrect admin password, sign in again")
        return


def main():
    db_tables = db_load()
    while True:
        menu_type = input(
            "Welcome to Greener Days Law Care Digital interface. If you are a customer, enter  1, if you are an employee, enter 2, if admin, enter 3:"
        )
        if menu_type == "1":
            customer_choice = input(
                "Enter 1 if you are not an existing customer, otherwise enter 2"
            )
            while customer_choice not in ["1", "2"]:
                customer_choice = input("Invalid input, please re-enter your option: ")
            if customer_choice == "1":
                validity = False
