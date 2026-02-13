
import datetime

from colorama import Fore, Style

welcome_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                          PY1 🏦BANK                          ║
║                    O'Z-O'ZIGA XIZMAT 🏧ATM                   ║
╠══════════════════════════════════════════════════════════════╣
║                         Xush kelibsiz!                       ║
║                                                              ║
║  Ushbu bankomat orqali quyidagilarni bajarishingiz mumkin:   ║
║    • 💰Balansni tekshirish                                   ║
║    • 💴Naqd pul yechish                                      ║
║    • ➕Hisobni to'ldirish                                     ║
║    • 💳Kartadan-kartaga o'tkazma                             ║
║    • 🔢PIN-kodni o'zgartirish                                ║
║    • ⌛Tranzaksiyalar tarixini ko'rish                        ║
║                                                              ║
║  Xavfsizlik ogohlantirishi:                                  ║
║    • PIN-kodingizni hech kimga aytmang.                      ║
║    • PIN kiritayotganda klaviaturani yopib turing.           ║
║    • Shubhali qurilma ko'rsangiz — bekor qiling.             ║
║                                                              ║
║  Tizim holati: ONLINE                                        ║
╠══════════════════════════════════════════════════════════════╣
║  [1] Kartani kiritish / Davom etish                          ║
║  [2] Kartani olish                                           ║
║  [0] Chiqish                                                 ║
╚══════════════════════════════════════════════════════════════╝
Tanlov: _"""

auth_card_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                     💳KARTANI TASDIQLASH (AUTH)              ║
╠══════════════════════════════════════════════════════════════╣
║  Iltimos, kartangizni kiriting.                              ║
║  (Simulyatorda: 16 xonali karta raqamini kiriting.)          ║
║                                                              ║
║  Misol: 8600123412341234                                     ║
║                                                              ║
║  [0] Bekor qilish va ortga qaytish                           ║
╚══════════════════════════════════════════════════════════════╝
Karta raqami: _"""

auth_pin_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                        🔢PIN TEKSHIRUVI                      ║
╠══════════════════════════════════════════════════════════════╣
║  Karta: 8600 **** **** 1234                                  ║
║                                                              ║
║  4 xonali PIN-kodni kiriting.                                ║
║  Qolgan urinishlar: 3                                        ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
PIN: """


def auth_pin_error_message(tryings: int = 3) -> str:
    return Fore.RED + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                            ❌XATOLIK                          ║
╠══════════════════════════════════════════════════════════════╣
║  PIN noto'g'ri kiritildi.                                    ║
║  Qolgan urinishlar: {tryings}                                ║
║                                                              ║
║  Maslahat: PIN kiritayotganda klaviaturani yopib turing.     ║
╚══════════════════════════════════════════════════════════════╝
Davom etish uchun ENTER bosing... """


auth_blocked_message = Fore.YELLOW + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                     ⚠XAVFSIZLIK OGОHLANTIRISHI               ║
╠══════════════════════════════════════════════════════════════╣
║  Karta 3 marta noto'g'ri PIN sababli BLOKLANDI.              ║
║  Iltimos, bankka murojaat qiling (passport/ID bilan).        ║
║                                                              ║
║  Operatsiya xavfsizlik uchun bekor qilindi.                  ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """


def main_menu_message(account_id: str) -> str:  # todo select from db
    owner = None
    card_number = None
    is_blocked = None

    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                         📉ASOSIY MENYU                       ║
╠══════════════════════════════════════════════════════════════╣
║  Mijoz: {owner + (53 - len(owner)) * " " + '║'}                                              
║  Karta: {card_number + (53 - len(card_number)) * " " + '║'}
║  Sessiya: {'✅AKTIV' + (51 - len('✅AKTIV')) * " " + '║' if not is_blocked else "❌NOFAOL" + (51 - len('❌NOFAOL')) * " " + '║'}
╠══════════════════════════════════════════════════════════════╣
║  [1] Balansni ko'rish                                        ║
║  [2] Naqd pul yechish                                        ║
║  [3] Hisobni to'ldirish (deposit)                            ║
║  [4] Kartadan-kartaga o'tkazma                               ║
║  [5] Tranzaksiyalar tarixi                                   ║
║  [6] PIN-kodni o'zgartirish                                  ║
║  [7] Kartani bloklash (xavfsizlik)                           ║
╠══════════════════════════════════════════════════════════════╣
║  [0] Chiqish / Kartani qaytarish                             ║
╚══════════════════════════════════════════════════════════════╝
Tanlov: _ """


