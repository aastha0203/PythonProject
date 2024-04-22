import sqlite3

CREATE_BUS_TABLE = '''
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
    
)'''
                              
CREATE_ROUTE_TABLE = '''
CREATE TABLE IF NOT EXISTS ROUTE(
    ROUTEID INT NOT NULL,
    SID INT NOT NULL,
    STATION_NAME VARCHAR(15) NOT NULL,
    PRIMARY KEY(ROUTEID,SID)
)'''
    
CREATE_OPERATOR_TABLE = '''
CREATE TABLE IF NOT EXISTS OPERATOR (
    OPID INT NOT NULL,
    NAME VARCHAR(25) NOT NULL,
    ADDRESS VARCHAR(40) NOT NULL,
    PHONE INT NOT NULL,
    EMAIL VARCHAR(25) NOT NULL,
    PRIMARY KEY(OPID)
)'''
    
CREATE_RUNS_TABLE = '''
CREATE TABLE IF NOT EXISTS RUNS (
    BUSID INT NOT NULL,
    RUNSDATE DATE NOT NULL,
    SEATAVAIL INT NOT NULL
)'''
    
CREATE_BOOKING_HISTORY_TABLE = '''
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
)'''

CREATE_TRIGGER = '''
CREATE TRIGGER TRIG_BOOK_HISTORY_INSERT
AFTER INSERT
ON BOOKING_HISTORY
WHEN NEW.REF_NO IS NULL
BEGIN
UPDATE BOOKING_HISTORY
SET REF_NO = IFNULL((SELECT MAX(REF_NO) FROM BOOKING_HISTORY) + 1, 1)
WHERE REF_NO IS NULL;
END
'''

GET_ALL_BUS = "SELECT * FROM BUS;"

FIND_BUS = '''
SELECT BID, OP.NAME, TYPE, SEATAVAIL, CAPACITY, FARE
FROM OPERATOR OP, BUS B, RUNS R
WHERE B.OPID = OP.OPID AND R.BUSID = B.BID AND 
EXISTS(SELECT * 
        FROM ROUTE R1,ROUTE R2 
        WHERE R1.ROUTEID = R2.ROUTEID AND R1.SID < R2.SID AND
        R2.STATION_NAME = ? AND R1.STATION_NAME = ? AND
        R1.ROUTEID = B.ROUTEID AND R2.ROUTEID = B.ROUTEID) AND RUNSDATE = ?;
'''
BOOK_SEAT = '''
INSERT INTO BOOKING_HISTORY(
    NAME_OF_CUSTOMER,
    GENDER,
    TOTAL_NO_OF_SEATS,
    MOBILE_NO,
    AGE,
    FARE,
    DESTINATION_POINT,
    BOARDING_POINT,
    TRAVEL_DATE,
    BUSID,
    BOOKING_DATE
    ) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, DATE('now'));
'''
def book_seat(connection, name, gender, seat, phone, age, fare,
              destination, boarding, travel_date, bid):
    with connection:
        connection.execute(BOOK_SEAT, (name, gender, seat, phone, age, fare,
                destination, boarding, travel_date, bid))


ADD_BUS_OPERATOR = '''
INSERT INTO OPERATOR VALUES (?, ?, ?, ?, ?);
'''
EDIT_OPERATOR = '''
UPDATE OPERATOR
SET NAME=?, ADDRESS=?, PHONE=?, EMAIL=?
WHERE OPID = ?;
'''

ADD_BUS = '''
INSERT INTO BUS VALUES (?, ?, ?, ?, ?, ?);
'''

EDIT_BUS = '''
UPDATE BUS
SET TYPE=?, CAPACITY=?, FARE=?, OPID=?, ROUTEID=?
WHERE BID=?;
'''

ADD_ROUTE = '''
INSERT INTO ROUTE VALUES (?, ?, ?);
'''

EDIT_ROUTE = '''
UPDATE ROUTE
SET SID=?, STATION_NAME=?
WHERE ROUTEID=?;
'''

ADD_RUNNING_DETAILS = '''
INSERT INTO RUNS VALUES (?, ?, ?);
'''

DELETE_RUNNING_DETAILS = '''
DELETE FROM RUNS
WHERE BUSID=? AND RUNSDATE=?;
'''

CHECK_BOOKING = '''
SELECT NAME_OF_CUSTOMER, GENDER, TOTAL_NO_OF_SEATS, MOBILE_NO, AGE, H.FARE, REF_NO, TRAVEL_DATE, BOARDING_POINT, DESTINATION_POINT
FROM BOOKING_HISTORY H, BUS
WHERE MOBILE_NO=? AND BUSID = BID;
'''

