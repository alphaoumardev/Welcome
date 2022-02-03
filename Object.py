class Diallo:
    def __init__(self, name, age, will):
        self.name = name
        self.age = age
        self.will = will

    def me(self):
        print(self.age)

    def alpha(self):
        print(self.name)

    def smile(self):
        print(self.will)


the_object = Diallo("Alpha oumar", 21, "The third parameterd")
print("The format of the object is {} {} {}".format(the_object.name, the_object.age, the_object.will))
print(the_object.age)
the_object.me()
the_object.alpha()
the_object.smile()


class Barry(Diallo):
    def __init__(self, name, age, will):
        # super().__init__(name,age,will)
        super().__init__(name, age, will)
        print("bonjouroumar")

    # def you(self):
    #     print("alllll")
    def you(self):
        pass


inherit = Barry()
inherit.you()
inherit.me()
