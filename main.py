from tkinter import *

def on_submit(event=None):
    input_text = questionField.get()
    textarea.insert("end", "You: " + input_text + "\n")  # Display the user input
    questionField.delete(0, 'end')  # Clear the input area

def create_gradient(canvas, color1, color2):
    w, h = canvas.winfo_reqwidth(), canvas.winfo_reqheight()
    for i in range(w):
        r = int((i / w) * (int(color2[1:3], 16) - int(color1[1:3], 16)) + int(color1[1:3], 16))
        g = int((i / w) * (int(color2[3:5], 16) - int(color1[3:5], 16)) + int(color1[3:5], 16))
        b = int((i / w) * (int(color2[5:], 16) - int(color1[5:], 16)) + int(color1[5:], 16))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(i, 0, i, h, fill=color, tags='gradient')

root = Tk()
root.geometry('370x456+100+30')
root.title('Chatbot')
root.resizable(False, False)

# Linear gradient red for the area holding logopic
logopic_frame = Frame(root, height=50)  # Decreased height
logopic_frame.pack(fill=X)

canvas = Canvas(logopic_frame, width=370, height=50, highlightthickness=0)
canvas.pack()
create_gradient(canvas, '#FF0000', '#FF4500')  # Linear gradient from red to dark red

LogoPic = PhotoImage(file='chatbot2-icon.png')
LogopicLabel = Label(logopic_frame, image=LogoPic)
LogopicLabel.place(x=10, y=0)

# Text alongside the logopic
text_label = Label(logopic_frame, text="Kasturbha Hospital HelpDesk", font=('times new roman', 12, 'bold'), fg='white', bg='#FF4500')
text_label1 = Label(logopic_frame, text="We are online to assist you", font=('times new roman', 10, 'bold'), fg='white', bg='#FF4500')
text_label.place(x=95, y=4)
text_label1.place(x=130, y=30)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

# White background for the displayed area
textarea = Text(centerFrame, font=('times new roman', 12, 'normal'), height=18.5, yscrollcommand=scrollbar.set, bg='white')
textarea.pack()
scrollbar.config(command=textarea.yview)

# Add a welcome message without splitting words
welcome_message = "Good evening. Welcome to Kasturba Hospital \n HelpDesk. \n Kasturba Hospital has emerged as a premier healthcare \n institution providing quality tertiary care to both domestic and international patients.\n"
textarea.insert("end", "Bot: " + welcome_message)

# Frame to hold the input area and submit button with an orange background
input_frame = Frame(root, bg='#FFA500')  # Orange color
input_frame.pack(side=BOTTOM, pady=15, padx=5, fill=X)

# Orange border for the input area
questionField = Entry(input_frame, font=('times new roman', 12, 'normal'), width=36, bd=4, bg='white')  # White background
questionField.pack(side=LEFT, padx=10)

# Bind the <Return> key to the on_submit function
questionField.bind('<Return>', on_submit)

# Submit button with an icon
submit_icon = PhotoImage(file='submit-button.png')  # Replace with your icon file
submit_button = Button(input_frame, image=submit_icon, command=on_submit, bd=1, bg='red')  # Orange background
submit_button.pack(side=LEFT, padx=5, pady=5)

# Move the input frame up a bit
input_frame.pack_configure(pady=5)

root.mainloop()
