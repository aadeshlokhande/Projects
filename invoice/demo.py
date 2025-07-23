try:
    from reportlab.pdfgen import canvas
except:
    import os 
    os.system("pip install reportlab")

companyName = "ICE Computers"
address1 = "Plot no 10 , Gyani Layout, Rajnagar,"
address2 = "Nagpur - 440013, India."
Cname = "demo"
invoiceNo = "10001"
date = "21/10/2021"
CPhone = "8766717506"

SrNo = "1"
work = "Digital Marketing"
rate = "3500"
qty = "1"
total = "4500"
paid = "4500"
remain = "00"

Authorised = "Aadesh G. Lokhande"

c = canvas.Canvas(f"{Cname}-Invoice.pdf",pagesize=(200,250),bottomup=0)

c.translate(10,40)
c.scale(1,-1)
c.drawImage("GCE.jpg",10,0,width=30,height=30)

c.scale(1,-1)
c.translate(-10,-40)
c.setFont("Helvetica-Bold",10)
c.drawCentredString(125,20,companyName)
c.line(60,22,190,22)
c.setFont("Helvetica-Bold",5)
c.drawCentredString(125,30,address1)
c.drawCentredString(125,35,address2)
c.setFont("Helvetica-Bold",6)

c.line(5,44,195,44)

c.setFont("Courier-Bold",8)
c.drawCentredString(100,55,"TAX-INVOICE")

c.roundRect(15,63,170,40,10,stroke=1,fill=0)
c.setFont("Times-Bold",5)
c.drawRightString(70,70,"INVOICE No. :")
c.drawRightString(70,80,"DATE :")
c.drawRightString(70,90,"CUSTOMER NAME :")
c.drawRightString(70,100,"PHONE No. :")

c.drawString(90,70,invoiceNo)
c.drawString(90,80,date)
c.drawString(90,90,Cname)
c.drawString(90,100,CPhone)

c.roundRect(15,108,170,130,10,stroke=1,fill=0)
c.line(15,120,185,120)
c.drawCentredString(25,118,"SR No.")
c.drawCentredString(75,118,"GOODS DESCRIPTION")
c.drawCentredString(125,118,"RATE")
c.drawCentredString(148,118,"QTY")
c.drawCentredString(173,118,"TOTAL")

c.drawCentredString(25,130,f"{SrNo}")
c.drawCentredString(75,130,f"{work}")
c.drawCentredString(125,130,f"{rate} Rs")
c.drawCentredString(148,130,f"{qty}")
c.drawCentredString(173,130,f"{int(rate)*int(qty)} Rs")


c.drawCentredString(75,207,"Paid")
c.drawCentredString(173,207,f"{paid} Rs")
c.drawCentredString(75,217,"Remaining")
c.drawCentredString(173,217,f"{remain} Rs")



c.line(15,210,185,210)
c.line(15,200,185,200)
c.line(35,108,35,220)
c.line(115,108,115,220)
c.line(135,108,135,220)
c.line(160,108,160,220)

c.line(15,220,185,220)
c.line(100,220,100,238)
c.drawString(20,225,"We declare that above mentioned")
c.drawString(20,230,"information is true.")
c.drawString(20,235,"(This is system generated invoive)")
c.drawRightString(170,235,"Authorised Signatory")



c.drawRightString(170,227,Authorised)

c.showPage()
c.save()