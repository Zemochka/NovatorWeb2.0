import smtplib
import psycopg2
import random
import time

conn = psycopg2.connect(database="postgres", user="postgres", password="zematema", host="localhost", port=5432)
cur = conn.cursor()
email = 'piton879@yandex.ru' #Тестовая почта
password = '12345678aA'
cur.execute("CREATE TABLE zema (id SERIAL PRIMARY KEY, " + "email VARCHAR(64), content VARCHAR(64))") #При повторном запуске необхадимо закоментироватьэту строку	

server = smtplib.SMTP('smtp.yandex.ru', 587)
server.ehlo() 
server.starttls()
server.login(email, password)
cur.execute("SELECT id, email, content FROM zema")
task = cur.fetchone()

while True:	
	cur.execute("SELECT id, email, content FROM zema")
	for row in cur:							#Испульзуется вместо cur.fetchone() для оптимизации процесса
		task = row
		id, dest_email, email_text = task

	if task != None:	
		subject = 'Messege from chatbot'
		message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (email, dest_email, subject, email_text)
		log = ("mail send to " + dest_email + " text: " + email_text + " number: " + str(id))
		print(log)	# server.sendmail(email, dest_email, message)

	time.sleep(1)
	cur.execute("INSERT INTO zema (email, content) VALUES (%s, %s)", ("art.kurg2005@gmail.com", "Messege from database"))
	conn.commit()
