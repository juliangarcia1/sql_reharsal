import sqlite3

dbname = 'customers.sql'


conn = sqlite3.connect(database=dbname)

def get_names():
    pass

def reset_tables(db_name):
    with open(db_name, 'r') as fr:
        text = fr.read()
        import pdb; pdb.set_trace()
        queries = text.split(';')

        query = ''
        cur = conn.cursor()
        cur.execute(query)
        cur.commit()
        cur.close()


reset_tables(dbname)



