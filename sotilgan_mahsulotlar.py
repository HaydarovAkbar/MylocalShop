from Magazin_Project.postgres_project import Magazin_Db

magazin = Magazin_Db()


class BuyMahsulot:
    def add_buy_list(self,MID,costomer_id,soni,money):
        """bu method bilan savdo haqidagi malumotni bazaga joylaymiz"""

        p_id = magazin.select_mahsulot(MID)[1]
        id = MID
        c_id = costomer_id
        quentity = soni
        jami_money = money

        if  (jami_money > 0):
            magazin.insert_buy_list(id, p_id, c_id, quentity, jami_money)
            return True
        else:
            return f"Buy_listga joylashda qanaqadir xatolik yuz berdi"

if __name__ == '__main__':
    b = BuyMahsulot()