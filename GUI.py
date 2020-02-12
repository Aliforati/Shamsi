import tkinter as t
import os,sys
import Shamsi as s
from PIL import Image,ImageDraw,ImageFont
gui=t.Tk()
def rp(rep):
    try:
        bp = sys._MEIPASS
    except Exception:
        bp = os.path.abspath(".")
    return os.path.join(bp, rep)
def img():
    month=int(mc.get())
    year=int(yc.get())
    mn={1: "ﻦﯾﺩﺭﻭﺮﻓ", 2: "ﺖﺸﻬﺒﯾﺩﺭﺍ", 3: "ﺩﺍﺩﺮﺧ", 4: "ﺮﯿﺗ", 5: "ﺩﺍﺩﺮﻣ", 6: "ﺭﻮﯾﺮﻬﺷ", 7: "ﺮﻬﻣ", 8: "ﻥﺎﺑﺁ", 9: "ﺭﺫﺁ",
          10: "ىﺩ", 11: "ﻦﻤﻬﺑ", 12: "ﺪﻨﻔﺳﺍ"}
    e=yc.get()+" "+s.Dateandtime.mn[int(mc.get())]
    e1="{:^90}".format(yc.get()+" "+mn[int(mc.get())])
    cal=s.Dateandtime.mcal(year,month)[134::]
    fo=ImageFont.truetype(rp("simpfxo.ttf"),26,0,"utf8-fa")
    fo1 = ImageFont.truetype(rp("simpfxo.ttf"), 21, 0, "utf8-fa")
    fo2 = ImageFont.truetype(rp("arial.ttf"), 28)
    im = Image.new("RGB", (800, 600))
    gp=ImageDraw.Draw(im)
    gp.text((10,60),e1,(255,255,255,255),fo2)
    gp.text((10,90),"ﻪﻌﻤﺟ ﻪﺒﻨﺷﺞﻨﭘ ﻪﺒﻨﺷﺭﺎﻬﭼ ﻪﺒﻨﺷ ﻪﺳ ﻪﺒﻨﺷﻭﺩ ﻪﺒﻨﺸﻜﯾ  ﻪﺒﻨﺷ",(255,255,255,255),fo)
    gp.text((5,120),cal,(255,255,255,255),fo1)
    if not os.path.exists(os.environ["USERPROFILE"] + "\\Desktop\\Shamsi\\"):
        os.mkdir(os.environ["USERPROFILE"]+"\\Desktop\\Shamsi\\")
    im.save(os.environ["USERPROFILE"]+"\\Desktop\\Shamsi\\"+e+".jpg")
    dn=t.Tk()
    d=t.Label(dn,text="انجام شد",width=27)
    dn.geometry("200x50")
    d.grid(row=1,columnspan=3)
    dn.iconbitmap(rp("icon.ico"))
    dn.title("پیام")
    op=t.Button(dn,text="باز کردن",command=lambda :im.show())
    op.grid(row=2,columnspan=3)
    dn.mainloop()
def getcal():
    cal=s.Dateandtime.mcal(int(yc.get()),int(mc.get()))[134::]
    view.delete(0.0,100.100)
    view.insert(0.0,cal)
    mn=t.Label(gui, text="{:^20}".format(yc.get()+" "+s.Dateandtime.mn[int(mc.get())]))
    mn.grid(row=3, columnspan=3)
def time():
    td.config(text="امروز: "+str(s.Dateandtime.Now()))
    td.after(1000,time)
ml=t.Label(gui,text="ماه").grid(row=0,column=0)
mc=t.Spinbox(gui,from_=1,to=12,width=5,command=getcal)
mc.grid(row=1,column=0)
yl=t.Label(gui,text="سال").grid(row=0,column=2)
yc=t.Spinbox(gui,from_=1300,to=2000,width=5,command=getcal)
yc.grid(row=1,column=2)
ib=t.Button(gui,text="چاپ",command=img)
ib.grid(row=7,columnspan=3)
wd=t.Label(gui,text="شنبه              یکشنبه                 دوشنبه           سه شنبه          چهار شنبه             پنج شنبه             جمعه").grid(row=4,columnspan=7)
view=t.Text(gui,width=62,height=6)
view.grid(row=5,columnspan=3)
view.insert(0.0,s.Dateandtime.mcal(int(yc.get()),int(mc.get()))[134::])
getcal()
td=t.Label(gui)
td.grid(row=6,columnspan=3)
time()
gui.title("تقویم شمسی")
gui.iconbitmap((rp('icon.ico')))
gui.mainloop()
