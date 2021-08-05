from psycopg2 import connect
import datetime    # bu kutubxonani savdo qilinayotgan vaqtni bazaga kiritish uchun chaqirdik

HOST = "localhost"
USER = "postgres"
PASS = "akbar2000"
DATA = "baza1"

data = datetime.datetime.now()
data1 = data.strftime("%Y/%m/%d %H:%M")


class Magazin_Db:
    def select_costomer(self, id):
        """bu funksiya orqali id li xaridor haqida malumot olishimiz mumkin!"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATA
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"SELECT * FROM costomer WHERE id = {id}") # barcha malumotlarni qaytaradi
            return cursor.fetchall()[0]             # ro'yxat tuple ko'rinishida qaytadi
        except Exception as e:
            print("Siz adashdingiz ->", e)

    def select_mahsulot(self, MID):
        """Bu funksiya orqali MID li mahsulot haqida malumotni olishimiz mumkin! """
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATA
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"SELECT * FROM products WHERE id = {MID}")   # barcha malumotlarni qaytaradi
            return cursor.fetchall()[0]                     ## natija tuple ko'rinishida qaytadi
        except Exception as e:
            print(f"Siz qayerdadir adashdingiz dustm -> {e}")

    def update_costomer_newMoney(self, id, money):
        """bu funksiya orqali xaridorni mablag'ini yangilashimiz mumkin !"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATA
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"UPDATE costomer SET money = {money} WHERE id = {id}")     # Faqat shu ID li xaridorni pulini yangilaydi
        except Exception as e:
            print("Siz qayerdadir adashdingiz ->", e)

    def update_product_count(self, MID, newSoni):
        """bu funksiya orqali mahsulotni sonini yangilashimiz mumkin !"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATA
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"UPDATE products SET soni = {newSoni} WHERE id = {MID}")
        except Exception as e:
            return f"Mahsulotni sonini yangilashda qandaydir muammoga duch keldim -> {e}"

    def insert_buy_list(self, id, p_id, c_id, quant, buy_m):
        """bu funksiya orqali savdo haqida malumotni bazaga kiritamiz !"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATA
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(
                f"INSERT INTO buy_list(id,p_id,c_id,quantity,buy_money,data) VALUES({id},{p_id},{c_id},{quant},{buy_m},'{data1}')")
            return True
        except Exception as e:
            print("siz qayerdadir adashdingiz !", e)


m = Magazin_Db()
if __name__ == '__main__':
    m = Magazin_Db()
    # m.update_product_count(11,20)
    # print(m.select_mahsulot(11))
    # print(data1)
    # print(m.select_costomer(4))
    # m.update_costomer_newMoney(4,270000000)
    # m.update_product_count(3,11)