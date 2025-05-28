import os
import sqlite3

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'sample_data.db')

# SQL script path
SQL_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'init_db.sql')

def init_database():
    """Initialize the SQLite database with sample data."""
    # Remove existing database if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    # Create a new database
    conn = sqlite3.connect(DB_PATH)
    
    try:
        # Read SQL script
        with open(SQL_SCRIPT_PATH, 'r') as f:
            sql_script = f.read()
        
        # Execute SQL script
        conn.executescript(sql_script)
        
        # Commit changes
        conn.commit()
        
        print(f"Database initialized successfully at {DB_PATH}")
        
        # Verify tables were created
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Created tables: {', '.join([table[0] for table in tables])}")
        
        # Count rows in each table
        for table in [table[0] for table in tables]:
            cursor.execute(f"SELECT COUNT(*) FROM {table};")
            count = cursor.fetchone()[0]
            print(f"Table {table}: {count} rows")
    
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
    
    finally:
        # Close connection
        conn.close()

if __name__ == "__main__":
    init_database()
