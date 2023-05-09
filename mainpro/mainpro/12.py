def is_leap(year: int) -> str:
    if(year%4 == 0 and year%400 == 0 and year%100!= 0 ): 
        return "True"
    else: 
        return "False"





year = int(input())
print(is_leap(year))