
import time
import winsound
print ("\033[1mTIMER\033[0m")
print("\033[3mPUT IN THE MINUTES THEN THE SECONDS\033[0m")

timer_amount_mins = input("How long do you want your timer to last in minutes? ")
if timer_amount_mins == "":

    timer_amount_mins = 0.0
else:
    timer_amount_mins = float(timer_amount_mins)
timer_amount_secs = input("How much seconds do you want to add ")
if timer_amount_secs == "":
    
    timer_amount_secs = 0.0
else:
    timer_amount_secs = float(timer_amount_secs)
timer_length = int(input("How many beeps do you want? "))

timer_amount_mins *=60
timer_amount =  timer_amount_mins + timer_amount_secs
timer_amount = int(timer_amount)

while timer_amount > 0:
    print(" ",timer_amount, end = '\r')
    timer_amount -= 1
    time.sleep(1)
   

if timer_amount == 0 :
    for i in range(timer_length):
        print("TIMER UP")
        winsound.Beep(2000, 200)
        winsound.Beep(1000, 200)
        winsound.Beep(500, 200)
        time.sleep(0.2)