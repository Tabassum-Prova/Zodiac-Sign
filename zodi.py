from datetime import date

Year = input("What's your year of birth?[ex:1992]")
Month = input("What's you month of birth? [ex:10]")
Day = input("What's your day of birth?[ex:25]")
print("Your Date Of Birth is", (Day + "/" + Month + "/" + Year))
today_day = date.today()
print(today_day)
age = today_day.year - int(Year)
print("You are", age, "years.old")

if((int(Month)==12 and int(Day) >= 22) or (int(Month)==1 and int(Day)<= 19)):
    Sign = ("\n Capricorn")
elif((int(Month)==1 and int(Day) >= 20) or (int(Month)==2 and int(Day)<= 18)):
    Sign = ("\n aquarius")
elif((int(Month)==2 and int(Day) >= 19) or (int(Month)==3 and int(Day)<= 20)):
    Sign = ("\n pisces")
elif((int(Month)==3 and int(Day) >= 21) or (int(Month)==4 and int(Day)<= 19)):
    Sign = ("\n Aries")
elif((int(Month)==4 and int(Day) >= 20) or (int(Month)==5 and int(Day)<= 20)):
    Sign = ("\n taurus")
elif((int(Month)==5 and int(Day) >= 21) or (int(Month)==6 and int(Day)<= 20)):
    Sign = ("\n Gemini")
elif((int(Month)==6 and int(Day) >= 21) or (int(Month)==7 and int(Day)<= 22)):
    Sign = ("\n Cancer")
elif((int(Month)==7 and int(Day) >= 23) or (int(Month)==8 and int(Day)<= 22)):
    Sign = ("\n Leo")
elif((int(Month)==8 and int(Day) >= 23) or (int(Month)==9 and int(Day)<= 22)):
    Sign = ("\n Virgo")
elif((int(Month)==9 and int(Day) >= 23) or (int(Month)==10 and int(Day)<= 22)):
    Sign = ("\n Libra")
elif((int(Month)==10 and int(Day) >= 23) or (int(Month)==11 and int(Day)<= 21)):
    Sign = ("\n Scorpio")
elif((int(Month)==11 and int(Day) >= 22) or (int(Month)==12 and int(Day)<= 21)):
    Sign = ("\n Sagittarius")
print(Sign)