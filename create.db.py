import sqlite3
from faker_library import Faker

conn = sqlite3.connect("person_data.db")
c = conn.cursor()

c.execute("""Create table person(
id INTEGER PRIMARY KEY,
name TEXXT,
age INT,
address TEXT,
phone TEXT,
email TEXT
)""")

faker = Faker()
for i in range(500):
    name = faker.name()
    age = faker.random_int(min = 18, max = 80,step=1)
    address = faker.address()
    phone = faker.phone_number()
    email = faker.email()
    c.execute("INSERT INTO person(name,age,address,phone,email) VALUES(?,?,?,?,?)",(name,age,address,phone,email))


conn.commit()
conn.close()


