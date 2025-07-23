from tkinter import *
import tkinter.messagebox as mb
from  tkinter import ttk
from time import strftime

# colur theme 
themeclr = "cadet blue"
accent = "powder blue"

root = Tk()
root.title("Real Estate Price Estimation")
root.configure(bg=themeclr)
root.geometry("1050x700")
root.minsize(width=1050,height=720)
root.maxsize(width=1050,height=720)

# buttons Functions 
def time():
    string = strftime('%d %b %Y %I:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

def reset():
    superAreaVar.set("Choose Option")
    availabiltyVar.set("Choose Option")
    locationVar.set("Choose Option")
    sizeBHKVar.set("Choose Option")
    societyVar.set("Choose Option")
    totalSQFTVar.set("Choose Option")
    bathVar.set("Choose Option")
    balconyVar.set("Choose Option")
    rangeVar.set("Min-Max")

def availabiltyFn():
    superAreaVaar = superAreaVar.get().lower()
    availabiltyVaar = availabiltyVar.get().lower()
    locationVaar = locationVar.get().lower()
    sizeBHKVaar = str(sizeBHKVar.get()).lower()
    societyVaar = str(societyVar.get()).lower()
    rangeVaar = str(rangeVar.get()).lower()
    bathVaar = str(bathVar.get()).lower()
    balconyVaar = str(balconyVar.get()).lower() 
    
    file = open("UpdatedData.csv","r")
    lines = file.read().lower().split("\n")
    superAreaList = []
    for line in lines:
        data = line.split(',')
        if(data[0]==superAreaVaar or superAreaVaar=="choose option"):
            superAreaList.append(line)

    availabiltyList = []
    for line in lines:
        data = line.split(",")
        if(data[1] == availabiltyVaar or availabiltyVaar == "choose option"):
            availabiltyList.append(line)

    locationList = []
    for line in lines:
        data = line.split(',')
        if(data[2]==locationVaar or locationVaar=="choose option"):
            locationList.append(line)    
    
    sizeBHKList = []
    for line in lines:
        data = line.split(',')
        if(data[3]==sizeBHKVaar or sizeBHKVaar=="choose option"):
            sizeBHKList.append(line)
    

    societyList = []
    for line in lines:
        data = line.split(',')
        if(data[4]==societyVaar or societyVaar=="choose option"):
            societyList.append(line)
    
    totalSQFTList = []
    for line in lines:
        data = line.split(',')
        if(rangeVaar=="min-max"):
            totalSQFTList.append(line)
        rangeTotal = rangeVaar.split('-')
        try:
            if(int(data[5].strip()) >= int(rangeTotal[0].strip()) and int(data[5].strip()) <= int(rangeTotal[1].strip())):
                totalSQFTList.append(line)
        except:
            pass

    bathList = []
    for line in lines:
        data = line.split(',')
        if(data[6]==bathVaar or bathVaar=="choose option"):
            bathList.append(line)
    
    balconyList = []
    for line in lines:
        data = line.split(',')
        if(data[7]==balconyVaar or balconyVaar=="choose option"):
            balconyList.append(line)
    
    file.close()

    linesSet = set(lines)
    superAreaSet = set(superAreaList)
    availabiltySet = set(availabiltyList)
    locationSet = set(locationList)
    sizeBHKSet = set(sizeBHKList)
    societySet = set(societyList)
    totalSQFTSet = set(totalSQFTList)
    bathSet = set(bathList)
    balconySet = set(balconyList)

    linesSet.intersection_update(superAreaSet)
    linesSet.intersection_update(availabiltySet)
    linesSet.intersection_update(locationSet)
    linesSet.intersection_update(sizeBHKSet)
    linesSet.intersection_update(societySet)
    linesSet.intersection_update(totalSQFTSet)
    linesSet.intersection_update(bathSet)
    linesSet.intersection_update(balconySet)

    ans = mb.askquestion("Details",f"Total Details available = {len(linesSet)}\nDo you want to see Data?")
    titleList = "Var_SuperbuiltupArea,Var_availability,Var_location,Var_size_BHK,Var_society,Var_total_sqft,Var_bath,Var_balcony,Var_price(in Rupees)".split(",")
    
    table['columns'] = titleList
    table.column("#0", width=0,  stretch=NO)
    table.column("Var_SuperbuiltupArea", anchor=CENTER, width=40)
    table.column("Var_availability", anchor=CENTER, width=40)
    table.column("Var_location", anchor=CENTER, width=40)
    table.column("Var_size_BHK", anchor=CENTER, width=40)
    table.column("Var_society", anchor=CENTER, width=40)
    table.column("Var_total_sqft", anchor=CENTER, width=40)
    table.column("Var_bath", anchor=CENTER, width=40)
    table.column("Var_balcony", anchor=CENTER, width=40)
    table.column("Var_price(in Rupees)", anchor=CENTER, width=40)
    
    table.heading("#0")
    table.heading("Var_SuperbuiltupArea", text = "Super built-up Area" ,anchor=CENTER)
    table.heading("Var_availability", text = "availability" ,anchor=CENTER)
    table.heading("Var_location", text = "location" ,anchor=CENTER)
    table.heading("Var_size_BHK", text = "size_BHK" ,anchor=CENTER)
    table.heading("Var_society", text = "society" ,anchor=CENTER)
    table.heading("Var_total_sqft", text = "total_sqft" ,anchor=CENTER)
    table.heading("Var_bath", text = "bath" ,anchor=CENTER)
    table.heading("Var_balcony", text = "balcony" ,anchor=CENTER)
    table.heading("Var_price(in Rupees)", text = "price(in Rupees)" ,anchor=CENTER)


    linesList = list(linesSet)
    listData = []
    a = 0
    if(ans == "yes"):
        MenuFrame.pack_forget()
        secondFrame.pack(fill=BOTH,expand=TRUE)
        btnFrame.pack(fill=BOTH,side = BOTTOM)

        for line in linesList:
            line = line.split(",")
            if(len(line)==9):
                a +=1
                table.insert(parent='',index='end',iid=a,text='',values=line)
    table.pack()



def backFn():
    secondFrame.pack_forget()
    btnFrame.pack_forget()
    MenuFrame.pack()

def show():
    superAreaVaar = superAreaVar.get().lower()
    availabiltyVaar = availabiltyVar.get().lower()
    locationVaar = locationVar.get().lower()
    sizeBHKVaar = sizeBHKVar.get().lower()
    societyVaar = societyVar.get().lower()
    totalSQFTVaar = totalSQFTVar.get().lower()
    bathVaar = bathVar.get().lower()
    balconyVaar = balconyVar.get().lower()

    file = open("UpdatedData.csv","r")
    lines = file.read().lower().split("\n")
    for line in lines:
        data = line.split(',')
        if(superAreaVaar==data[0] and availabiltyVaar==data[1] and locationVaar==data[2] and sizeBHKVaar==data[3] and societyVaar==data[4] and totalSQFTVaar==data[5] and bathVaar==data[6] and balconyVaar==data[7]):
            price = int(data[8])
            sqft = int(totalSQFTVaar)
            mb.showinfo('Total Price',f"Price = {price*sqft*74} Rs")

def sortData():
    superAreaVaar = superAreaVar.get().lower()
    availabiltyVaar = availabiltyVar.get().lower()
    locationVaar = locationVar.get().lower()
    sizeBHKVaar = str(sizeBHKVar.get()).lower()
    societyVaar = str(societyVar.get()).lower()
    totalSQFTVaar = str(totalSQFTVar.get()).lower()
    bathVaar = str(bathVar.get()).lower()
    balconyVaar = str(balconyVar.get()).lower() 
    

    file = open("UpdatedData.csv","r")
    lines = file.read().lower().split("\n")
    superAreaList = []
    for line in lines:
        data = line.split(',')
        if(data[0]==superAreaVaar or superAreaVaar=="choose option"):
            superAreaList.append(line)

    availabiltyList = []
    for line in lines:
        data = line.split(",")
        if(data[1] == availabiltyVaar or availabiltyVaar == "choose option"):
            availabiltyList.append(line)

    locationList = []
    for line in lines:
        data = line.split(',')
        if(data[2]==locationVaar or locationVaar=="choose option"):
            locationList.append(line)    
    
    sizeBHKList = []
    for line in lines:
        data = line.split(',')
        if(data[3]==sizeBHKVaar or sizeBHKVaar=="choose option"):
            sizeBHKList.append(line)
    

    societyList = []
    for line in lines:
        data = line.split(',')
        if(data[4]==societyVaar or societyVaar=="choose option"):
            societyList.append(line)
    
    totalSQFTList = []
    for line in lines:
        data = line.split(',')
        if(totalSQFTVaar=="choose option"):
            totalSQFTList.append(line)
        rangeTotal = totalSQFTVaar.split('-')
        try:
            if(int(data[5].strip()) >= int(rangeTotal[0].strip()) and int(data[5].strip()) <= int(rangeTotal[1].strip())):
                totalSQFTList.append(line)
        except:
            pass

    bathList = []
    for line in lines:
        data = line.split(',')
        if(data[6]==bathVaar or bathVaar=="choose option"):
            bathList.append(line)
    
    balconyList = []
    for line in lines:
        data = line.split(',')
        if(data[7]==balconyVaar or balconyVaar=="choose option"):
            balconyList.append(line)
    
    file.close()
    linesSet = set(lines)
    superAreaSet = set(superAreaList)
    availabiltySet = set(availabiltyList)
    locationSet = set(locationList)
    sizeBHKSet = set(sizeBHKList)
    societySet = set(societyList)
    totalSQFTSet = set(totalSQFTList)
    bathSet = set(bathList)
    balconySet = set(balconyList)

    linesSet.intersection_update(superAreaSet)
    linesSet.intersection_update(availabiltySet)
    linesSet.intersection_update(locationSet)
    linesSet.intersection_update(sizeBHKSet)
    linesSet.intersection_update(societySet)
    linesSet.intersection_update(totalSQFTSet)
    linesSet.intersection_update(bathSet)
    linesSet.intersection_update(balconySet)
    
    superAreaList = []
    for i in linesSet:
        j = i.split(",")
        superAreaList.append(j[0])
    superAreaList = set(superAreaList)
    superAreaList = list(superAreaList)
    superAreaList.sort()
    superAreaEntry = OptionMenu(itemsFrame, superAreaVar,*superAreaList)
    superAreaEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    superAreaEntry.grid(row=0, column=3,sticky='n')

    availabiltyList = []
    for i in linesSet:
        j = i.split(",")
        availabiltyList.append(j[1])
    availabiltyList = set(availabiltyList)
    availabiltyList = list(availabiltyList)
    availabiltyList.sort()

    availabiltyEntry = OptionMenu(itemsFrame, availabiltyVar,*availabiltyList)
    availabiltyEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    availabiltyEntry.grid(row=1, column=3,sticky='n')

    locationSet = []
    for i in linesSet:
        j = i.split(",")
        locationSet.append(j[2])
    locationList = set(locationList)
    locationList = list(locationList)
    locationList.sort()

    locationSet = OptionMenu(itemsFrame, locationVar,*locationSet)
    locationSet.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    locationSet.grid(row=2, column=3,sticky='n')

    sizeBHKList = []
    for i in linesSet:
        j = i.split(",")
        sizeBHKList.append(j[3])
    sizeBHKList = set(sizeBHKList)
    sizeBHKList = list(sizeBHKList)
    sizeBHKList.sort()

    sizeBHKEntry = OptionMenu(itemsFrame, sizeBHKVar,*sizeBHKList)
    sizeBHKEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    sizeBHKEntry.grid(row=3, column=3,sticky='n')

    societyList = []
    for i in linesSet:
        j = i.split(",")
        societyList.append(j[4])
    societyList = set(societyList)
    societyList = list(societyList)
    societyList.sort()

    societyEntry = OptionMenu(itemsFrame, societyVar,*societyList)
    societyEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    societyEntry.grid(row=4, column=3,sticky='n')

    totalSQFTList = []
    for i in linesSet:
        j = i.split(",")
        totalSQFTList.append(j[5])
    totalSQFTList = set(totalSQFTList)
    totalSQFTList = list(totalSQFTList)
    totalSQFTList.sort()

    TotalSQFTEntry = OptionMenu(itemsFrame, totalSQFTVar,*totalSQFTList)
    TotalSQFTEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    TotalSQFTEntry.grid(row=5, column=3,sticky='n')

    bathList = []
    for i in linesSet:
        j = i.split(",")
        bathList.append(j[6])
    bathList = set(bathList)
    bathList = list(bathList)
    bathList.sort()
    bathEntry = OptionMenu(itemsFrame, bathVar,*bathList)
    bathEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    bathEntry.grid(row=6, column=3,sticky='n')

    balconylist = []
    for i in linesSet:
        j = i.split(",")
        balconylist.append(j[7])
    balconyList = set(balconyList)
    balconyList = list(balconyList)
    balconyList.sort()

    balconyEntry = OptionMenu(itemsFrame, balconyVar,*balconylist)
    balconyEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
    balconyEntry.grid(row=7, column=3,sticky='n')

Tops = Frame(root, bg=themeclr, bd=20, pady=2, relief=RIDGE)

lblTitle = Label(Tops, font="arial 50 bold", text="Real Estate Price Estimation", bd=10, bg=themeclr, fg="Cornsilk", justify=CENTER)
lblTitle.pack()

lblname = Label(Tops, font="arial 15 bold", text="By Rupesh Manohar Sankale", bg=themeclr, fg="Cornsilk",justify=CENTER)

lblname.pack()

Tops.pack(side=TOP, fill=BOTH)

MenuFrame = Frame(root, bg=themeclr, bd=10, relief=RIDGE)
MenuFrame.pack( fill= X )

file = open("UpdatedData.csv","r")
data = file.read().split("\n")
DataList = []
for line in data:
    lista = line.split(",")
    DataList.append(lista)
file.close()

superAreaVar = StringVar()
availabiltyVar = StringVar()
locationVar = StringVar()
sizeBHKVar = StringVar()
societyVar = StringVar()
totalSQFTVar = StringVar()
bathVar = StringVar()
balconyVar = StringVar()
rangeVar = StringVar()

superAreaVar.set("Choose Option")
availabiltyVar.set("Choose Option")
locationVar.set("Choose Option")
sizeBHKVar.set("Choose Option")
societyVar.set("Choose Option")
totalSQFTVar.set("Choose Option")
bathVar.set("Choose Option")
balconyVar.set("Choose Option")
rangeVar.set("Min-Max")

itemsFrame = Frame(MenuFrame, bg=accent, bd=8, relief=RIDGE)

superBuildUpArea = Label(itemsFrame, text="\tArea\t\t\t:-\t",  font="arial 16 bold", bg=accent,justify=RIGHT)
superBuildUpArea.grid(row=0,sticky="w")

availabilty = Label(itemsFrame, text="\tAvailability\t\t:-\t",  font="arial 16 bold", bg=accent,justify=RIGHT)
availabilty.grid(row=1,sticky="w")

location = Label(itemsFrame, text="\tLocation\t\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
location.grid(row=2,sticky="w")

sizeBHK = Label(itemsFrame, text="\tSize BHK\t\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
sizeBHK.grid(row=3,sticky="w")

society = Label(itemsFrame, text="\tSociety\t\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
society.grid(row=4,sticky="w")

totalSQFT = Label(itemsFrame, text="\tTotal SQFT\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
totalSQFT.grid(row=5,sticky="w")

bath = Label(itemsFrame, text="\tBathroom\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
bath.grid(row=6,sticky="w")

balcony = Label(itemsFrame, text="\tBalcony\t\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
balcony.grid(row=7,sticky="w")

# ++++++++++++++++++++++++++++++++
optionBuild = ["Super built-up Area", "Built-up Area", "Plot Area"]
superAreaEntry = OptionMenu(itemsFrame,superAreaVar,*optionBuild)
superAreaEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
superAreaEntry.grid(row=0, column=3,sticky='n')
confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 0,column=4)
# ++++++++++++++++++++++++++++++++++++

optionAvailabillity = ["Ready to move","Not ready to move"]
availabiltyEntry = OptionMenu(itemsFrame, availabiltyVar,*optionAvailabillity)
availabiltyEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
availabiltyEntry.grid(row=1, column=3,sticky='n')
confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 1,column=4)
# +++++++++++++++++++++++++++++++++++

optionLocation = []
for i in DataList:
    lista = i[2]
    optionLocation.append(lista)
locationEntry = OptionMenu(itemsFrame, locationVar,*optionLocation)
locationEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
locationEntry.grid(row=2, column=3,sticky='n')

confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 2,column=4)
# +++++++++++++++++++++++++++++++++++

optionSizeBHK = []
for i in DataList:
    try:
        lista = int(i[3])
        optionSizeBHK.append(lista)
    except:
        pass
optionSizeBHK = list(set(optionSizeBHK))

optionSizeBHK.sort()
sizeBHKEntry = OptionMenu(itemsFrame, sizeBHKVar,*optionSizeBHK)
sizeBHKEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
sizeBHKEntry.grid(row=3, column=3,sticky='n')

confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 3,column=4)
# +++++++++++++++++++++++++++++++++++++++++++++

optionSociety = []
for i in DataList:
    lista = i[4]
    optionSociety.append(lista)
optionSociety = list(set(optionSociety))
optionSociety.sort()

societyEntry = OptionMenu(itemsFrame, societyVar,*optionSociety)
societyEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
societyEntry.grid(row=4, column=3,sticky='n')

confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 4,column=4)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

optionTotalSQFT = []
for i in DataList:
    try:
        lista = int(i[5])
        optionTotalSQFT.append(lista)
    except:
        pass
optionTotalSQFT = list(set(optionTotalSQFT))

optionTotalSQFT.sort()
TotalSQFTEntry = OptionMenu(itemsFrame, totalSQFTVar,*optionTotalSQFT)
TotalSQFTEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
TotalSQFTEntry.grid(row=5, column=3,sticky='n')

confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 5,column=4)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

optionBath = []
for i in DataList:
    try:
        lista = int(i[6])
        optionBath.append(lista)
    except:
        pass
optionBath = list(set(optionBath))

optionBath.sort()
bathEntry = OptionMenu(itemsFrame, bathVar,*optionBath)
bathEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
bathEntry.grid(row=6, column=3,sticky='n')

confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 6,column=4)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

