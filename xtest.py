class Cos():

    def number_of_exercises(self):
        noe = input("How many different exercises did you do today?: ")
        try:
            int(noe)
            return noe
        except ValueError:
            print("Input number please.")
            self.number_of_exercises()


    def take(self, x):
        for item in range(int(x)):
            yield input("Exercise name: ")

    def generate_list_of_exercises(self):
        noe = int(self.number_of_exercises())
        w = self.take(noe)
        return [ex for ex in w]


    def wlacz(self):
        print(self.generate_list_of_exercises())

d = Cos()

d.wlacz()


