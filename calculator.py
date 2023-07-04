class Calculator:
    def __int__(self, x, y):
        self.x = x,
        self.y = y

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

    try:
        def div(self):
        return x/y
    except ZeroDivisionError as err:
        return print( "Dividing by Zero!")

    def mul(self):
        return self.x * self.y

    def sub(self):
        return "stuff"

    def add(self):
        return self.x + self.y