optionBalcony = []
for i in DataList:
    try:
        lista = int(i[7])
        optionBalcony.append(lista)
    except:
        pass
optionBalcony = list(set(optionBalcony))

optionBalcony.sort()
balconyEntry = OptionMenu(itemsFrame, balconyVar,*optionBalcony)
balconyEntry.config(width=20,bg=themeclr,fg = "White", bd=3,font="arial 16 bold",justify=CENTER)
balconyEntry.grid(row=7, column=3,sticky='n')

confirmBtn = Button(itemsFrame, font="arial 16 bold",text = "Confirm",height=1, width=10, bg=themeclr,fg="white", bd=3,justify=CENTER,command=sortData)
confirmBtn.grid(row = 7,column=4)
##################################################################

rangelbl = Label(itemsFrame, text="\tSQFT Range\t\t:-\t", font="arial 16 bold", bg=accent,justify=RIGHT)
rangelbl.grid(row=8,sticky="w")
rangeEntry = Entry(itemsFrame, font="arial 16 bold", textvariable=rangeVar, bd=6, width=23, justify=CENTER)
rangeEntry.grid(row=8, column=3)
itemsFrame.pack(fill=BOTH)
########################################################################

Cost_F = Frame(MenuFrame, bg=accent, bd=4)
showPriceBtn = Button(Cost_F, font="arial 16 bold",text = "Show Price",height=1, width=39,bg = themeclr,fg = "white",  bd=6, justify=CENTER, command=show)
showPriceBtn.grid(row = 0,column=0)

