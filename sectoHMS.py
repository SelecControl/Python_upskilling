# Pseudo code
# Take integer input as seconds
# divide by 3600 to get total hrs.
# Store the rminder in Min
# Then divid that with 60 to get minutes and store it's reminder in seconds and proint the output

Sec = int(input("Enter the seconds: "))
Sec_input = Sec
Hrs = Sec // 3600
Sec = Sec % 3600
Min = Sec // 60
Sec = Sec % 60
print(f"{Sec_input} seconds = {Hrs} hour(s), {Min} minutes(s), {Sec} second(s)")
