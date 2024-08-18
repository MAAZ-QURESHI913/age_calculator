print("WEL COME TO AGE CALCULATOR :")

name = input("\nenter name : ")

current_year  = int(input("enter current year : "))
user_age = int(input("\nenter your birth year : ")) 
year_cal = current_year - user_age
month_cal = 12 * year_cal
days_cal = 365 * year_cal
hours_cal = 24 * days_cal
minuts_cal = 60 * hours_cal
secounds_cal = 60 * minuts_cal

print(f"\n\n😋😎😗🥰😍😋🤩🤗🤔😛😵🤫\n\nhello mr/miss {name.title()}\n\nhappy happy returns of day,\n\nyou`r age is {year_cal} year , {month_cal} month , {days_cal} days , {hours_cal} hours , {minuts_cal} minuts , and {secounds_cal} secounds:\n")
    