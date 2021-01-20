import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE customers 
		(customerId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')

conn.execute('''CREATE TABLE  admins
		(adminId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		)''')

conn.execute('''CREATE TABLE  suppliers
		(supplierId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')


conn.execute('''CREATE TABLE "products" (
	"productId"	INTEGER,
	"name"	TEXT,
	"price"	REAL,
	"description"	TEXT,
	"image"	TEXT,
	"imageFile"	BLOB,
	"stock"	INTEGER,
	"productGrade"	INTEGER,
	"categoryId"	INTEGER,
	"supplierId"	INTEGER,
	FOREIGN KEY("supplierId") REFERENCES "suppliers"("supplierId"),
	FOREIGN KEY("categoryId") REFERENCES "categories"("categoryId"),
	PRIMARY KEY("productId")
)''')

conn.execute('''CREATE TABLE "cart" (
		"userId"	INTEGER,
		"productId"	INTEGER,
		FOREIGN KEY("productId") REFERENCES "products"("productId"),
		FOREIGN KEY("userId") REFERENCES "users"("userId")
	)''')


conn.execute('''CREATE TABLE "purchaseHistory" (
		"customerId"	INTEGER,
		"productId"	INTEGER,
		FOREIGN KEY("productId") REFERENCES "products"("productId"),
		FOREIGN KEY("customerId") REFERENCES "customers"("customerId")
)''')

conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')



conn.close()

