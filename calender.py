import calendar
def isleapyear(year):                                      #checks whether the year is leap year or not taking year as input
    print(calendar.isleap(year))

def whichdayis(year,month,day):                            #returns the day taking year,month,day as input
    dict={0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    month=calendar.weekday(year,month,day)
    print(dict[month])

def printmonth(year,month):                                #prints whole month calendar taking year and month as input
    print(calendar.month(year,month))

def printyear(year):                                       #prints whole year calendar taking month ad input
    print(calendar.calendar(year))
    
def numberofleapyears(start_year,end_year):               #returns no of leapyears in between two years
    print(calendar.leapdays(start_year,end_year))

year=2020
month=12
day=31
start_year=2000
end_year=2020

# # isleapyear(year)
# # whichdayis(year,month,day)
# # printmonth(year,month)
# printyear(year)
# # numberofleapyears(start_year,end_year)
# print("################################################")



