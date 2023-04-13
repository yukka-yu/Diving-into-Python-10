'''Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.'''

'''Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.'''

class Animal:
    def __init__(self, kind, name_, age, weight, color, voice):
        self.kind = kind
        self.name_ = name_
        self.age = age
        self.weight = weight
        self.color = color
        self.voice = voice
    
    def get_info(self):
        print(f'{self.__class__.__name__} {self.kind} {self.name_} is {self.age} years old, its weight is {self.weight} kg, it\'s {self.color} and can say {self.voice}')




class Mammal(Animal):
    def __init__(self, run_speed, *args, **kwargs):
        self.run_speed = run_speed
        super().__init__(*args, **kwargs)

    def get_mammal_info(self):
        super().get_info()
        print(f'It can run with speed {self.run_speed} km/h')

class Fish(Animal):
    def __init__(self, swim_depth, *args, **kwargs):
        self.swim_depth = swim_depth
        self.voice ='blob'
        super().__init__(*args, **kwargs)
        

    def get_fish_info(self):
        super().get_info()
        print(f'It can swim to depth {self.swim_depth} m')

class Bird(Animal):
    def __init__(self, fly_height, *args, **kwargs):
        self.fly_height = fly_height
        super().__init__(*args, **kwargs)
        
    def get_bird_info(self):
        super().get_info()
        print(f'It can fly on height to {self.fly_height} m')


mammal1 = Mammal(60, 'cheetah', 'Freddy', 3, 25, 'spotted', 'r-r-miu')
mammal1.get_mammal_info() 

fish1 = Fish(2, 'guppy', 'Flore', 1, 0.005, 'green', 'blob')
fish1.get_fish_info()

bird1 = Bird(1, 'ostrich', 'Tom', 5, 35, 'black\'n\'white', 'crrr')
bird1.get_bird_info()


class AnimalFactory:
    def __init__(self, class_name, *args):
        self.class_name = class_name
        self.args = args

    def create_animal(self):
        return self.class_name(*self.args)
    
af1 = AnimalFactory(Fish, 3, 'guppy', 'Fi', 1, 0.005, 'blue', 'blob')
fish2 = af1.create_animal()
fish2.get_fish_info()

    
