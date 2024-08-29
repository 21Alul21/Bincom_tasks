<<<<<<< HEAD
<<<<<<< HEAD
"""module for saving the colur and frequencies to a 
postgresql database
"""

import psycopg2
from collections import Counter
import os

# Color frequency data
color_frequencies = {
    'BLUE': 31, 
    'GREEN': 10, 
    'RED': 9,
    'BLACK': 1, 
    'ASH': 1, 
    'PINK': 5, 
    'ORANGE': 9, 
    'YELLOW': 5, 
    'WHITE': 16, 
    'CREAM': 2, 
    'BROWN': 6
    }


def save_to_postgresql(color_frequencies):
    """Function to save the colors and
    their frequencies to PostgreSQL
    """
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="defaultdb",
            user="avnadmin",
            password= os.environ.get("PASSWORD"),
            host=os.environ.get("HOST"),
            port=os.environ.get("PORT"),
            sslmode="require"
        )
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS color_frequencies (
                color VARCHAR(50) PRIMARY KEY,
                frequency INT
            )
        ''')

        # Insert color frequencies into the table
        for color, frequency in color_frequencies.items():
            cursor.execute(
                '''
                INSERT INTO color_frequencies (color, frequency)
                VALUES (%s, %s)
                ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency
                ''',
                (color, frequency)
            )

        # Commit the transaction
        conn.commit()
        print("Data has been saved to the database.")

        # Close the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

# Call the function to save data
save_to_postgresql(color_frequencies)
=======
>>>>>>> parent of ac469bc (added file for saving color and frequencies to postgresql db)
=======
>>>>>>> parent of ac469bc (added file for saving color and frequencies to postgresql db)
