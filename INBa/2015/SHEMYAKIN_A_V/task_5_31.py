creators = ["Кирилл", "Мефодий"] #список создателей
import random as random_number; #импорт оператора random
print ("Данная программа выводит имя одного из создателей старославянской азбуки в случайном порядке");
print (random_number.choice(creators)); #случайный выбор из списка
input ("Press Enter to exit");
