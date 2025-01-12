import requests 
from pprint import pprint


r = requests.get("https://nbu.uz/uz/exchange-rates/json/")

courses = r.json()

pprint(courses)

while True:


    print("Bizda mavjud valyuta kurslari ")
    print("Dasturdan chiqishni xohlasangiz 0 ni bosing ")
    for course in courses:
        pprint(course["code"])


        currency_unit = float(input("Summani kiriting "))
        from_convert = input("- Qaysi valyutadan konvertatsiya qilinadi  ").upper()
        to_converter = input("- Qaysi valyutaga konvertatsiya qilinadi ").upper()


        currency_course = None
        to_currency_course = None


        if currency_unit == 0:
            print("Siuz dasturni tark etdingiz ")

        break


    for money_course in courses:


        if money_course["code"] == from_convert:
            currency_course = float(money_course["cb_price"])
         

        if money_course["code"] == to_converter:
            to_currency_course = float(money_course["cb_price"])


        if currency_course and to_currency_course:
           result = (currency_unit * currency_course) / to_currency_course
           print(f"{Style.DIM} + {Fore.RED}Natija: = {result},{Style.RESET_ALL}")

        elif from_convert == money_course["code"] and to_converter == money_course["code"]:

           for course in courses:
            pprint(course["code"])
            pprint("Siz mavjud bo'lmagan valyuta kiritdingiz... Chiqmoqchi bo'lsangiz 0 ni kiriting ")