def balance_menu_message(account_id: str) -> str:  # todo select from db
    card_number = ""
    balance = ""
    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                       💰BALANS MA'LUMOTI                     ║
╠══════════════════════════════════════════════════════════════╣
║  Karta: {card_number + (53 - len(card_number)) * " " + '║'}
║                                                              ║
║  Joriy balans: {balance + ' so\'m' + (41 - len(balance)) * " " + '║'}                                
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║  [9] Asosiy menyuga qaytish                                  ║
║  [0] Chiqish                                                 ║
╚══════════════════════════════════════════════════════════════╝
Tanlov: _ """


withdraw_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                       💸NAQD PUL YECHISH                     ║
╠══════════════════════════════════════════════════════════════╣
║  Limitlar: min 10 000 | max 5 000 000                        ║
║  Eslatma: Miqdor 10 000 ga karrali bo'lishi kerak.           ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Miqdor (so'm): _ """


def withdraw_confirmation_message(amount: str) -> str:
    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                     OPERATSIYANI TASDIQLASH                  ║
╠══════════════════════════════════════════════════════════════╣
║  Siz yechmoqchisiz: {amount + ' so\'m' + (36 - len(amount)) * " " + '║'}
║                                                              ║
║  Davom etilsinmi?                                            ║
║  [1] Ha, tasdiqlayman                                        ║
║  [0] Yo'q, bekor qilish                                      ║
╚══════════════════════════════════════════════════════════════╝
Tanlov: _ """


def withdraw_success_message(account_id: str, amount: str) -> str:  # todo select from db
    card_number = "5656"
    balance = "565665465465"
    current_time = datetime.datetime.now()
    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                     ✅AMALIYOT MUVAFFAQIYATLI                 ║
╠══════════════════════════════════════════════════════════════╣
║  Operatsiya: Naqd pul yechish                                ║
║  Miqdor:     {amount + ' so\'m' + (43 - len(amount)) * " " + '║'}
║  Karta:      {card_number + (48 - len(card_number)) * " " + '║'}
║  Sana/vaqt:  {str(current_time) + (48 - len(str(current_time))) * " " + '║'}
║                                                              ║
║  Qolgan balans: {balance + ' so\'m' + (40 - len(balance)) * " " + '║'}
╠══════════════════════════════════════════════════════════════╣
║  Iltimos, pulingizni oling.                                  ║
║  Kartangizni unutmang.                                       ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """


def withdraw_failed_enough_card_money_message(amount: str) -> str:  # todo select from db
    balance = "65656"
    return Fore.RED + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                            ❌XATOLIK                          ║
╠══════════════════════════════════════════════════════════════╣
║  Balans yetarli emas.                                        ║
║  So'ralgan: {amount + ' so\'m' + (43 - len(amount)) * " " + '║'}
║  Mavjud:    {balance + ' so\'m' + (40 - len(balance)) * " " + '║'}
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """


withdraw_not_enough_amount_atm_message = Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                            ❌XATOLIK                          ║
╠══════════════════════════════════════════════════════════════╣
║  Bankomatda yetarli naqd pul yo'q.                           ║
║  Iltimos, boshqa miqdor kiriting yoki keyinroq urinib ko'ring║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """

