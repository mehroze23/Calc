class Calculator:
    def __int__(self, x, y):
        self.x = x,
        self.y = y

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

    def div(self):
        return f"Division result is: {self.x/self.y}"

    def mul(self):
        return self.x * self.y

    def sub(self):
        return f"Subtration result is {self.x-self.y}"
 
    def add(self):
        return self.x + self.y