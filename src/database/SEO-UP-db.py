#sudo apt-get install python3-dev libpq-dev
#pip3 install psycopg2
#sudo apt install -y postgresql postgresql-contrib postgresql-client
#sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'admin';"
#sudo passwd postgres
def connect():
    """ Connect to the PostgreSQL database server """
    import psycopg2

    conn = None
    try:
    # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(user="postgres", database="postgres", password="admin", host="localhost", port=5432)
        conn.autocommit = True

    # create a cursor
        cur = conn.cursor()
        
    # execute a statement
    # write to table
        print('Connected to Databse. Executing Query\n')
        cur.execute("SELECT * FROM keywords;")

    # show results of table
        result = cur.fetchall()
        print(result)
        
       
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()