withdraw_not_suitable_banknote = Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                            ❌XATOLIK                          ║
╠══════════════════════════════════════════════════════════════╣
║  Kiritilgan miqdorni mavjud kupyuralar bilan berib bo'lmadi. ║
║  Maslahat: 10 000 ga karrali miqdor tanlang.                 ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing...

"""

deposit_fill_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                      HISOBNI TO'LDIRISH (DEPOSIT)            ║
╠══════════════════════════════════════════════════════════════╣
║  Hisobingizni to'ldirish uchun miqdor kiriting.              ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Miqdor (so'm): _ """


def deposit_success_message(account_id: str, amount: str):
    card_number = "649865645464"
    balance = "152564646546546"
    current_time = datetime.datetime.now()
    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                       AMALIYOT MUVAFFAQIYATLI                ║
╠══════════════════════════════════════════════════════════════╣
║  Operatsiya: Hisobni to'ldirish                              ║
║  Miqdor:     {amount + ' so\'m' + (43 - len(amount)) * " " + '║'}
║  Karta:      {card_number + (48 - len(card_number)) * " " + '║'}
║  Sana/vaqt:  {str(current_time) + (48 - len(str(current_time))) * " " + '║'}
║                                                              ║
║  Yangi balans: {balance + ' so\'m' + (41 - len(balance)) * " " + '║'}
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """


deposit_failed_message = """
╔══════════════════════════════════════════════════════════════╗
║                            XATOLIK                           ║
╠══════════════════════════════════════════════════════════════╣
║  Miqdor to'g'ri kiriting bo'lishi kerak.                     ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing...

"""

transfer_to_card_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                    KARTADAN-KARTAGA O'TKAZMA                 ║
╠══════════════════════════════════════════════════════════════╣
║  Qabul qiluvchi karta raqamini kiriting (16 xonali).         ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Qabul qiluvchi karta: _ """

transfer_enter_amount_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                    KARTADAN-KARTAGA O'TKAZMA                 ║
╠══════════════════════════════════════════════════════════════╣
║  O'tkazma miqdorini kiriting.                                ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Miqdor (so'm): _ """


def transfer_confirm_message(amount: str, to_card: str):
    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                     OPERATSIYANI TASDIQLASH                  ║
╠══════════════════════════════════════════════════════════════╣
║  Kimga:   {to_card + (51 - len(to_card)) * " " + '║'}
║  Miqdor:  {amount + ' so\'m' + (46 - len(amount)) * " " + '║'}
║                                                              ║
║  Davom etilsinmi?                                            ║
║  [1] Ha, tasdiqlayman                                        ║
║  [0] Yo'q, bekor qilish                                      ║
╚══════════════════════════════════════════════════════════════╝
Tanlov: _

"""


def transfer_success_message(to_card: str, amount: str):
    current_time = datetime.datetime.now()
    return Fore.GREEN + Style.BRIGHT + f"""
╔══════════════════════════════════════════════════════════════╗
║                       AMALIYOT MUVAFFAQIYATLI                ║
╠══════════════════════════════════════════════════════════════╣
║  Operatsiya: Kartadan-kartaga o'tkazma                       ║
║  Kimga:     {to_card + (51 - len(to_card)) * " " + '║'}
║  Miqdor:    {amount + ' so\'m' + (46 - len(amount)) * " " + '║'}
║  Sana/vaqt: {str(current_time) + (48 - len(str(current_time))) * " " + '║'}                                    ║
║                                                              ║
║  Qolgan balans: 1 400 000 so'm                               ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """


transfer_card_not_found_message = Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                            XATOLIK                           ║
╠══════════════════════════════════════════════════════════════╣
║  Qabul qiluvchi karta topilmadi.                             ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """

transfer_to_yourself_message = Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                            XATOLIK                           ║
╠══════════════════════════════════════════════════════════════╣
║  O'zingizga o'zingiz pul yubora olmaysiz.                    ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """

