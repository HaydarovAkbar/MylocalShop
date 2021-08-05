"""
Tuzuvchi: Haydarov Akbar
sana: 2021/04/18
"""
from Magazin_Project.xaridor import xaridor_func, qold
from Magazin_Project.order_project import order, mahsulot
from Magazin_Project.buy_class import BuyClass
from Magazin_Project.sotilgan_mahsulotlar import BuyMahsulot

buyClass = BuyClass()  # buy classni qulay ko'rinishiga keltiryapmiz
buyMahsulot = BuyMahsulot()  # buyMahsulot class ni qulay ko'rinishga keltiryapmiz


def sotuv(costomer_id, MID, soni):
    """bu funksiya bilan savdoni amalga oshiramiz"""
    if order(MID, costomer_id, soni) == True:

        if buyClass.buy(MID, soni, costomer_id):

            buy_money = mahsulot(MID, soni)  # mahsulotlarni hammasini narxi shunga teng

            if buyMahsulot.add_buy_list(MID, costomer_id, soni, buy_money):
                print(xaridor_func(costomer_id, MID, soni, buy_money))

            else:
                print("Kechirasiz sotilgan mahsulotlar ruyxatini kiritishda xato yuz berdi! \n")

        else:
            print("Kechirasiz mahsulot sotib olishda xato yuz berdi\n")

    else:
        print(order(MID, costomer_id, soni))


while True:
    """istalgancha savdo qilishingiz mumkin agar pulingiz yetsa"""
    try:
        costomer_id = int(input("Costumer ID (1,2,3,4)ni kiriting >"))
        MID = int(input("Mahsulot ID (1,2,...,20)sini kiriting >"))
        soni = int(input("Sonini kiriting >"))

        sotuv(costomer_id, MID, soni)

        yana = input("Yana savdo qilasizmi Yes/No").lower()
        if yana == "no":
            break
    except Exception as e:
        print("son kiritmadinggiz\n")
