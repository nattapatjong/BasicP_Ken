kilo = int(input("ระยะทาง : "))

if (kilo < 5):
    print("ฟรี")
elif (51 > kilo > 4):
    print("10 บาท")
elif (101 > kilo > 50):
    print("15 บาท")
elif (301 > kilo > 100):
    print("25 บาท")
elif (501 > kilo > 300):
    print("35 บาท")
else:
    print("45 บาท")