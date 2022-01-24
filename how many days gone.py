import datetime as DT

birthDate  = input("Enter your birth date just like this format 1991,4,29 : ")
print("birthDate " , type(int(birthDate)))
birth_Year = DT.date(1991,4,29)
print(type(birth_Year))
input_year = input("Enter the date (exam : 1991.04.29) : ")
year       = DT.datetime.strptime(input_year , "%Y.%m.%d")

days_life  = (year.date() - birth_Year).days
if days_life <= 0 :
    print("you hasn't become birth yet on this date  :| ")
else:
    print('\n{} days gone from your lifetime and your birth date '.format(days_life))