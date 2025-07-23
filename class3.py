# # score = int(input("can u put score : "))
# # if score >=0:
# #     if score <= 100:
# #         if score >=80:
# #             print("A")
# #         if score < 80:
# #             if score >= 70:
# #                 print("B")
# #             if score < 70:
# #                 if score >= 60:
# #                     print("C")
# #                 if score < 60:
# #                     if score >= 50:
# #                         print("D")
# #                     if score < 50:
# #
# #
# #                       print("F")
# lit = []
# i = True
# while i == True:
#    lit.append(input("name : "))
#    if lit[-1] == "*":
#       lit.remove(lit[-1])
#       break
# print(lit)


# # while True:
# #    choice = int(input("Enter 1 for + Enter 2 for exit"))

# #    if choice == 1:
# #       num = int(input("เลขที่ต้องการจะบวก"))
# #       sumation = 0

# #       for i in range(num):
# #          num1 = int(input("กรอกเลข :"))
# #          sumation += num1

# #       print("ผลลัพ : "sumation)

# #    if choice == 2:
# #       break


def dat():
    print("------------------------------------------")


monsterhp = 100
DMG = 0
HERO = False
game = int(
    input("เข้าต่อกรกับร่างจุตติของเทพปีศาจ(Enter 1) กลับบ้านไปปลูกผักสร้างฮาเร็มที่ชนบท(Enter 2) : ")
)
dat()


while game == 1:
    monsterhp = 100
    wepponuse = False
    DMG = 0
    HERO = False
    turn = int(input("จำนวนการ combo : "))
    dat()
    print("ร่างจุตติของเทพปีศาจ : ", str(monsterhp), "HP")
    dat()
    for i in range(turn):
        print("combo :", i)
        print("combo left :", turn - i)
        print("ร่างจุตติของเทพปีศาจ : ", str(monsterhp), "HP")
        wepponuse = False
        while wepponuse == False:
            weppon = int(
                input(
                    """เลือกอาวุธที่จะโจมตี
ดาบคู่สวรรค์สบั้นจักรดาราทั้ง 12 (15dmg)(Enter 1)
หอกแห่งความพิโรธของเทพโบราณ (20dmg)(Enter 2)
กริชแห่งการหลงลืมและพรากจาก(5dmg)(Enter 3)
:"""
                )
            )
            if weppon == 1:
                DMG = 15
                wepponuse = True
            elif weppon == 2:
                DMG = 20
                wepponuse = True
            elif weppon == 3:
                DMG = 5
                wepponuse = True
            else:
                dat()
                print("หยิบให้ถูกสิวะไอเวร หยิบใหม่")
                dat()
        monsterhp -= DMG
        if monsterhp < 0:
            monsterhp = 20
        print("ร่างจุตติของเทพปีศาจ : ", str(monsterhp), "HP")
        if monsterhp == 0:
            break
        dat()

    if monsterhp == 0:
        print(
            """***คุณปราบร่างจุตติของเทพปีศาจสำเร็จ***
              ----------------------------------
              1,000,000exp
              ----------------------------------
              LV UP :995
              LV UP :996
              LV UP :997
              LV UP :998
              LV UP :999
              ----------------------------------
              ได้รับฉายา *ผู้กล้าแห่งความ*
              ----------------------------------
              ปลดล็อค ความสามารถพิเศษ : ผู้นำพาความหวัง
              คุณสมบัติ : ได้รับความเคารพจากทุกผ่าพันธุ์ทั่วโลก
              ----------------------------------"""
        )
        HERO = True
    else:
        print("คุณตาย")
        dat()
    game = int(
        input(
            "เข้าต่อกรกับร่างจุตติของเทพปีศาจ(Enter 1) กลับบ้านไปปลูกผักสร้างฮาเร็มที่ชนบท(Enter 2) : "
        )
    )
dat()

if HERO == True:
    print("ผู้คนมากมายออกมาต้อนรับคุณ")
    print("ฮาเร็มของคุณต้อนรับคุณด้วยความอบอุ่น")
else:
    print("คุณถูกร่างจุตติของเทพปีศาจฆ่า")
    print("ฮาเร็มของคุณทุกข์ใจจนฆ่าตัวตายไปทีละคน")
