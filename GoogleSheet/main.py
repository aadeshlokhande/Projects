# aadeshsheet@hackathon1209.iam.gserviceaccount.com
import gspread

gc = gspread.service_account(filename="hackathon1209-d4da1d1b790d.json")

wks = gc.open("Abc").sheet1

a = wks.get("C6")
print(a)

wks.update("A2","bhola")