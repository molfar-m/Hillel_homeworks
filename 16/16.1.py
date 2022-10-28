class Human:

    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address,
        }

    def call(self, phone_number):
        return f'{self.phone} вызывает абонента {phone_number}'


human1 = Human('Volodymyr', 'Pohrebniak', 32, '+38(067)-481-98-70', 'Odessa')
human2 = Human('Evgenij', 'Stojanov', 35, '+38(067)-432-95-77', 'Kyiv')
human3 = Human('Roman', 'Gora', 19, '+38(050)-431-54-89', 'Kharkiv')

print(human1.get_info())
print(human2.get_info())
print(human3.get_info())
print(human1.call('+38(050)-431-54-89'))
