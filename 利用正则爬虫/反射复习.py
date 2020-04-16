class Dog:
    def eat(self):
        print("Dog is eating!")

def cat():
    eat = "Cat is eating!"

if __name__ == '__main__':
    if hasattr(cat,"eat"):
        print(getattr(cat,"eat"))
    # d = Dog()
    # if hasattr(d,"eat"):
    #     getattr(d,"eat")()