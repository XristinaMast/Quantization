from math import floor

print("Please enter the range of these numbers (a,b)")
a = float(input("a: "))
b = float(input("b: "))

q = int(input("Now please enter the quantization level: "))
step = abs(b-a) / q

while True:
    print("Now you will set the values of the samples, when you finish please type anything but a number")

    want_to_stay = True
    while True:
        s = input("Please enter the value of the sample: ")
        try:
            s = float(s)
            if s < a or s > b:
                continue
            else:
                zone = floor(s/step)
                print("It is in the zone: " + str(zone) + ", binary: " + str(bin(zone))[2:])
        except ValueError:
            # ο χρήστης έδωσε χαρακτήρα
            want_to_stay = False
            break
    if not want_to_stay:
        break
