class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print("Hayvon ovoz chiqaradi")


class Dog(Animal):
    def __init__(self, name, sound, breed, age):
        super().__init__(name, sound)
        self.breed = breed
        self.age = age

    def speak(self):
        super().speak()
        print(f"{self.name} {self.sound} deydi")
        print(f"Zot: {self.breed}")

    def info(self):
        print(f"Yoshi: {self.age}")
