# python_project

# (NOTE)---this is complete code of this project if you want to get seprat code of scanner and gui then comment on.

import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from pyzbar.pyzbar import decode
import cv2
from csv import writer
import csv
from tkinter import ttk

gui_root= Tk()

gui_root.title("SMART ATTNDANCE SYSTEAM")

gui_root.geometry("850x550")

def scan_qr():
    print("Scan Button Pressed!")

    com = cv2.VideoCapture(0)
    com.set(3, 640) # Set the width
    com.set(4, 480) # Set the height
    while True:
        success, frame = com.read()
        
        if not success:
            break
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type
            # print(f"Type: {barcode_type}, Data: {barcode_data}")
            # frame = cv2.draw()
            print(barcode_data)
        
        cv2.imshow("Show Your QR Code", frame)
        
        if cv2.waitKey(100) & 0xFF == 27: # Press 'ESC' to exit
            break
        if decoded_objects != []:
            with open('attendance.csv', 'a',newline='') as f_object:
            # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(f_object)
            
                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow([barcode_data])
            
                # Close the file object
                f_object.close()
            break

    com.release()
    cv2.destroyAllWindows()

def show_attendance():
    class CSVTableApp:
        def __init__(self, root):
            self.root = root
            self.root.title("CSV Table Viewer")

            # Create a Treeview widget
            self.tree = ttk.Treeview(root, show="headings")
            self.tree.pack(expand=True, fill="both")

            # Add a vertical scrollbar
            scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
            scrollbar.pack(side="right", fill="y")
            self.tree.configure(yscrollcommand=scrollbar.set)

            # Load CSV data into the table
            self.load_csv_data("attendance.csv")

        def get_headers(self):
            # Read the first row of the CSV file to get column headers
            with open("attendance.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                headers = next(csv_reader)
            return headers

        def load_csv_data(self, file_path):
            # Clear existing data in the treeview
            self.tree.delete(*self.tree.get_children())

            # Read CSV data and insert it into the treeview
            with open(file_path, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                headers = next(csv_reader)
                self.tree["columns"] = headers
                for header in headers:
                    self.tree.heading(header, text=header)
                    self.tree.column(header, anchor="center", width=100)
                for index, row in enumerate(csv_reader, start=1):
                    self.tree.insert("", "end", iid=index, values=tuple(row))

    root = tk.Tk()
    app = CSVTableApp(root)
    root.mainloop()


# <------------------------------------------------adding the image

# Add image file
 
bg = PhotoImage( file = "test.png") 

# Show image using label 

GUI_IMAGE = Label( gui_root, image = bg) 
GUI_IMAGE.place(x = 0,y = 0) 

# Add text 

GUI_IMAGE= Label(gui_root, text ="SMART ATTEANDANCE SYASTEAM",bg="white",
                 font=("Algerian","40","bold"))

GUI_IMAGE.pack(pady="200") 


#<-----------------------------------------------------Creating Two Buttons


#{1} scan the QR Code

Frame=Frame(gui_root,bg="black",borderwidth="4")
Frame.pack()
 
b1=Button(Frame,fg="blue",text="SCAN QR",height="2",width="20",bg="yellow"
           ,font=("Agbalumo","16","bold"),borderwidth="10",relief="sunken",command=scan_qr)

b1.pack(side="left",anchor="center")



#{2}2 Show Attendance

b2=Button(Frame,fg="red",text="SHOW ATTENDANCE",height="2",width="20",bg="yellow",
          font=("Agbalumo","16","bold"),borderwidth="10",relief="sunken",command=show_attendance)

b2.pack(side="right",anchor="nw")


gui_root.mainloop()
