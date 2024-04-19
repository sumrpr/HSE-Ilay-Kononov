'''
Опишите любую абстракцию (желательно юридическую, но вы можете выбрать любую
другую) с помощью инструментов ООП (например, Истец-Ответчик, ПравоОбязательство, Срок, Судья и др.).
Придумайте атрибуты и методы для абстракции. Если ничего не приходит на ум, просто
дополните абстракцию (класс) из домашнего задания № 7 любыми атрибутами и
методами на ваше усмотрение

У меня пока не получается осуществлять динамические изменения внутри кода.
Тут либо нужен иной интерфейс, либо иначе вводит начальные данные, так как сейчас все изменения
просто переписываются начальными данными. Тут, наверное, нужен свой event_handler и держать программу на 
while true. Как-то так. Но задание, думаю, выполнено
'''

class Player:
    def __init__(self, class_, race, hp):
        self.hp = hp
        self.abilities = []
        self.class_= class_
        self.race = race
        
    def creat_character(self):
        self.character = [
            self.class_,
            self.race,
            self.hp,
            self.abilities
        ]
    
    def change_hp(self, type, ammount):
        if type == 'heal':
            self.hp += ammount
        if type == 'damage':
            self.hp -= ammount
        return(Player.creat_character(self))
    
    def add_ability(self, name):
        self.abilities.append(name)
    
    def change_class(self, newclass):
        self.class_ = newclass
    
    def change_race(self, newrace):
        self.race = newrace

Davakin = Player('Маг', 'Норд', 190)

Davakin.add_ability('fus-ro-dha!')

Davakin.change_hp('damage', 10)

print(*Davakin.character, sep='\n')