transaction_history = Fore.GREEN + Style.BRIGHT + """
╔═══════════════════════════════════════════════════════════════════╗
║                  TRANZAKSIYALAR TARIXI (OXIRGI 10)                ║
╠═══════════════════════════════════════════════════════════════════╣
║  1) 2026-02-03 12:48 | TRANSFER_OUT | -150 000 | Balans: 1 400k   ║
║  2) 2026-02-03 12:45 | DEPOSIT       | +300 000 | Balans: 1 550k  ║
║  3) 2026-02-03 12:43 | WITHDRAW      | -200 000 | Balans: 1 050k  ║
║                                                                   ║
║  (Agar tarix bo'sh bo'lsa: "Tranzaksiya mavjud emas")             ║
╠═══════════════════════════════════════════════════════════════════╣
║  [9] Asosiy menyuga qaytish                                       ║
║  [0] Chiqish                                                      ║
╚═══════════════════════════════════════════════════════════════════╝
Tanlov: _ """

old_pin_code_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                      PIN-KODNI O'ZGARTIRISH                  ║
╠══════════════════════════════════════════════════════════════╣
║  Xavfsizlik uchun eski PIN-kodni kiriting.                   ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Eski PIN: _ _ _ _ """

new_pin_code_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                      PIN-KODNI O'ZGARTIRISH                  ║
╠══════════════════════════════════════════════════════════════╣
║  Yangi 4 xonali PIN-kodni kiriting.                          ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Yangi PIN: _ _ _ _ """

new_pincode_confirmation_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                      PIN-KODNI O'ZGARTIRISH                  ║
╠══════════════════════════════════════════════════════════════╣
║  Yangi PIN-kodni qaytadan kiriting (tasdiqlash).             ║
║                                                              ║
║  [0] Bekor qilish                                            ║
╚══════════════════════════════════════════════════════════════╝
Tasdiqlash PIN: _ _ _ _ """

pin_updated_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                       AMALIYOT MUVAFFAQIYATLI                ║
╠══════════════════════════════════════════════════════════════╣
║  PIN-kodingiz muvaffaqiyatli o'zgartirildi.                  ║
║  Iltimos, yangi PIN-ni hech kimga aytmang.                   ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """

error_in_old_pin_message = Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                            XATOLIK                           ║
╠══════════════════════════════════════════════════════════════╣
║  Eski PIN noto'g'ri kiritildi.                               ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """

not_matched_new_pin_message = Fore.RED + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                            XATOLIK                           ║
╠══════════════════════════════════════════════════════════════╣
║  Yangi PIN va tasdiqlash PIN mos kelmadi.                    ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """

self_block_message = Fore.YELLOW + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                     KARTANI BLOKLASH (XAVFSIZLIK)            ║
╠══════════════════════════════════════════════════════════════╣
║  Diqqat! Kartani bloklasangiz, ATM orqali kira olmaysiz.     ║
║  Keyin bankka murojaat qilish kerak bo'ladi.                 ║
║                                                              ║
║  Davom etilsinmi?                                            ║
║  [1] Ha, kartani bloklayman                                  ║
║  [0] Yo'q, bekor qilish                                      ║
╚══════════════════════════════════════════════════════════════╝
Tanlov: _ """

logout_message = Fore.GREEN + Style.BRIGHT + """
╔══════════════════════════════════════════════════════════════╗
║                           CHIQISH                            ║
╠══════════════════════════════════════════════════════════════╣
║  Kartangiz qaytarildi.                                       ║
║  Bankomatdan foydalanganingiz uchun rahmat!                  ║
║                                                              ║
║  Xavfsizlik eslatmasi:                                       ║
║    • Chekingizni (agar bo'lsa) olib keting.                  ║
║    • Hech kimga PIN aytmang.                                 ║
╚══════════════════════════════════════════════════════════════╝
ENTER bosing... """
