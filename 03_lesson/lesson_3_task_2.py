from smartphone import Smartphone

phone1 = Smartphone("iPhone", "15", "+79111111111")
phone2 = Smartphone("Samsung", "S24", "+79991234567")
phone3 = Smartphone("Xiaomi", "14", "+79533216547")
phone4 = Smartphone("Google", "Pixel", "+79258765432")
phone5 = Smartphone("OnePlus", "12", "+79211122334")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')