availabilityBtn = Button(Cost_F, font="arial 16 bold",text = "Availability",height=1,bg = themeclr,fg="white", width=37, bd=6, justify=CENTER, command = availabiltyFn)
availabilityBtn.grid(row = 0,column=1)

resetBtn = Button(Cost_F, font="arial 16 bold",text = "Reset",height=1, width=39, bg="red",fg="white", bd=6,justify=CENTER,command=reset)
resetBtn.grid(row = 1,column=0)

timeFrame = Frame(Cost_F, bg=accent, bd=4)
timeFrame.grid(row = 1,column=1)

lbl = Label(timeFrame, font="arial 24 bold",bg=accent, fg="royalblue2")
lbl.pack(side=BOTTOM)
Cost_F.pack(side=BOTTOM, fill=BOTH)
time()

# ==========================================================================
secondFrame = Frame(root, bg=themeclr, bd=10,height=150, relief=RIDGE)

table = ttk.Treeview(secondFrame)
table.pack(fill = BOTH,expand=TRUE)

btnFrame = Frame(root, bg=themeclr, height=20,bd=10, relief=RIDGE,)

backBtn = Button(btnFrame, font="arial 16 bold",bg = themeclr,fg= "white",text = "Back",height=1, bd=6, justify=CENTER, command = backFn)
backBtn.pack(fill = BOTH, expand=TRUE)

root.mainloop()