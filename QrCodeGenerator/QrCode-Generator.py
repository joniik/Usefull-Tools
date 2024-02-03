import qrcode
import customtkinter
import os
from PIL import Image
import time

current_path = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = 'qr_code.png'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

def button_callback():
    global IMAGE_PATH
    user_input = message_textbox.get("1.0", "end-1c")

    print("button clicked")

    qr.add_data(user_input)
    qr.make(fit=True)

    bg = (255, 255, 255) # Taustan väri 
    fg = (255, 0,0) # Qr Koodin Väri

    img = qr.make_image(back_color=(bg), fill_color=(fg))

    img.save(os.path.join(current_path, "qr_code.png"))

    print(IMAGE_PATH)

timestart = time.time()

def update():
    global IMAGE_PATH, timestart
    if time.time() - timestart >= 0.5:
        timestart = time.time()
        IMAGE_PATH = 'qr_code.png'
        print("refresh")
        kuva.configure(light_image=Image.open(IMAGE_PATH))
    app.after(10, update)

app = customtkinter.CTk()
app.geometry("400x700")

IMAGE_WIDTH = 300   
IMAGE_HEIGHT = 300

message_label = customtkinter.CTkLabel(app, text="Write what you want to QrCode:")
message_label.place(x=50, y=20)

message_textbox = customtkinter.CTkTextbox(app, width=300, height=200)
message_textbox.place(x=50, y=50)

button = customtkinter.CTkButton(app, text="Generate QR Code", command=button_callback)
button.place(x=200, y=300, anchor="center")

kuva = customtkinter.CTkImage(light_image=Image.open(IMAGE_PATH), size=(IMAGE_WIDTH, IMAGE_HEIGHT))
label = customtkinter.CTkLabel(master=app, image=kuva, text='')
label.place(x=50, y=350)

app.after(10, update)
app.mainloop()
