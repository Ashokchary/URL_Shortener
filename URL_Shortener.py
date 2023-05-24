#Importing all necessary modules
import tkinter
import pyshorteners

#Function
def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))
    
#Creating Window
root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("300x300")
root.config()

#Configuring Window and Labelling
longurl_label = tkinter.Label(root, text="Enter Long URL",font=("Arial",20))
longurl_entry = tkinter.Entry(root,font=("Arial",14))
shorturl_label=tkinter.Label(root, text="Output shortened URL",font=("Arial",17)) 
shorturl_entry = tkinter.Entry(root,font=("Arial",14))
shorten_button = tkinter.Button(root, text="Shorten URL",font=("Arial",15),command=shorten)

#Placing the Labels and Entry
longurl_label.pack(pady=10)
longurl_entry.pack(pady=10)
shorturl_label.pack(pady=10)
shorturl_entry.pack(pady=10)
shorten_button.pack(pady=10)

root.mainloop()
