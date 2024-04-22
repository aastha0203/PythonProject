import database
from tkinter import *
from tkinter.messagebox import *


class Project:
    def __init__(self):
        root = Tk()
        h, w, = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        def close():
            root.destroy()
            self.menu()

        #Frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()

        #Headers
        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)

        Label(frame2, text="Name:Aastha Gupta", font="arial 12 bold",
              fg='blue').grid(row=1, column=0, pady=40)

        Label(frame2, text="Er : 211B005", font="arial 12 bold",
              fg='blue').grid(row=2, column=0)

        Label(frame2, text="Mobile:7903371384", font="arial 12 bold",
              fg='blue').grid(row=3, column=0, pady=40)



        Label(frame2, text="Submitted to :Dr. Mahesh Kumar", font="arial 14 bold",
              bg='sky blue', fg='red').grid(row=4, column=0)

        Label(frame2, text="Project Based Learning", font="arial 12 bold",
              fg='red').grid(row=5, column=0)

        root.after(5000, close)

        root.mainloop()

    def menu(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
            

        def seat_book():
            root.destroy()
            self.seatbooking()
        def check_booked_list():
            root.destroy()
            self.check_book_ticket()
        def add_bus_details():
            root.destroy()
            self.addbusdetails()
            
        #Frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()

        #Headers
        bus = PhotoImage(file=".//Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0, columnspan=3)



        Button(frame2, text='Seat Booking', font='arial 14', command=seat_book ,
               bg='green2').grid(row=1, column=0, padx=20,  pady=30)

        Button(frame2, text='Checked Booked Seat', font='arial 14', command=check_booked_list,
               bg='green3').grid(row=1, column=1, padx=20,  pady=30)
        Button(frame2, text='Add Bus Details', font='arial 14', command=add_bus_details,
               bg='green4').grid(row=1, column=2, padx=20,  pady=30)

        Label(frame2, text='For Admin Only', font='arial 10 bold',
              fg='Red').grid(row=2, column=2, pady=20)


        root.mainloop()

    def seatbooking(self):
        root = Tk()
        h, w, = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))


        connection = database.connect()
        database.create_tables(connection)
        #database.update_seatavail(connection, 1, '2022-09-20')
        #database.book_seat(connection, 'Aastha', 'Female', 2, 7903371384, 20, 100,'Guna', 'Bhopal', '2022-09-20', 1)

        #database.create_tables(connection)
        #bus_list = database.find_bus(connection, 'Guna', 'Bhopal', '2022-09-20')
        #bus_list = database.get_all_bus(connection)
        #bus_list = connection.execute('select * from runs;').fetchall()
        #no_of_buses = len(bus_list)
        #print(bus_list)
        #for i in range(len(bus_list)):
        #    print(i)

        #Frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()
        frame4 = Frame(root)
        frame4.pack()
        frame5 = Frame(root)
        frame5.pack()
        frame6 = Frame(root, relief='groove', bd=3)
        frame6.pack()

        #Headers
        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Enter Journey Details", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=10)


        Label(frame3, text="To").grid(row=0, column=0)
        to = Entry(frame3, width=20)
        to.grid(row=0, column=1)

        Label(frame3, text="From").grid(row=0, column=2)
        frm = Entry(frame3, width=20)
        frm.grid(row=0, column=3)

        Label(frame3, text="Journey Date").grid(row=0, column=4)
        date = Entry(frame3, width=20)
        date.grid(row=0, column=5)





        def showbus():

            def proceed_to_book():#(to, frm, date):
                Label(frame5, text='Fill Passenger Details to book bus ticket', font='Arial 18 bold ',
                  fg='red', bg='light blue').grid(row=0, column=0, columnspan=15)

                Label(frame5, text="Name").grid(row=1, column=0, pady=20)
                nm = Entry(frame5, width=20)
                nm.grid(row=1, column=1, padx=10)

                #Drop down Menu
                Label(frame5, text="Gender").grid(row=1, column=2)
                gender_type = StringVar()
                gender_type.set('Male')
                opt = ["Male", "Female", "Other"]
                d_menu = OptionMenu(frame5, gender_type,
                                    *opt).grid(row=1, column=3, padx=10)

                Label(frame5, text="No of Seats").grid(row=1, column=4, padx=10)
                seats = Entry(frame5, width=4)
                seats.grid(row=1, column=5, padx=10)

                Label(frame5, text="Mobile No").grid(row=1, column=6, padx=10)
                mob = Entry(frame5, width=12)
                mob.grid(row=1, column=7, padx=10)

                Label(frame5, text="Age").grid(row=1, column=8, padx=10)
                age = Entry(frame5, width=5)
                age.grid(row=1, column=9, padx=10)


                def confirm():
                    nm1=nm.get()
                    gender1=gender_type.get()
                    seats1=int(seats.get())
                    mob1=int(mob.get())
                    age1=int(age.get())
                    fare1=fare[int(bus_select.get())-1]
                    #print(fare1, type(fare1))
                    total_fare=fare1*seats1
                    bid=bus[int(bus_select.get())-1]

                    print(gender1, type(gender1))
                    print(seats1, type(seats1))
                    print(mob1, type(mob1))
                    print(age1, type(age1))
                    print(nm1, type(nm1))
                    print(total_fare, type(total_fare))
                    print(bid, type(bid))

                    if (seats1>0):
                        choice = askyesno('Fare Confirm','Total amount to be paid Rs'+str(total_fare))
                    
                    #print(nm1, gender1, seats1, mob1, age1)
                    print(nm1, gender1, seats1, mob1, age1, total_fare, to1, frm1, date1, bid)
                    
                    if choice==True:
                        #booking seat
                        connection = database.connect()
                        database.book_seat(connection, nm1, gender1, seats1,
                                           mob1, age1, total_fare, to1, frm1, date1, bid)
                                           
                        '''
                        database.book_seat(connection, 'Aastha', 'Female', 2,
                                           7903371384, 20, 100, 'Guna', 'Bhopal', '2022-09-20', 1)
                                           '''
                        #updating seatavail
                        database.update_seatavail(connection, bid, date1)
                        #database.update_seatavail(connection, 1, '2022-09-20')
                        root.destroy()
                        self.bus_ticket(mob1)

                        


                
                Button(frame5, text="Book Seat", command=confirm,
                       bg='green2').grid(row=1, column=10, padx=10)

                print(connection.execute('select * from booking_history').fetchall())

            widgets=frame4.grid_slaves()
            for i in widgets:
                i.destroy()
            '''
            widgets=frame5.grid_slaves()
            for i in widgets:
                i.destroy()'''

            #Headers
            Label(frame4, text="Select Bus", font="arial 10 bold",
                  fg='green3').grid(row=0, column=0, padx=10)
            Label(frame4, text="Operator", font="arial 10",
                  fg='green3').grid(row=0, column=1, padx=10)
            Label(frame4, text="Bus Type", font="arial 10",
                  fg='green3').grid(row=0, column=2, padx=10)
            Label(frame4, text="Available/Capacity", font="arial 10",
                  fg='green3').grid(row=0, column=3, padx=10)
            Label(frame4, text="Fare", font="arial 10",
                  fg='green3').grid(row=0, column=4, padx=10)

            
            to1=(to.get()).capitalize()
            frm1=(frm.get()).capitalize()
            date1=date.get()
            
            
            bus_list = database.find_bus(connection, to1, frm1, date1)
            #bus_list = database.find_bus(connection, 'Guna', 'Bhopal', '2022-09-20')
            #bus_list = database.find_bus(connection, 'Guna', 'Bhopal', '20-09-2022')

            no_of_buses = len(bus_list)
            print(to1, frm1, date1)
            print(bus_list)


            bus_select = IntVar()
            bus=[]
            fare=[]
            a=0
            for i in bus_list:
                print(i)
                bus.append(i[0])
                b = Radiobutton(frame4, text='Bus'+str(a+1),
                       variable=bus_select, value=a+1, indicator=0 ,bg='green2').grid(row=a+1, column=0, padx=10)
                Label(frame4, text=i[1], font="arial 10 italic",
                  fg='blue').grid(row=a+1, column=1)
                Label(frame4, text=i[2], font="arial 10",
                  fg='blue').grid(row=a+1, column=2)
                Label(frame4, text=str(i[3])+'/'+str(i[4]), font="arial 10",
                  fg='blue').grid(row=a+1, column=3)
                Label(frame4, text=i[5], font="arial 10",
                  fg='blue').grid(row=a+1, column=4)
                fare.append(i[5])
                a+=1
            
            
            Button(frame4, text="Proceed to Book", command=proceed_to_book,
                   bg='green2').grid(row=1, column=5, padx=125, pady=20)



        Button(frame3, text='Show Bus', command=showbus, fg='black',
               bg='light green').grid(row=0, column=6, padx=10)
        def home():
            root.destroy()
            self.menu()

        img1 = PhotoImage(file=".//home.png")
        Button(frame3, fg='black', bg='light green',command=home,
               image=img1).grid(row=0, column=7)

        connection.commit()

        root.mainloop()

    def bus_ticket(self, mob1):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        connection = database.connect()


        #Frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root, relief='groove', bd=3)
        frame3.pack()

        #Headers
        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Bus Ticket").grid(row=1, column=0, pady=10)


        ticket = database.generate_ticket(connection, mob1)
        print(ticket, type(ticket))
                        
        Label(frame3, text="Passengers : "+ticket[0]).grid(row=0, column=0)
        Label(frame3, text="Gender : "+ticket[1]).grid(row=0, column=1)
        Label(frame3, text="No of seats: "+str(ticket[2])).grid(row=1, column=0)
        Label(frame3, text="Phone : "+str(ticket[3])).grid(row=1, column=1)
        Label(frame3, text="Age :"+str(ticket[4])).grid(row=2, column=0)
        Label(frame3, text="Fare Rs: "+str(ticket[5])).grid(row=2, column=1)
        Label(frame3, text="Booking Ref. "+str(ticket[6])).grid(row=3, column=0)
        Label(frame3, text="Bus Detail: "+ticket[7]).grid(row=3, column=1)
        Label(frame3, text="Travel On: "+ticket[8]).grid(row=4, column=0)
        Label(frame3, text="Booked On: "+ticket[9]).grid(row=4, column=1)
        Label(frame3, text="Boarding Point: "+ticket[10]).grid(row=5, column=0)
        Label(frame3, text="Destination Point: "+ticket[11]).grid(row=5, column=1)
        Label(frame3, text="*Total amount Rs "+str(ticket[5])+
                " /- to be paid at the time of boarding the bus", font="arial 8 italic").grid(row=7, column=0, columnspan=2)
        showinfo('Success','Seat Booked ....')

        root.mainloop()

    def check_book_ticket(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        connection = database.connect()
        database.create_tables(connection)

        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()
        frame4 = Frame(root, relief='groove', bd=3)
        frame4.pack()

        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Check Your Booking", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=30)



        Label(frame3, text="Enter Your Mobile No:").grid(row=0, column=0, pady=10)
        mob = Entry(frame3, width=15)
        mob.grid(row=0, column=1)



        def check():
            mob1=int(mob.get())
            data = database.check_booking(connection, mob1)
            print(data)
            
            if (data):
                
                Label(frame4, text="Passengers : "+data[0]).grid(row=0, column=0)
                Label(frame4, text="Gender : "+data[1]).grid(row=0, column=1)
                Label(frame4, text="No of seats: "+str(data[2])).grid(row=1, column=0)
                Label(frame4, text="Phone : "+str(data[3])).grid(row=1, column=1)
                Label(frame4, text="Age :"+str(data[4])).grid(row=2, column=0)
                Label(frame4, text="Fare Rs: "+str(data[5])).grid(row=2, column=1)
                Label(frame4, text="Booking Ref. "+str(data[6])).grid(row=3, column=0)
                Label(frame4, text="Travel On: "+data[7]).grid(row=4, column=0)
                Label(frame4, text="Boarding Point: "+data[8]).grid(row=5, column=1)
                Label(frame4, text="Destination Point: "+data[9]).grid(row=6, column=0)
                Label(frame4, text="*Total amount Rs "+str(data[5])+
                      " /- to be paid at the time of boarding the bus", font="arial 8 italic").grid(row=7, column=0, columnspan=2)
            else:
                c = askyesno('No Booking Record' , 'Do you want to book seat now?')

                if c==True:
                    root.destroy()
                    self.seatbooking()

        Button(frame3, text='Check Booking', command=check).grid(row=0, column=2, padx=10)
        connection.commit()
        root.mainloop()

    def addbusdetails(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()

        def newoperator():
            root.destroy()
            self.addoperator()

        def newbus():
            root.destroy()
            self.addbus()

        def newroute():
            root.destroy()
            self.addroute()

        def newrun():
            root.destroy()
            self.addrun()
        
        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)

        Label(frame2, text="Add New Details to DataBase", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=30)

        
        Button(frame3, text='New Operator', fg='black', command=newoperator,
               bg='light green').grid(row=3, column=2, padx=20)
        Button(frame3, text='New Bus', fg='black', command=newbus,
               bg='orange red').grid(row=3, column=3, padx=20)
        Button(frame3, text='New Route', fg='black', command=newroute,
               bg='steelBlue1').grid(row=3, column=4, padx=20)
        Button(frame3, text='New Run', fg='black', command=newrun,
               bg='rosy brown').grid(row=3, column=5, padx=20)

        root.mainloop()

    def addoperator(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        connection = database.connect()

        #Frames
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()

        #Header
        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()
        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Add Bus Operator Details", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=30)



        Label(frame3, text="Operator ID").grid(row=0, column=0)
        op = Entry(frame3, width=10)
        op.grid(row=0, column=1)

        Label(frame3, text="Name").grid(row=0, column=2)
        nm = Entry(frame3, width=20)
        nm.grid(row=0, column=3)

        Label(frame3, text="Address").grid(row=0, column=4)
        ad = Entry(frame3, width=20)
        ad.grid(row=0, column=5)

        Label(frame3, text="Phone").grid(row=0, column=6)
        ph = Entry(frame3, width=12)
        ph.grid(row=0, column=7)

        Label(frame3, text="Email").grid(row=0, column=8)
        mail = Entry(frame3, width=20)
        mail.grid(row=0, column=9)

        def print_details():
            Label(frame3, text=op.get()+' '+nm.get()+' '+ad.get()+' '+ph.get()+' '+mail.get()
                  ).grid(row=1, column=0, columnspan=10)

        def add():
            print_details()
            check = database.check_operator(connection, op.get())
            if (check):
                showerror('DB Insertion Error','Record Already Exists...')
            else:
                database.add_bus_operator(int(op.get()), nm.get(), ad.get(), int(ph.get()), mail.get())
                showinfo('Operator Entry' , 'Operator Record Added!')
            

        def edit():
            print_details()
            check = database.check_operator(connection, op.get())
            if (check):
                database.edit_operator(nm.get(), ad.get(), int(ph.get()), mail.get(), int(op.get()))
                showinfo('Operator Entry Update' , 'Operator Recoed Updated Successfully!')
            else:
                showerror('DB Insertion Error',"Operator Doesn't Exists...")

        def home():
            root.destroy()
            self.menu()

        Button(frame3, text='Add', command=add, fg='black',
               bg='light green').grid(row=0, column=10, padx=10)
        Button(frame3, text='Edit', command=edit, fg='black',
               bg='light green').grid(row=0, column=11)

        img1 = PhotoImage(file=".\\home.png")
        Button(frame3, fg='black', bg='light green', command=home,
               image=img1).grid(row=1, column=8, columnspan=2, pady=20)

        root.mainloop()

    def addbus(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        connection = database.connect()

        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()

        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Add Bus Details", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=30)


        Label(frame3, text="Bus ID").grid(row=0, column=0)
        bid = Entry(frame3, width=15)
        bid.grid(row=0, column=1)

        bus_type = StringVar()
        bus_type.set('AC 2X2')
        options = ['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2',
                    'AC-Sleeper 2X1','Non-AC Sleeper 2X1']
        Label(frame3, text="Bus Type").grid(row=0, column=2)
        menu = OptionMenu(frame3, bus_type, *options)
        menu.grid(row=0, column=3)

        Label(frame3, text="Capacity").grid(row=0, column=4)
        capacity = Entry(frame3, width=15)
        capacity.grid(row=0, column=5)

        Label(frame3, text="Fare Rs").grid(row=0, column=6)
        fare = Entry(frame3, width=15)
        fare.grid(row=0, column=7)

        Label(frame3, text="Opeartor ID").grid(row=0, column=8)
        opid = Entry(frame3, width=15)
        opid.grid(row=0, column=9)

        Label(frame3, text="Route ID").grid(row=0, column=10)
        rid = Entry(frame3, width=15)
        rid.grid(row=0, column=11)

        def print_details():
            Label(frame3, text=bid.get()+' '+bus_type.get()+' '+capacity.get()+
                  ' '+fare.get()+' '+opid.get()+' '+rid.get()
                  ).grid(row=1, column=0, columnspan=12)

        def add():
            print_details()
            check = database.check_bus(connection, int(bid.get()))
            if (check):
                showerror('DB Insertion Error','Record Already Exists...')
            else:
                database.add_bus(connection, int(bid.get()), bus_type.get(), int(capacity.get()), int(fare.get()), int(opid.get()), int(rid.get()))
                showinfo('Bus Entry','Bus Record Added!')

        def edit():
            print_details()
            check = database.check_bus(connection, int(bid.get()))
            if (check):
                database.edit_bus(connection, bus_type.get(), int(capacity.get()), int(fare.get()), int(opid.get()), int(rid.get()), int(bid.get()) )
                showinfo('Bus Entry','Bus Record Edited Successfully!')
            else:
                showerror('DB Insertion Error',"Bus Doesn't Exists...")

        def home():
            root.destroy()
            self.menu()


        Button(frame3, text='Add Bus', fg='black', command=add,
               bg='light green').grid(row=2, column=5, pady=30)

        Button(frame3, text='Edit Bus', fg='black', command=edit,
               bg='light green',).grid(row=2, column=6, pady=30)
        img1 = PhotoImage(file=".\\home.png")
        Button(frame3, fg='black', bg='light green', command=home,
               image=img1).grid(row=2, column=7, padx=20)

        root.mainloop()

    def addroute(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        connection = database.connect()

        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()

        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Enter Journey Details", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=30)


        Label(frame3, text="Route Id").grid(row=0, column=0)
        rid = Entry(frame3, width=20)
        rid.grid(row=0, column=1)

        Label(frame3, text="Station Name").grid(row=0, column=2)
        nm = Entry(frame3, width=20)
        nm.grid(row=0, column=3)

        Label(frame3, text="Station Id").grid(row=0, column=4)
        sid = Entry(frame3, width=20)
        sid.grid(row=0, column=5)

        def print_details():
            Label(frame3, text=rid.get()+' '+nm.get()+' '+sid.get()
                  ).grid(row=1, column=0, columnspan=6)

        def add():
            print_details()
            check = database.check_route(connection, int(rid.get()))
            if (check):
                showerror('DB Insertion Error','Route Already Exists...')
            else:
                database.add_route(connection, int(rid.get()), int(sid.get()), nm.get())
                showinfo('Bus Entry','Route Record Added Successfully!')

        def delete():
            print_details()
            check = database.check_route(connection, int(rid.get()))
            if (check):
                database.delete_route(connection, int(rid.get()), int(sid.get()))
                showinfo('Bus Entry','Route Deleted Successfully!')
            else:
                showerror('DB Insertion Error',"Route Doesn't Exists...")

        def home():
            root.destroy()
            self.menu()


        Button(frame3, text='Add Route', fg='black', command=add,
               bg='light green').grid(row=0, column=6, padx=10)
        Button(frame3, text='Delete Route', fg='black', command=delete,
               bg='Red').grid(row=0, column=7)

        img1 = PhotoImage(file=".\\home.png")
        Button(frame3, fg='black', bg='light green', command=home,
               image=img1).grid(row=1, column=7, pady=20)

        root.mainloop()

    def addrun(self):
        root = Tk()
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        connection = database.connect()

        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()

        bus = PhotoImage(file="Bus_for_project.png")
        Label(frame1, image=bus).pack()

        Label(frame2, text="Online Bus Booking System", font="arial 18 bold",
              bg='sky blue', fg='Red').grid(row=0, column=0)
        Label(frame2, text="Enter Journey Details", font="arial 14 bold",
              bg='light green', fg='green').grid(row=1, column=0, pady=30)



        Label(frame3, text="Bus Id").grid(row=0, column=0)
        bid = Entry(frame3, width=20)
        bid.grid(row=0, column=1)

        Label(frame3, text="Running Date").grid(row=0, column=2)
        date = Entry(frame3, width=20)
        date.grid(row=0, column=3)

        Label(frame3, text="Seat Available").grid(row=0, column=4)
        seatavail = Entry(frame3, width=20)
        seatavail.grid(row=0, column=5)

        def print_details():
            Label(frame3, text=bid.get()+' '+date.get()+' '+seatavail.get()
                  ).grid(row=1, column=0, columnspan=6)

        def add():
            print_details()
            check = database.check_running_details(connection, int(bid.get()), date.get())
            if (check):
                showerror('DB Insertion Error','Already Running...')
            else:
                database.add_running_details(connection, int(bid.get()), date.get(), int(seatavail.get()))
                showinfo('Running Entry','Running Details Added Successfully!')

        def delete():
            print_details()
            check = database.check_running_details(connection, int(bid.get()), date.get())
            if (check):
                database.delete_running_details(connection, int(bid.get()), date.get())
                showinfo('Delete Entry','Running Details Deleted Successfully!')
            else:
                showerror('DB Insertion Error',"Running Details Doesn't Exists...")

        def home():
            root.destroy()
            self.menu()

        Button(frame3, text='Add Run', fg='black', command=add,
               bg='light green').grid(row=0, column=6, padx=10)
        Button(frame3, text='Delete Run', fg='black', command=delete,
               bg='Red').grid(row=0, column=7)

        img1 = PhotoImage(file=".\\home.png")
        Button(frame3, fg='black', bg='light green', command=home,
               image=img1).grid(row=1, column=7, pady=20)

        root.mainloop()


    

    

run = Project()


