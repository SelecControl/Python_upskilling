a = input("Enter the year: ")
year = int(a)

if (year % 4 == 0):
    if(year % 400 == 0):
        print("leap")
    else:
        if(year % 100 == 0):
            print("NOT leap")
        else:
            print("leap")
else:
    print("NOT leap")
