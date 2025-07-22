gm = float(input("เดินทางกี่กิโล : "))
if 5 <= gm <= 50 :
    print("ราคา 10 บาท")
elif 51 <= gm <= 100:
    print("ราคา 15 บาท")
elif 101 <= gm <= 300:
    print("ราคา 25 บาท")
elif 301 <= gm <= 500:
    print("ราคา 35 บาท")
elif 501 <= gm :
    print("ราคา 45 บาท")
else:
    print("ไม่ส่งครับ")