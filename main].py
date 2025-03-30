import customtkinter
from httpFunctions import startWithIndex
from customtkinter import*


app = CTk()
app.title("Text Editor")
app.geometry("2560x1600")
set_appearance_mode("dark")
#functions


#frames
frame = CTkFrame(master=app,fg_color="#FFFFFF", border_color='#FFFFFE', border_width=2, width=1900, height=200)
frame.grid(row=0, column=0, padx=10, pady=10)

#fonts
my_font = customtkinter.CTkFont(family="Poppins", size=75, weight="bold", )

my_font2 = customtkinter.CTkFont(family="sans serif", size=25, weight="normal",)

#labels
label = CTkLabel(master=frame, text="Easy file sharing",font=(my_font,70,'bold'), text_color='black')
#label.grid(row=0, column=0, padx=10, pady=10)
label.place(relx=0.5,rely=0.4, anchor=CENTER)

label = CTkLabel(master=frame, text="hello did this work", font=(my_font))

#buttons
button = CTkButton(master=app,command=lambda : start('192.168.1.111', 8000), text="Launch Server")
button.place(relx=0.5,rely=0.5,anchor=CENTER)
app.mainloop()