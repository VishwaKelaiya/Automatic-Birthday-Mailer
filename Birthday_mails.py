import smtplib, ssl
import datetime
import psycopg2 as pg2

def sendmail(s1):
   try:
      port = 465  # For SSL
      smtp_server = "smtp.gmail.com"
      sender_email = ""  # Enter your gmail address here
      receiver_email = s1  # Enter receiver address
      password = input("Type your mail account password and press enter: ")
      message = """Happy Birthday!!!!"""

      context = ssl.create_default_context()
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
         server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, message)
      print('mail sent successfully')

   except:
      print('Some error with smtp mail part!')

   return None

secret = '' # enter your postgres password

y = datetime.datetime.now()
try:
   conn = pg2.connect(database='Birthday_details',user='postgres',password=secret)#database = your sql database,
   # here I have used postgresql database
   cur = conn.cursor()
   cur.execute('SELECT * FROM bday_mail_details')
   x = cur.fetchall() # fetched all data from database
   l1=[]
   for i in range(len(x)):
       if '-'.join(map(str,[y.day,y.month])) == '-'.join(map(str,[ x[i][2].day,x[i][2].month])):
           l1.append(x[i][1])
   sendmail(l1)
except:
   print('Please check some error in database part!')



