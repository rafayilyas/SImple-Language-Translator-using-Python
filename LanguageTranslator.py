from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def change(text="Type", src="English", dest="Urdu"):
    try:
        trans = Translator()
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    except Exception as e:
        messagebox.showerror("Error", "Translation failed: " + str(e))
        return ""

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END).strip()
    
    if s not in LANGUAGES.values() or d not in LANGUAGES.values():
        messagebox.showwarning("Warning", "Please select valid source and destination languages.")
        return
    
    if not msg:
        messagebox.showinfo("Info", "Please enter text to translate.")
        return
    
    gettext = change(text=msg, src=s, dest=d)
    des_txt.delete(1.0, END)
    des_txt.insert(END, gettext)

# GUI Setup
root = Tk()
root.title("Language Translator App")
root.geometry("550x750")
root.config(bg='#f2f5f9')  # Light grayish blue background for a calm look

# Title with Emoji
Label(root, text="🌐 Language Translator 🌐", font=("Arial", 30, "bold"), bg='#f2f5f9', fg="#333333").pack(pady=15)

# Source Text Area with Emoji
Label(root, text="📄 Source Text", font=("Arial", 18, "bold"), fg='#1a1a1a', bg='#f2f5f9').place(x=50, y=70)
Sor_txt = Text(root, font=("Arial", 12), wrap=WORD, relief=SOLID, borderwidth=2, bg="#ffffff", fg="#333333")
Sor_txt.place(x=50, y=110, height=120, width=450)

# Language Selection Labels and Dropdowns
list_txt = list(LANGUAGES.values())

Label(root, text="🌍 From:", font=("Arial", 12, "bold"), fg="#1a1a1a", bg="#f2f5f9").place(x=50, y=250)
comb_sor = ttk.Combobox(root, value=list_txt, font=("Arial", 12))
comb_sor.place(x=120, y=250, height=30, width=150)
comb_sor.set("Select Language")

Label(root, text="➡️ To:", font=("Arial", 12, "bold"), fg="#1a1a1a", bg="#f2f5f9").place(x=300, y=250)
comb_dest = ttk.Combobox(root, value=list_txt, font=("Arial", 12))
comb_dest.place(x=350, y=250, height=30, width=150)
comb_dest.set("Select Language")

# Translate Button with Emoji
button_change = Button(root, text="Translate 🔄", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", relief=RAISED, command=data)
button_change.place(x=200, y=310, height=40, width=150)

# Destination Text Area with Emoji
Label(root, text="📄 Destination Text", font=("Arial", 18, "bold"), fg='#1a1a1a', bg='#f2f5f9').place(x=50, y=370)
des_txt = Text(root, font=("Arial", 12), wrap=WORD, relief=SOLID, borderwidth=2, bg="#ffffff", fg="#333333")
des_txt.place(x=50, y=410, height=120, width=450)

# Footer Label with Emoji
Label(root, text="🌍 Translate across 100+ languages with ease! 🌏", font=("Arial", 10, "italic"), fg="#1a1a1a", bg="#f2f5f9").pack(side=BOTTOM, pady=20)

root.mainloop()
