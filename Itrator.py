atuple = ("alpha ", "oumar", "diallo")
ite = iter(atuple)
print(ite)
print(next(ite))
print(next(ite), next(ite))
for alpha in atuple:
    print(alpha)


class Ite:
    def __iter__(self):
        self.al = 1
        return self

    def __next__(self):
        me = self.al
        self.al += 3
        return me


alls = Ite()
the_iter = iter(alls)
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))
print(next(the_iter))


class Iteration:
    def __iter__(self):
        self.the_iter = 0
        return self

    def __next__(self):
        if self.the_iter <= 20:
            nexts = self.the_iter
            self.the_iter += 5
            return nexts
        else:
            return StopIteration


theItration = Iteration()
itra = iter(theItration)
print(next(itra))
print(next(itra)), print(next(itra)), print(next(itra)), print(next(itra))


#  The variable'Scope In python
def alpha():
    diallo = 21
    print(diallo)

    def innerFunct():
        print(diallo)

    innerFunct()  # to call the innerFunction


# print(diallo) #That will occur an error "Diallo is not defined"
print(atuple)
alpha()


def youIn(diallo):
    return diallo
    # print(diallo)


youIn("edopas")

person = {
    "name": "Alpha oumar Diallo",
    "age": 21,
    "height": 180,
    "weight": 70,
}
