from Magazin_Project.order_project import mahsulot
from Magazin_Project.postgres_project import Magazin_Db

magazin = Magazin_Db()

class BuyClass:
    """bu class bilan savdoni amalga oshiramiz !"""

    def products_new_count(self, MID, newCount):
        """bu funksiya mahsulotni sonini kamaytirishda foydalanamiz!"""

        magazin.update_product_count(MID, newCount)
        return True

    def costomer_update(self, idx, qoldiq):
        """bu class bilan xaridorni yangi mablag'ini bazaga joylash uchun ishlatamiz"""
        magazin.update_costomer_newMoney(idx, qoldiq)
        return True

    def qoldiq_pul(self, item1, item2):
        """Xaridorni puli qancha qolganini aniqlashda foydalanamiz !"""
        qoldiq = item1 - item2
        return qoldiq

    def buy(self, MID, soni, cos_id):
        """bu yerda savdoni amalga oshiramiz"""
        jami_summa = mahsulot(MID, soni)  # bu xaridor olmoqchi bo'lgan barcha mahsulotlarini narxi
        cos_money = float(magazin.select_costomer(cos_id)[3])  ## bu xaridorni savdo qilmasdan avvalgi pul miqdori
        qoldiq = self.qoldiq_pul(cos_money, jami_summa)
        if self.costomer_update(cos_id,
                                qoldiq):  # shart to'g'ri bo'lgandagina ishlaydi aks holda else: holatni ekranga chiqaradi
            mahsulotlar_soni = magazin.select_mahsulot(MID)[4]  ## bu savdodan avvalgi mahsulotlar soni
            new_count = mahsulotlar_soni - soni  ## bu savdodan keyingi mahsulotlar soni
            if self.products_new_count(MID,
                                       new_count):  # mahsulotlarni sonini yuqoridagi funksiya bilan bazaga kiritilyapti
                return True
            else:
                return f"Mahsulotni sonini yangilashda qandaydir muammoga duch keldim !"
        else:
            return f"Xaridorni mablag'ini yangilashda qandaydir muammoga duch keldim!"


if __name__ == '__main__':
    b = BuyClass()
    b.buy()
