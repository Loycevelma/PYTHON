class Car:
    def __init__(self,make,model,color,speed):
        self.make=make
        self.model=model
        self.color=color
        self.speed=speed


    def hoot(self):
        return f"Hello  i love {self.make} {self.model} of  color {self.color}  running at a speed of{self.speed} per hour"
    def  breakDown(self):
                return f"Hello my {self.make} {self.model} of  color {self.color}  running at a speed of{self.speed} per hour  broke down"

        