import sqlite3

conn = sqlite3.connect('profile.db')
cursor = conn.cursor()

create_table_query = """CREATE TABLE profile (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, pass_prot BOOLEAN);"""
cursor.execute(create_table_query)

insert_records_query = f"INSERT INTO profile (name,city,pass_prot) VALUES ('Guest','Null',0);"
cursor.execute(insert_records_query)
insert_records_query = f"INSERT INTO profile (name,city,pass_prot) VALUES ('Shashank','kuwait',0);"
cursor.execute(insert_records_query)
insert_records_query = f"INSERT INTO profile (name,city,pass_prot) VALUES ('Tariq','india',0);"
cursor.execute(insert_records_query)

conn.commit()

cursor.execute('SELECT * FROM profile')
for row in cursor:
    print(row)

conn.close()
