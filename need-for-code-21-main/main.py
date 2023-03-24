import smtplib
conn =smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('gaurishbhosale2002@gmail.com','rsuthrkzqbmembqb')
conn.sendmail('gaurishbhosale2002@gmail.com','mdkalbande@gmail.com','Need Help Urgently! ')
conn.quit()