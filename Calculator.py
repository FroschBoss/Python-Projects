import tkinter as tk #used for graphical interfaces
from tkinter import ttk #used for themed widgets

def handle_button_click(clicked_button_text): #gets called every time a button if cliecked
    current_text = result_var.get() #takes the text of the clicked button
    
    if clicked_button_text == "=":
        try:
            expression = current_text.replace("÷","/").replace("×","*") 
            result = eval(expression)
            #using this to replace custom symbols with Python symbols/operators like / for divide and * for multiplication
            
            if result.is_integer():
                result = int(result) #checks if the result is an integer
                
            result_var.set(result) 
        except Exception as e:
            result_var.set("Error") #used to catch any errors like if it can't calculate a certain operation
            
    elif clicked_button_text == "AC": 
        result_var.set("") #used to clear the calculator
    
    elif clicked_button_text == "%": #convert the current number into a decimal by dividing it by 100
        try: 
            current_number = float(current_text)
            result_var.set(current_number / 100) #divides the current result by 100 to make it into a decimal
        except ValueError: #if it can't then it will be marked as an error
            result_var.set("Error")
    
    elif clicked_button_text == "±": #converts the current number into it's negative
        try:
            current_number = float(current_text) #turns the current number that is in string form into a float
            result_var.set(-current_number) #sets the current_number to be the negative of itself
        except ValueError: #error checking
            result_var.set("Error")
    else: result_var.set(current_text + clicked_button_text) #used for the other buttons and appends the clicked buttons text to the current text in the result entry of the calculator
 
# Creates the window    
root = tk.Tk()
root.title("Calculator")
# Entry Widgrt to display the result with larger font size
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var,
font = ("Helvectica", 24), justify = "right")
result_entry.grid(row=0, column=0, columnspan=4,sticky="nsew") #assigned widget to a gridlayer

# Button Layer
buttons = [
    ("AC",1,0), ("±",1, 1), ("%",1,2), ("÷",1,3),
    ("7",2,0), ("8",2,1), ("9",2,2), ("×",2,3),
    ("4",3,0), ("5",3,1), ("6",3,2), ("-",3,3),
    ("1",4,0), ("2",4,1), ("3",4,2), ("+",4,3),
    ("0",5,0,2), (".",5,2), ("=",5,3)
]

#styling the button
style = ttk.Style()
style.theme_use('default')
style.configure("TButoon", font=("Helvetica", 16), width = 10, height = 4)

#Creating the buttons
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    #^using lambda to associate every button with the handle _button_click
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)  #buttons are added to the grid with properties like columnspan

   
#Configure row and column weight (make it so they expand proportionally)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    
#setting the window size and other settings
width = 500 #width of the window
height = 700 #height of the window
root.geometry(f"{width}x{height}")

root.resizable(False,False) #makes the window non-reizable

#keyboard control
root.bind("<Return>",lambda event: handle_button_click("=")) #binding the equals botton to the enter key
root.bind("<BackSpace>",lambda event: handle_button_click("AC"))   #binding the clear button to the delete key

root.mainloop()      
            