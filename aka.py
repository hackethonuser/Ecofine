import mysql.connector

# Replace with your actual MySQL credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sql123',
    'database': 'circular_marketplace'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ------------------ INITIALIZE DB ------------------ #

def initialize_db():
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS circular_marketplace")
    conn.database = DB_CONFIG['database']

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS listers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            lister_type VARCHAR(50),
            name VARCHAR(100),
            description TEXT,
            quantity VARCHAR(20),
            image VARCHAR(255),
            tags VARCHAR(100)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INT AUTO_INCREMENT PRIMARY KEY,
            collector_name VARCHAR(100),
            item_id INT,
            item_name VARCHAR(100),
            FOREIGN KEY (item_id) REFERENCES items(id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# ------------------ AUTH ------------------ #

def login_lister():
    username = input("Username: ")
    password = input("Password: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM listers WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        print("Login successful.")
        return True
    else:
        print("Authentication failed.")
        return False

def register_lister():
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO listers (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("Registered successfully.")
    except mysql.connector.errors.IntegrityError:
        print("Username already exists.")
    cursor.close()
    conn.close()

# ------------------ LISTER ------------------ #

def lister_menu():
    while True:
        print("\n--- Lister Menu ---")
        print("1. Add item")
        print("2. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            break

def add_item():
    lister_type = input("Business or Farmer? ")
    name = input("Item name: ")
    desc = input("Description: ")
    qty = input("Quantity: ")
    image = input("Image filename: ")
    tags = input("Tags (comma-separated): ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO items (lister_type, name, description, quantity, image, tags)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (lister_type, name, desc, qty, image, tags))
    conn.commit()
    cursor.close()
    conn.close()
    print("Item added.")

# ------------------ COLLECTOR ------------------ #

def collector_menu():
    while True:
        print("\n--- Collector Menu ---")
        print("1. Browse items")
        print("2. Filter by tag")
        print("3. Request item")
        print("4. View my requests")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            browse_items()
        elif choice == "2":
            filter_items()
        elif choice == "3":
            request_item()
        elif choice == "4":
            view_requests()
        elif choice == "5":
            break

def browse_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    for item in cursor.fetchall():
        print(f"{item['id']}: {item['name']} - {item['description']} [{item['quantity']}] ({item['tags']})")
    cursor.close()
    conn.close()

def filter_items():
    tag = input("Tag to filter by: ").lower()
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE LOWER(tags) LIKE %s", (f"%{tag}%",))
    for item in cursor.fetchall():
        print(f"{item['id']}: {item['name']} - {item['description']} [{item['quantity']}] ({item['tags']})")
    cursor.close()
    conn.close()

def request_item():
    collector_name = input("Your name: ")
    item_id = input("Item ID to request: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM items WHERE id = %s", (item_id,))
    row = cursor.fetchone()
    if row:
        item_name = row[0]
        cursor.execute("INSERT INTO requests (collector_name, item_id, item_name) VALUES (%s, %s, %s)",
                       (collector_name, item_id, item_name))
        conn.commit()
        print("Request submitted.")
    else:
        print("Item not found.")
    cursor.close()
    conn.close()

def view_requests():
    name = input("Enter your name: ")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM requests WHERE collector_name = %s", (name,))
    results = cursor.fetchall()
    if results:
        for req in results:
            print(f"Requested '{req['item_name']}' (ID: {req['item_id']})")
    else:
        print("No requests found.")
    cursor.close()
    conn.close()

# ------------------ MAIN ------------------ #

def main():
    initialize_db()
    print("\nWelcome to Circular Economy Marketplace!")
#    user = input("Are you a Lister or Collector? ").strip().lower()
    login_lister()
 #   if user == "lister":
  #      print("1. Login\n2. Register")
   #     action = input("Choose: ")
    #    if action == "2":
     #       register_lister()
      #  if login_lister():
       #     lister_menu()
    #elif user == "collector":
     #   collector_menu()
    #else:
     #   print("Invalid input.")

if __name__ == "__main__":
    main()