GENERATE_TICKET = '''
SELECT NAME_OF_CUSTOMER, GENDER, TOTAL_NO_OF_SEATS, MOBILE_NO, AGE, H.FARE, REF_NO, O.NAME, TRAVEL_DATE, BOOKING_DATE, BOARDING_POINT, DESTINATION_POINT
FROM BOOKING_HISTORY H, BUS B, OPERATOR O
WHERE MOBILE_NO=? AND BUSID = BID AND B.OPID = O.OPID;
'''


UPDATE_SEATAVAIL = '''
UPDATE RUNS
SET SEATAVAIL = SEATAVAIL-1 
WHERE BUSID=? AND RUNSDATE=?;
'''

CHECK_OPERATOR = '''
SELECT OPID
FROM OPERATOR
WHERE OPID = ?;
'''

CHECK_BUS = '''
SELECT BID
FROM BUS
WHERE BID = ?;
'''

CHECK_ROUTE = '''
SELECT ROUTEID
FROM ROUTE
WHERE ROUTEID = ?;
'''

DELETE_ROUTE = '''
DELETE FROM ROUTE WHERE ROUTEID=? AND SID=?;
'''

CHECK_RUNNING_DETAILS = '''
SELECT BUSID
FROM RUNS
WHERE BUSID=? AND RUNSDATE=?;
'''


def connect():
    return sqlite3.connect('Busbooking.db')

def create_tables(connection):
    with connection:
        connection.execute(CREATE_BUS_TABLE)
        connection.execute(CREATE_OPERATOR_TABLE)
        connection.execute(CREATE_ROUTE_TABLE)
        connection.execute(CREATE_RUNS_TABLE)
        connection.execute(CREATE_BOOKING_HISTORY_TABLE)

        
def get_all_bus(connection):
    with connection:
        return connection.execute(GET_ALL_BUS).fetchall()
    
def find_bus(connection, destination, boarding, date):
    with connection:
        return connection.execute(FIND_BUS ,(destination, boarding, date)).fetchall()
    
    
def add_bus_operator(connection, opid, name, address, phone, email):
    with connection:
        connection.execute(ADD_BUS_OPERATOR, (opid, name, address, phone, email))
    
def edit_operator(connection, name, address, phone, email, opid):
    with connection:
        connection.execute(EDIT_OPERATOR, (name, address, phone, email, opid))


def add_bus(connection, bid, bus_type, capacity, fare, opid, routeid):
    with connection:
        connection.execute(ADD_BUS, (bid, bus_type, capacity, fare, opid, routeid))
    
def edit_bus(connection, bus_type, capacity, fare, opid, routeid, bid):
    with connection:
        connection.execute(EDIT_BUS, (bus_type, capacity, fare, opid, routeid, bid))
        

def add_route(connection, routeid, sid, station_name):
    with connection:
        connection.execute(ADD_ROUTE, (routeid, sid, station_name))

        
def edit_route(connection, sid, station_name, routeid):
    with connection:
        connection.execute(EDIT_ROUTE, (sid, station_name, routeid))
        

def add_running_details(connection, bid, runsdate, seatavail):
    with connection:
        connection.execute(ADD_RUNNING_DETAILS, (bid, runsdate, seatavail))
        
def delete_running_details(connection, bid, runsdate):
    with connection:
        connection.execute(ADD_RUNNING_DETAILS, (bid, runsdate))
        
def check_booking(connection, phone):
    with connection:
        return connection.execute(CHECK_BOOKING, (phone, )).fetchone()
        
def book_seat(connection, name, gender, seat, phone, age, fare, destination, boarding, travel_date, bid):
    with connection:
        connection.execute(BOOK_SEAT, (name, gender, seat, phone, age, fare, destination, boarding, travel_date, bid))
        
def update_seatavail(connection, bid, travel_date):
    with connection:
        connection.execute(UPDATE_SEATAVAIL, (bid, travel_date))

def check_operator(connection, opid):
    with connection:
        return connection.execute(CHECK_OPERATOR, (opid, )).fetchone()

def check_bus(connection, bid):
    with connection:
        return connection.execute(CHECK_BUS, (bid, )).fetchone()

def check_route(connection, routeid):
    with connection:
        return connection.execute(CHECK_ROUTE, (routeid, )).fetchone()

def delete_route(connection, routeid, sid):
    with connection:
        return connection.execute(CHECK_ROUTE, (routeid, sid)).fetchone()

def check_running_details(connection, bid, runsdate):
    with connection:
        return connection.execute(CHECK_RUNNING_DETAILS, (bid, runsdate)).fetchone()

def generate_ticket(connection, phone):
    with connection:
        return connection.execute(GENERATE_TICKET, (phone, )).fetchone()



    

