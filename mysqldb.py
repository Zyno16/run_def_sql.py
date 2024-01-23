import mysql.connector
all_err =""
try:
    conn = mysql.connector.connect(
        host   = "localhost",
        user   = "userpython",
        passwd  = "123456",
        database ="arabicinfo"
        )
except mysql.connector.Error as e:
    all_err += str(e) +", "

def dbrun(sql):
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute( sql )
            conn.commit()
            return True
        else:
            return False

    except mysql.connector.Error as e:
        all_err += str(e) + ","
        return False
 
def dbget(sql):
    try:
        if "conn" in globals():
            cur =conn.cursor()
            cur.execute("select * from emp")
            all_rows =cur.fetchall()
            return all_rows
        else:
            return []
    except mysql.connector.Error as e:
        all_err += str(e) +","
        return []
