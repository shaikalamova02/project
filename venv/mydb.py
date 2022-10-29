import mysql.connector
mydb = mysql.connector.connect(
  host="byghb6d46yybynjv0tsr-mysql.services.clever-cloud.com",
  user="u8tzi4kadbrv7nyy",
  password="ApHKufhtw1Mqrvr4JxFo",
  database="byghb6d46yybynjv0tsr"
)
print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE airport (name_of_airport VARCHAR(255),city VARCHAR(255),country VARCHAR(255));")


sql = "INSERT INTO airport (name_of_airport,city,country) VALUES (%s,%s,%s)"
val= ("Almaty International Airport ","Almaty","KZ")
mycursor.execute(sql,val)
mydb.commit()
