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
        cursor.execute(f'SELECT * FROM "{table}"')

        headers = [description[0] for description in cursor.description]

        # Retrieve all row entries
        rows = cursor.fetchall()

        # Combine headers and rows into a 2D list matrix
        matrix_2d = [headers] + [list(row) for row in rows]
        tables_data[table] = matrix_2d
    conn.close()
    return tables_data


def customer_menu(email, password, table, new):

    valid = True
    if new:
        if "@" not in email:
            print("Your email is not correctly formatted")
            valid = False
        if len(password) < 8:
            print("password is too short, must be 8 characters or longer")
            valid = False
        for i in table:
            if i[3] == email:
                print("Email exists, please use a different one.")
                valid = False
        return valid
    else:
        valid = False
        for i in table:
            if i[3] == email:
                if i[4] == password:
                    valid = True
        if valid:
            print("login successful good job goy")
        else:
            print("email or password incorrect")
            return False
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
            "Welcome to Greener Days Law Care Digital interface. If you are a customer, enter  1, if you are an employee, enter 2, if admin, enter 3. Enter 4 to exit:"
        )
        if menu_type == "1":
            customer_choice = input(
                "Enter 1 if you are not an existing customer, otherwise enter 2: "
            )
            while customer_choice not in ["1", "2"]:
                customer_choice = input("Invalid input, please re-enter your option: ")
            if customer_choice == "1":
                validity = False
                while not validity:
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    validity = customer_menu(
                        email, password, db_tables["Customer"], True
                    )
            elif customer_choice == "2":
                validity = False
                while not validity:
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    validity = customer_menu(
                        email, password, db_tables["Customer"], False
                    )
        elif menu_type == "2":
            pass
        elif menu_type == "3": 
            pass
        elif menu_type == "4":
            print("Thanks for using this service. Goodbye now")
            return
        else:
            print("Invalid input")

main()
