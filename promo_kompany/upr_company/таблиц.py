import sqlite3

conn = sqlite3.connect("db.sqlite3")
curs = conn.cursor()
# основные таблицы
curs.execute("CREATE TABLE People(id int, Email varchar(32), password varchar(32), name varchar(32), surname varchar(32), phone_number varchar(12))")
curs.execute("CREATE TABLE Home(id int, city varchar(32), Street  varchar(32), num_home varchar(10), entrase int, entra  se_kv int, pr_open_kv int, )")
curs.execute("CREATE TABLE Company(id int, name_company int)")
curs.execute("CREATE TABLE bypass_result(apartment№ int, id_company int)")
# доп таблицы
curs.execute("CREATE TABLE Home_company(id_home int, id_company int)")
curs.execute("CREATE TABLE People_company(id_people int, id_company int)")


