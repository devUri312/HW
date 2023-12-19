class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        
class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self):
        print("True in the True_phrase")

    def display_name(self):
        print(f'Имя героя: {self.name}')

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def true_in_true_phrase(self):
        print("True in the True_phrase")

    def display_name(self):
        print(f'Имя героя: {self.name}')

class Villain(EarthHero):  # Наследование от EarthHero
    people = 'monster'

    def gen_x(self):
        pass  # Пока ничего не делает

    def crit(self, target):
        target.health_points -= self.damage ** 2

# Создаем объекты
air_hero = AirHero(
    name='Aeroman',
    nickname='Skywalker',
    superpower='Control of the air',
    health_points=75,
    catchphrase='I am the wind beneath your wings!',
    damage=10
)

earth_hero = EarthHero(
    name='Terraman',
    nickname='Earthquake',
    superpower='Manipulation of earth',
    health_points=80,
    catchphrase='Feel the ground tremble!',
    damage=12
)

villain = Villain(
    name='Darkness',
    nickname='Shadowmaster',
    superpower='Dark magic',
    health_points=100,
    catchphrase='In the shadows, I thrive!',
    damage=15
)

# Вызываем методы
air_hero.display_name()
air_hero.double_health()
air_hero.true_in_true_phrase()
print(air_hero)

earth_hero.display_name()
earth_hero.double_health()
earth_hero.true_in_true_phrase()
print(earth_hero)

villain.display_name()
villain.double_health()
villain.true_in_true_phrase()
print(villain)

# Применяем метод crit
villain.crit(earth_hero)
print(f"Health points of {earth_hero.name} after the crit: {earth_hero.health_points}")
