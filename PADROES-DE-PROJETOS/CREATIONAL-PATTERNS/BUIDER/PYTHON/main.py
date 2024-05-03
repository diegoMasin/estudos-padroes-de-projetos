class Car:
    def __init__(self, model, color, wheels, engine):
        self.model = model
        self.color = color
        self.wheels = wheels
        self.engine = engine

    def __str__(self):
        return f"Modelo: {self.model}, Cor: {self.color}, Rodas: {self.wheels}, Motor: {self.engine}"


class CarBuilder:
    def __init__(self):
        self.car = None

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def build(self):
        return self.car


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_model("Sedan") \
            .set_color("Preto") \
            .set_wheels(4) \
            .set_engine("Motor a combustão")

        return self.builder.build()


# Uso do Builder
builder = CarBuilder()
director = Director(builder)
car = director.construct()

print(car)
