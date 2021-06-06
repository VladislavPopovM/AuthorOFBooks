from db import DB

db = DB()

id_writer = db.set_writer('Толстой, Лев')[0]
db.set_book('Война и мир', id_writer)
db.set_book('Воскресение', id_writer)

id_writer = db.set_writer('Чехов, Антон')[0]
db.set_book('Палата №6', id_writer)
db.set_book('Человек в футляре', id_writer)
db.set_book('Каштанка', id_writer)

id_writer = db.set_writer('Горький, Максим')[0]
db.set_book('Старуха Изергиль' ,id_writer)
db.set_book('На дне' ,id_writer)

db.connect_close()