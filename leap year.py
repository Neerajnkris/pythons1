current_year = int(input("enter the current year: "))
final_year= int(input("enter final year: "))
print("leap years from",current_year,"to",final_year,"are")
for year in range(current_year,final_year +1):
    if(year % 4 ==0 and year %100!=0):
        print (year)