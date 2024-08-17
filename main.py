from tkinter import *
import requests

def get_quote():
    connection = requests.get("https://api.kanye.rest")
    if connection.raise_for_status():
        raise ConnectionError

    con_json = connection.json()
    the_quote = con_json["quote"]
    print(the_quote)
    canvas.itemconfig(quote_text, text=the_quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 248, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()


