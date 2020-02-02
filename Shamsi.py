from datetime import datetime
class Dateandtime:
    Day=None
    Month=None
    Year=None
    Hour=None
    Min=None
    H24=None
    m = {6: "یک شنبه", 0: "دو شنبه", 1: "سه شنبه", 2: "چهارشنبه", 3: "پنج شنبه", 4: "جمعه", 5: "شنبه"}
    mn = {1: "فروردین", 2: "اردیبهشت", 3: "خرداد", 4: "تیر", 5: "مرداد", 6: "شهریور", 7: "مهر", 8: "آبان", 9: "آذر",
          10: "دی", 11: "بهمن", 12: "اسفند"}
    def __init__(self,Year,Month,Day,Hour=None,Min=None,H24=None):
        self.Year=Year
        self.Month=Month
        self.Day=Day
        self.Hour=Hour
        self.Min=Min
        self.H24=H24
        if Day > 31 or Day < 1:
            raise SyntaxError("خطای روز")
        if Month > 12 or Month < 1:
            raise SyntaxError("خطای ماه")
        if Month>6 and Day>30:
            raise SyntaxError("خطای روز")
        if Year/10000>1:
            raise SyntaxError("خطای سال")
        if Month==12 and Year%4!=3 and Day==30:
            raise SyntaxError("خطای کبیسه")
        if Hour is not None and (Hour > 24 or Hour < 0):
            raise SyntaxError("خطای ساعت")
        if Min is not None and (Min > 59 or Min < 0):
            raise SyntaxError("خطای دقیقه")
    @staticmethod
    def GTSH(yy,mm,dd):
        daysmonth={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        i=(yy)*365+((yy)//4)
        s=mm-1
        k=0
        while(s>0):
            k+=daysmonth[s]
            if yy%4==0 and s==2:
                i+=1
            s-=1
        l=dd
        i+=k+l
        if (yy%4==0 and l+k<80):
            i-=1
        elif l+k<80:
            i+=1
        elif l+k>=80 and yy%4==0:
            i+=1
        i-=226900
        i-=(i//365)//4
        y=i//365
        i%=365
        b=0
        while(b<12):
            b+=1
            if i<30:
                break;
            if b<6:
                i-=31
            else:
                i-=30
        if i==0 and i:
            b-=1
            d=31 if b<6 else 30
        else:
            d=i
        return Dateandtime(y,b,d)
    def __h24f__(self,i):
        st="" if i==0 else "ساعت "
        if self.H24==True:
            st+="0"+str(self.Hour) if self.Hour<10 else str(self.Hour)
        elif self.Hour==12:
            st+="12"
        elif self.Hour==24:
            st+="00"
        else:
            if self.Hour<12:
                if self.Hour<10:
                    st+=("0"+str(self.Hour))
                else:
                    st+=str(self.Hour)
            else:
                st+="0"+str(self.Hour-12) if self.Hour-12<10 else str(self.Hour-12)
        st+=" و " if i==1 else ":"
        st+="0"+str(self.Min) if self.Min<10 else str(self.Min)
        if i==1:
            st+=" دقیقه"
            if self.H24==False:
                st+=" قبل از ظهر" if ((self.Hour%24)/12)<1 else " بعد از ظهر"
        else:
            st+=" AM" if ((self.Hour%24)/12)<1 else " PM"
        return st
    def __numberic__(self):
        return str(self.Year) + "/" + str(self.Month) + "/" + str(self.Day) + " " + self.__h24f__(0) if self.Hour != None else str(self.Year) + "/" + str(self.Month) + "/" + str(self.Day)
    def __str__(self):
        return self.m[self.__dayofweek__()]+" "+str(self.Day) + " ام " + self.mn[self.Month] + " ماه سال " + str(self.Year) + " " + self.__h24f__(1) if self.Hour != None else self.m[self.__dayofweek__()]+" "+str(self.Day) + " ام " + self.mn[self.Month] + " ماه سال " + str(self.Year)
    def __h24c__(self):
        if self.H24==True:
            self.H24=False
        else:
            self.H24=False
    def __dayofweek__(self):
        y=(self.Year-1)*365+((self.Year-4)//4)
        z=self.Month-1
        while(z>0):
            y+=30 if z>6 else 31
            z-=1
        y+=self.Day
        return y%7
    @staticmethod
    def Now():
        n=datetime.now()
        c=Dateandtime.GTSH(n.year,n.month,n.day)
        return Dateandtime(c.Year,c.Month,c.Day,n.hour,n.minute,True)
    @staticmethod
    def mcal(year,month):
        a=Dateandtime(year,month,1)
        t = list(map(lambda x:x+1,[2, 1, 1, 2, 2, -1, 3]))
        s="{0:^70}".format("o"+Dateandtime.mn[a.Month]+" "+str(year)+"o")+"\n"
        s+="o{m[4][0]:o<5}{m[3][0]:o^10}{m[2][0]:o^10}{m[1][0]:o^10}{m[0][0]:o^10}{m[6][0]:o^10}{m[5][0]:o>5}o".format(m=Dateandtime.m)

        s+="\n "
        c=1
        b=[]
        for i in range((a.__dayofweek__()-5)%7):
           b.append("")
        s+="\b"*10
        for i in range(1,32):
            b.append(i)
            if i==29 and month==12 and year%4!=3:
                break
            if i==30 and month>6:
                break
        while b.__len__()<42:
            b.append("")
        s+=" {h[6]:<5}{h[5]:^10}{h[4]:^10}{h[3]:^10}{h[2]:^10}{h[1]:^10}{h[0]:>5}\n" \
           " {h[13]:<5}{h[12]:^10}{h[11]:^10}{h[10]:^10}{h[9]:^10}{h[8]:^10}{h[7]:>5}\n" \
           " {h[20]:<5}{h[19]:^10}{h[18]:^10}{h[17]:^10}{h[16]:^10}{h[15]:^10}{h[14]:>5}\n" \
           " {h[27]:<5}{h[26]:^10}{h[25]:^10}{h[24]:^10}{h[23]:^10}{h[22]:^10}{h[21]:>5}\n" \
           " {h[34]:<5}{h[33]:^10}{h[32]:^10}{h[31]:^10}{h[30]:^10}{h[29]:^10}{h[28]:>5}\n" \
           " {h[41]:<5}{h[40]:^10}{h[39]:^10}{h[38]:^10}{h[37]:^10}{h[36]:^10}{h[35]:>5}\n".format(h=b)
        return s
    @staticmethod
    def ycal(year):
        s="{:^65}".format(str(year))+"\n"
        for i in range(12):
            s+=Dateandtime.mcal(year,i+1).replace(" "+str(year)+"o","o")+"\n\n"
        return s