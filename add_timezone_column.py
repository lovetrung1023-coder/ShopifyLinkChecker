
#!/usr/bin/env python3
"""
Migration script to add timezone_checked column to stores table
"""
import psycopg2
import os

def add_timezone_column():
    """Add timezone_checked column to stores table"""
    
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable is not set")
        return
    
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        
        print("🔄 Adding timezone_checked column to stores table...")
        
        # Check if column already exists
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='stores' AND column_name='timezone_checked'
        """)
        
        if cur.fetchone():
            print("✅ Column timezone_checked already exists")
        else:
            # Add the column
            cur.execute("""
                ALTER TABLE stores 
                ADD COLUMN timezone_checked VARCHAR(100)
            """)
            conn.commit()
            print("✅ Successfully added timezone_checked column")
        
        cur.close()
        conn.close()
        
        print("\n✅ Migration completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        if conn:
            conn.rollback()
        raise

if __name__ == "__main__":
    add_timezone_column()
