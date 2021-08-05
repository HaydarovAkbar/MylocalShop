from Magazin_Project.postgres_project import Magazin_Db
import datetime

date = datetime.datetime.now()
hozir = datetime.datetime.strftime(date,
                                   "%Y/%m/%d %H:%M")  # hozirgi vaqtni (2021/04/18 16:07) ko'rinishga keltirilyapti

magazin = Magazin_Db()


def qold(id):
    """bu funksiya bilan id li xaridorni mablag'ini ko'rishimiz mumkin"""
    qoldiq = magazin.select_costomer(id)[3]
    return qoldiq


def xaridor_func(c_id, MID, soni, mnarxi):
    """bu funksiya barcha malumotlarni olib ekranda tasdiqlash uchun qo'llaymiz"""
    xaridor = magazin.select_costomer(c_id)[1]
    mahsulot = magazin.select_mahsulot(MID)[2]
    result = f"""
xaridor    -  {xaridor}
mahsulot   -  {mahsulot}
soni       -  {soni}
jami narxi -  {mnarxi}
vaqt       -  {hozir}
qoldiq pul -  {qold(c_id)}

Xarid muvoffaqiyatli amalga oshirildi!\n
"""
    return result


if __name__ == '__main__':
    print(xaridor_func(1, 2, 2, 2000))
