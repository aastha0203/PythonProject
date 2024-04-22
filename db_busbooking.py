import sqlite3
con = sqlite3.connect('Busbooking.db')
cur = con.cursor()

"""
cur.execute('DROP TABLE BUS;')
cur.execute('''
CREATE TABLE IF NOT EXISTS BUS(
    BID INT NOT NULL,
    TYPE VARCHAR(15) NOT NULL,
    CAPACITY INT NOT NULL,
    FARE INT NOT NULL,
    OPID INT NOT NULL,
    ROUTEID INT NOT NULL,
    PRIMARY KEY(BID),
    FOREIGN KEY(OPID) REFERENCES OPERATOR(OPID),
    FOREIGN KEY(ROUTEID) REFERENCES ROUTE(ROUTEID)
)''')
cur.execute("INSERT INTO BUS VALUES (1,'AC 2x2',30,1000,1,1),(2,'AC 3x2',50,800,1,2),(3,'Non AC 2x2',30,600,1,3),(4,'Non AC 2x2',30,600,1,4)")
#cur.execute('SELECT * FROM BUS')

cur.execute('DROP TABLE OPERATOR;')
cur.execute('''
CREATE TABLE IF NOT EXISTS OPERATOR (
    OPID INT NOT NULL,
    NAME VARCHAR(25) NOT NULL,
    ADDRESS VARCHAR(40) NOT NULL,
    PHONE INT NOT NULL,
    EMAIL VARCHAR(25) NOT NULL,
    PRIMARY KEY(OPID)
)''')
cur.execute("INSERT INTO OPERATOR VALUES (1,'Kamla','AB road Guna',12345,'kamlabus@gmail.com'),(2,'Rayeen','AB road Guna',12346,'rayeen@gmail.com'),(3,'Kalyani','Hauj Khas Delhi',12347,'kalyani@gmail.com'),(4,'Mahakaal','AB road Jhansi',12348,'mahakaal@gmail.com')")
#cur.execute('SELECT * FROM OPERATOR')

cur.execute('DROP TABLE ROUTE;')
cur.execute('''
CREATE TABLE IF NOT EXISTS ROUTE(
    ROUTEID INT NOT NULL,
    SID INT NOT NULL,
    STATION_NAME VARCHAR(15) NOT NULL,
    PRIMARY KEY(ROUTEID,SID)
)''')
cur.execute("INSERT INTO ROUTE VALUES (1,1,'Guna'),(1,2,'JP College'),(1,3,'Binagunj'),(1,4,'Biora'),(1,5,'Bhopal')")
cur.execute("INSERT INTO ROUTE VALUES (2,1,'Bhopal'),(2,2,'Biora'),(2,3,'Binagunj'),(2,4,'JP College'),(2,5,'Guna')")

cur.execute('DROP TABLE RUNS;')
cur.execute('''
CREATE TABLE IF NOT EXISTS RUNS (
    BUSID INT NOT NULL,
    RUNSDATE DATE NOT NULL,
    SEATAVAIL INT NOT NULL
)''')
cur.execute("INSERT INTO RUNS VALUES (1, '2022-09-20', 30), (2, '2022-09-20', 30)")


cur.execute('DROP TABLE BOOKING_HISTORY;')
cur.execute('''
CREATE TABLE IF NOT EXISTS BOOKING_HISTORY (
    REF_NO INT,
    MOBILE_NO INT NOT NULL,
    NAME_OF_CUSTOMER VARCHAR(25) NOT NULL,
    GENDER VARCHAR(6) NOT NULL,
    AGE INT NOT NULL,
    FARE INT NOT NULL,
    TOTAL_NO_OF_SEATS INT NOT NULL,
    BUSID INT NOT NULL,
    BOOKING_DATE DATE NOT NULL,
    TRAVEL_DATE DATE NOT NULL,
    BOARDING_POINT VARCHAR(15) NOT NULL,
    DESTINATION_POINT VARCHAR(15) NOT NULL,
    PRIMARY KEY(REF_NO, MOBILE_NO)
)''')


#create trigger1

#cur.execute('DROP TRIGGER TRIG_BOOK_HISTORY_INSERT')
cur.execute('''
CREATE TRIGGER TRIG_BOOK_HISTORY_INSERT
AFTER INSERT
ON BOOKING_HISTORY
WHEN NEW.REF_NO IS NULL
BEGIN
UPDATE BOOKING_HISTORY
SET REF_NO = IFNULL((SELECT MAX(REF_NO) FROM BOOKING_HISTORY) + 1, 1)
WHERE REF_NO IS NULL;
END
''')
"""


#cur.execute("INSERT INTO ROUTE VALUES (3,1,'Delhi'),(3,2,'Agra'),(3,3,'Jhansi'),(3,4,'Shivpuri')")
#cur.execute("INSERT INTO ROUTE VALUES ()")


#cur.execute("CREATE TABLE IF NOT EXISTS BOOKING_HISTORY (REF_NO INT, MOBILE_NO INT,NAME_OF_CUSTOMER VARCHAR(25),GENDER VARCHAR(6),AGE INT,FARE INT,TOTAL_NO_OF_SEATS INT,BUSID INT,BOOKING_DATE DATE,TRAVEL_DATE DATE,BOARDING_POINT VARCHAR(15),DESTINATION_POINT VARCHAR(15),PRIMARY KEY(MOBILE_NO))")


#cur.execute('DESCRIBE RUNS')


#cur.execute('SELECT * FROM BUS')
print(cur.execute('SELECT * FROM BUS').fetchall())
#cur.execute('SELECT * FROM ROUTE')
print(con.execute('SELECT * FROM ROUTE').fetchall())
cur.execute('SELECT * FROM OPERATOR')
print(cur.fetchall())
cur.execute('SELECT * FROM RUNS')
res = cur.fetchall()
print(res)
print(con.execute('SELECT * FROM BOOKING_HISTORY').fetchall())


'''
res = cur.execute("select * from runs").fetchone()
print(res[1] , type(res[1]))
'''



#create trigger2 not working
"""
#cur.execute('DROP TRIGGER TRIG_BOOK_HISTORY_INSERT1')
cur.execute('''
CREATE TRIGGER TRIG_BOOK_HISTORY_INSERT1
AFTER INSERT
ON BOOKING_HISTORY
FOR EACH ROW
BEGIN
IF()
UPDATE RUNS
SET SEATAVAIL = IFNULL((SELECT MAX(SEATAVAIL) FROM RUNS) - 1, 1);
END
''')
"""
con.commit()
con.close()




#cur.execute("INSERT INTO TEST VALUES (1,'RATNESH'),(2,'ASHUTOSH')")
#cur.execute('SELECT * FROM TEST;')


