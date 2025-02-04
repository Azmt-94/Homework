class Vehicle:
    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    _COLOR_VARIANTS = ['black', 'white', 'green', 'blue', 'red']

    def set_color(self, new_color):
        if new_color.lower() in Vehicle._COLOR_VARIANTS:
            self._color = new_color
        else:
                print(f'Нельзя сменить цвет на {new_color}')

    def get_model(self):
        return self._model

    def get_engine_power(self):
        return self._engine_power

    def get_color(self):
        return self._color

    def print_info(self):
        return print(f"Владелец : {self.owner}\nМодель : {self._model}\n"
                     f"Мощность двигателя : {self._engine_power}\nЦвет : {self._color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
