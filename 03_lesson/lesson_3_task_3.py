from address import Address
from mail import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "5")
from_addr = Address("654321", "СПб", "Невский", "25", "3")

mailing = Mailing(to_addr, from_addr, 250, "RB123456789CN")

print(f"""Отправление {mailing.track} из {mailing.from_address.index}, {
    mailing.from_address.city}, {mailing.from_address.street}, {
    mailing.from_address.house} - {mailing.from_address.apartment} в {
    mailing.to_address.index}, {mailing.to_address.city}, {
    mailing.to_address.street}, {mailing.to_address.house} - {
    mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.""")
