print("SARIM ALI KHAN")
print("18B-043-CS(A)")
print("THE FORMAT OF DATES")
date_format = input("Enter the date format dd-mm-yy or mm-dd-yy: ")
if date_format == 'dd-mm-yy':
    for i in range(11):
        date = input("Enter the date: ")
        dd,mm,yy = date.split('-')
        dd = int(dd)
        mm = int(mm)
        yy = str(yy)
        if(mm ==1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            max_days = 31
        elif(mm ==4 or mm == 6 or mm == 9 or mm == 11):
            max_Days = 30
        else:
            max_days = 28
        if (mm < 1 or mm > 12):
            print("Your month is invalid")
        elif (len(yy)>2):
            print("Your year is invalid as per the format")
        elif (dd < 1 or dd > max_days):
            print("day is invalid")
        else:
            print("Your date is valid.")
elif date_format == 'mm-dd-yy':
    for i in range(11):
        date = input("Enter the date: ")
        mm,dd,yy = date.split('-')
        dd = int(dd)
        mm = int(mm)
        yy = str(yy)
        if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            max_days = 31
        elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
            max_Days = 30
        else:
            max_days = 28
        if (mm < 1 or mm > 12):
            print("Your month is invalid")
        elif (len(yy) > 2):
            print("Your year is invalid as per the format")
        elif (dd < 1 or dd > max_days):
            print("day is invalid")
        else:
            print("Your date is valid.")
