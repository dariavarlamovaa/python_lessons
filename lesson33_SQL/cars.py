import sqlite3 as sq

# Нам не нужно использовать эти функции, тк мы работаем в контекстном менеджере
# con.commit()
# con.close()

# cars = [
#     ("Volvo", 333),
#     ("LADA", 120),
#     ("BMW", 600),
#     ("Opel", 134),
#     ("Volvo", 800),
# ]

with sq.connect('cars.db') as con:
    cur = con.cursor()
    # =================================================
    # cur.execute('''CREATE TABLE IF NOT EXISTS cars(
    # cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
    # model TEXT NOT NULL,
    # price INTEGER CHECK(price > 0))
    # ''')

    # =================================================
    # with for-loop
    # for car in cars:
    #     cur.execute('''INSERT INTO cars VALUES(NULL, ?, ?)''', car)

    # with executemany()
    # cur.executemany('''INSERT INTO cars VALUES(NULL, ?, ?)''', cars)

    # with many rows
    # cur.execute('''INSERT INTO  cars VALUES(NULL, "Opel", 170)''')
    # cur.execute('''INSERT INTO  cars VALUES(NULL, "BMW", 500)''')
    # cur.execute('''INSERT INTO  cars VALUES(NULL, "Volvo", 350)''')
    # cur.execute('''INSERT INTO  cars VALUES(NULL, "KIA", 190)''')
    # cur.execute('''INSERT INTO  cars VALUES(NULL, "Toyota", 250)''')

    # =================================================
    # cur.execute('''SELECT * FROM cars''')
    # print(cur.fetchall())  # fetchall() is not allowed to call again
    # print(cur.fetchmany(5))  # 5 first rows

    # =================================================
    # cur.executescript('''INSERT INTO  cars VALUES(NULL, "Volvo", 300);
    #                     INSERT INTO  cars VALUES(NULL, "BWM", 900)''')

    # =================================================
    # try:
    #     cur.executescript('''BEGIN;
    #     CREATE TABLE IF NOT EXISTS expensive_cars(
    #     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     model TEXT NOT NULL,
    #     price INTEGER CHECK(price > 0)
    #     );
    #     UPDATE cars SET price = price + 100;
    #     INSERT INTO expensive_cars
    #     SELECT * FROM cars WHERE price >= 300;
    #     ''')
    # except sq.Error as e:
    #     print(e)
    #     if con:
    #         con.rollback()
    #
    # else:
    #     if con:
    #         con.commit()
