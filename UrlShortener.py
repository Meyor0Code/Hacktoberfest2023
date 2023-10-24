import sqlite3
import random
import string

# Initialize the SQLite database
conn = sqlite3.connect('url_shortener.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY,
        original_url TEXT,
        short_url TEXT
    )
''')
conn.commit()

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Function to shorten a URL
def shorten_url(original_url):
    # Check if the URL is already in the database
    cursor.execute('SELECT short_url FROM urls WHERE original_url = ?', (original_url,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        # Generate a new short URL
        short_url = generate_short_url()
        cursor.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
        conn.commit()
        return short_url

# Function to expand a short URL
def expand_url(short_url):
    cursor.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    return result[0] if result else None

# Main loop
while True:
    print("\nOptions:")
    print("1. Shorten a URL")
    print("2. Expand a short URL")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        original_url = input("Enter the original URL: ")
        short_url = shorten_url(original_url)
        print(f"Shortened URL: http://your-shortener-domain/{short_url}")
    elif choice == "2":
        short_url = input("Enter the short URL: ")
        original_url = expand_url(short_url)
        if original_url:
            print(f"Expanded URL: {original_url}")
        else:
            print("Short URL not found.")
    elif choice == "3":
        print("Goodbye!")
        conn.close()
        break
    else:
        print("Invalid choice. Please select a valid option.")
