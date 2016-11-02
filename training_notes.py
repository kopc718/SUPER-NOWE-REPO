import csv


class Tools(object):

    def __init__(self, data_file_name="big6.csv"):
        self._data_file_name = data_file_name

    def new_note(self):
        note_name = str(input("Date in format dd/mm/yyyy: "))

        with open(self._data_file_name, "a+", newline="") as f:
            f.seek(self.lines_in_data_file() + 2)
            csv.writer(f, delimiter="|").writerow(
                    "{a}|{b}{c}{d}{e}\n".format(a=note_name,
                                                b=input("Which body part: "),
                                                c=input("What exercise?: "),
                                                d=int(input("How many series?: ")),
                                                e=input("How many times per serie, separate by '/'?: "))
                                                 )

    def lines_in_data_file(self):
        with open(self._data_file_name, "r") as f:
            return len([1 for _ in f])

    @property
    def notes_into_dict(self):
        data_ceeper = {}
        with open(self._data_file_name, "r") as f:
            for row in f:
                print(row)
        return data_ceeper

    def search_dict(self, search_in):
        try:
            print("Notes names list: ")
            print([key for key in search_in.keys()])
            print(search_in[input("Input note name to read")])
        except KeyError:
            print("Wrong name")
            self.search_dict(search_in)

    def exercises_data_counter(self):
        pass

    def run_app(self):
        x = int(input("\n"
                      "\n\n"
                      ""
                      "1 => NEW NOTE \n"
                      "2 => OPEN TRAINING NOTE \n"
                      "3 => Exit\n"
                      "Input number and push ENTER to accept: "))
        if x == 1:
            self.new_note()
            self.run_app()

        if x == 2:
            td = self.notes_into_dict
            self.search_dict(td)
            self.run_app()
        if x == 3:
            print("exit")

if __name__ == "__main__":
    s = Tools()
    s.run_app()
    print(s.notes_into_dict)
