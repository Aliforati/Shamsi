# Shamsi
Requirements:python 3.6
Install by "" pip install https://github.com/Aliforati/Shamsi/archive/master.zip "" command
Use in script or shell by import 'from Dateandtime import Dateandtime'
You can create Dateandtime objects thats represents shamsi date by Year,Month,Day,(*)Hour,(*)Min,(*)H24 :
Year:Between 1,9999 in shamsi
Month:Between 1,12 in shamsi
Day: Between 1,31 in Farvardin-Sharivar Months & 1,30 in Mehr-Esfand(Leap years) Months & 1,29 in Esfand(Non-Leap years) Month
Hour:Between 00,23 (You can also use 24 as 00)
Min:Between 00,59
H24:True (for 24-Hours system) & False (for 12-Hours system)

Methods:
__str__():return date and time in persian like چهارشنبه 20 آذر ماه سال 1398 ساعت 10 و 08 دقیقه بعد از ظهر
__numberic__():return date in numberic like 1398/09/20 10:08 PM
__h24c__():convert 12-Hours to 24-Hours system or 24-Hours to 12-Hours system

Static Methods:
Now():returns current date and time in persian
GTSH():get Years,Month,Day in Gregorian system & convert it to Shamsi & return a Dateandtime object thats include converted date


*:Not Necessary
