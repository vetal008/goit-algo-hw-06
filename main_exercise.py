from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isnumeric():
            super().__init__(value)
        else:
            raise TypeError("Phone number must be 10 digits")

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    """Знаходження номеру"""
    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    """Додавання номера"""
    def add_phone(self, phone: str):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise ValueError('Phone already added')

    """Видалення номера"""
    def remove_phone(self, phone: str):
        if self.find_phone(phone):
            self.phones.remove(self.find_phone(phone))
        else:
            raise ValueError('No such phone')

    """Зміна номеру"""
    def edit_phone(self, phone: str, new_phone: str):
        if self.find_phone(phone):
            self.phones.remove(self.find_phone(phone))
            self.phones.append(Phone(new_phone))
        else:
            raise ValueError('No such phone')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)};"

class AddressBook(UserDict):

    """Додавання нового запису до книги"""
    def add_record(self, record: Record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            raise ValueError('Record with the same name already added')

    """Знаходження рекорду за ім'ям"""
    def find(self, name: str):
        if self.data:
            return self.data[name]
        else:
            return None

    """Видалення рекорду"""
    def delete(self, name: str):
        if name in self.data.keys():
            del self.data[name]

    def __str__(self):
        if self.data:
            address_str = str()
            for elem in self.data.keys():
                address_str += (str(self.data[elem]) + '\n')
            address_str += '--------------------'
            return address_str
        else:
            return "No Phones"

if __name__ == '__main__':
    book = AddressBook()   # Створення книги записів
    ivan = Record('Ivan')  # Створення рекорду
    john = Record('John')  # Створення ще одного рекорду
    john.add_phone('9999999999')   # Додавання номеру до першого рекорду
    ivan.add_phone('3333333333')   # Ще раз додаємо номер
    ivan.add_phone('4444444444')   # І ще один раз для зручності
    book.add_record(ivan)          # Додавання рекорду до книги
    print(book)   # Принтування для перевірки
    ivan.remove_phone('3333333333')   # Видалення одного з номерів
    ivan.edit_phone('4444444444', '1234567890')   # Зміна одного з номеру
    book.add_record(john)     # Додавання другого рекорду до книги
    # book.add_record(john)    """Якщо розкоментувати, то буде помилка оскільки рекорд з таким ім'ям вже є"""
    print(book)     # Принтування для перевірки
    book.delete('John')   # Видалення другого рекорду з книги
    print(book)     # Принтування для перевірки






