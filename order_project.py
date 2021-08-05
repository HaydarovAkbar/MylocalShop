from Magazin_Project.postgres_project import Magazin_Db

magazin = Magazin_Db()


def order_soni(MID, soni):
    """Mahsulot ID si va xaridor talab qilayotgan soni ni kiritasiz"""
    msoni = magazin.select_mahsulot(MID)[4]
    if msoni >= soni:  # agar mahulot bulsa ishlaydi aks holda ishlamaydi
        return True
    else:
        return False


def mahsulot(MID, soni):
    """xaridor olmoqchi bo'lgan mahsulotlarni jami narxini chiqaradi"""
    narxi = magazin.select_mahsulot(MID)[3]
    narx = float(
        narxi.replace(".", ""))  ## mahsulotni narxi string ko'rinishida va orasida '.'ta bor shuni songa aylantiryapmiz
    jami = narx * soni
    return jami  # javob float tipida chiqadi


def order_pul(Mid, cos_id, soni):
    """Xaridorni mahsulotlarni olishga puli yetadimi yoki yuq shuni tekshiradi"""
    jami = mahsulot(Mid, soni)
    costomer = float(magazin.select_costomer(cos_id)[3])
    if costomer >= jami:
        return True
    else:
        return f"Sizni hisobingizda mablag' yetarli emas \niltimos hisobingizni to'ldiring!"


def order(MID, cos_id, soni):
    """agar mahsulot olishga puli yetsa dastur ishlashda davom etadi"""
    if order_soni(MID, soni):
        return order_pul(MID, cos_id, soni) ## natijani True ko'rinishida qaytaradi
    else:
        return f"Afsuski hozir bizda bunaqa miqdorda mahsulot yuq!"


if __name__ == '__main__':
    print(order(1, 1, 1))
