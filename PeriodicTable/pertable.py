import tkinter as tk
from Tech_In_Seconds import agl

eleList = agl.AllChemElements()
root = tk.Tk()
root.title("Periodic Table by Aadesh Lokhande")
root.configure(bg="grey7")
root.resizable(0, 0)

mainframe = tk.Frame(root, bg="grey7")
mainframe.pack()


def info(event):
    outputWindow = tk.Tk()
    outputWindow.configure(bg="grey7")
    outputWindow.resizable(0, 0)

    def des():
        outputWindow.destroy()

    text = event.widget.cget("text").split("\n")[0]
    dic = agl.chemEleInfo(text)
    list = ["Atomic number", "Relative atomic mass", "Standard state", "Classification", 
            "Group", "Group name", "Period", "Block", "Shell structure", "CAS Registry"]

    eleBtn = tk.Button(outputWindow,
                        text=f"{dic['Name'].upper()}",
                        bg="grey7",
                        fg="green",
                        font=("Arial", 20, "bold"),
                        height=2,
                        width=60)
    eleBtn.grid(row=0, column=0, columnspan=2)

    for i in range(1, 11):
        outputWindow.title(f"This information about {dic['Name']}")
        b1Btn = tk.Button(outputWindow,
                            text=list[i - 1].upper(),
                            bg="grey7",
                            fg="white",
                            font=("Arial", 20, "bold"),
                            height=1,
                            width=30)
        b1Btn.grid(row=i, column=0)

        b2Btn = tk.Button(outputWindow,
                            text=f"{dic[list[i - 1]]}",
                            bg="grey7",
                            fg="white",
                            justify="right",
                            font=("Arial", 20, "bold"),
                            height=1,
                            width=30)
        b2Btn.grid(row=i, column=1)

    bkBtn = tk.Button(outputWindow,
                        text="Back",
                        justify="left",
                        fg="red",
                        bg="grey7",
                        font=("Arial", 20, "bold"),
                        height=2,
                        width=60,
                        command=des)
    bkBtn.grid(row=11, column=0, columnspan=2)
    outputWindow.mainloop()
a = 0

def myinfo():
    global a
    if (a % 2 == 0):
        ttlBtn.configure(text="Created By:\nAadesh Lokhande", font=("Arial", 30, "bold"))
    else:
        ttlBtn.configure(text="Periodic Table", font=("Arial", 30, "bold"))
    a += 1

for element in eleList:
    dic = agl.chemEleInfo(element)
    button = tk.Button(
                mainframe,
                text=f"{element}\n{dic['Name']}",
                width=11,
                height=3,
                font=("Arial", 10, "bold"),
                borderwidth=1,
                relief="solid",
            )
    block = dic['Block']
    if (block == "p"):
        button.configure(bg="yellow", fg="black")
    elif (block == "d"):
        button.configure(bg="blue", fg="white")
    elif (block == "s"):
        button.configure(bg="red", fg="white")
    elif (block == "f"):
        button.configure(bg="green", fg="white")

    button.grid(row=dic["row"], column=dic["col"])
    button.bind("<Button-1>", info)

ttlBtn = tk.Button(
    mainframe,
    text="Periodic Table".upper(),
    width=20,
    height=2,
    bg="grey7",
    fg="white",
    font=("Arial", 30, "bold"),
    activebackground="grey7",
    activeforeground="cadet blue",
    command=myinfo,
    relief="solid")
ttlBtn.grid(row=1, column=5, columnspan=7, rowspan=3)
root.mainloop()
