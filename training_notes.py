import csv


class Tools(object):

    def __init__(self, data_file_name="big6.csv"):
        self._data_file_name = data_file_name

    def new_note(self):
        with open(self._data_file_name, "a+", newline="") as f:
            f.seek(self.lines_in_data_file() + 2)
            csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow([
                input("Note name: "),
                input("Start time: "),
                input("What exercise(if more than 1 separate by '/'?: "),
                input("How many series?: "),
                input("How many times each run, separate by '/'?: ")
                                                                                            ])

    def lines_in_data_file(self):
        with open(self._data_file_name, "r") as f:
            return len([1 for _ in f])

    @property
    def notes_into_dict(self):
        data_ceeper = {}
        with open(self._data_file_name, "r") as f:
            f_reader = csv.reader(f, delimiter=' ', quotechar='|')
            for row in f_reader:
                try:
                    data_ceeper.update({row[0]: [row[1], row[2], row[3], row[4]]})
                except IndexError:
                    continue
        return data_ceeper

    def search_dict(self):
        search_in = self.notes_into_dict
        try:
            print("Notes names list: ")
            print([key for key in search_in.keys()])
            note_name = input("Input note name to read")
            try:
                exercise_ = ([search_in[note_name][1].split("/")[0],
                             (search_in[note_name][1].split("/")[1])])
            except IndexError:
                exercise_ = search_in[note_name][1]
            ser_ = search_in[note_name][2]
            rep_ = search_in[note_name][3]
            if type(exercise_) == list:
                try:
                    ser_ = [search_in[note_name][2].split("/")[0],
                            search_in[note_name][2].split("/")[1]]
                    rep_ = [search_in[note_name][3].split("/")[0],
                            search_in[note_name][3].split("/")[1]]
                except IndexError:
                    print("Mistake in entered search_in[note_name]! Input note again.")
            elif type(exercise_) != list:
                ser_ = search_in[note_name][2]
                rep_ = search_in[note_name][3]

            print("Training note: ", note_name)
            print("Start time:    ", search_in[note_name][0])
            print("Exercise:      ", exercise_)
            print("Series:        ", ser_)
            print("Repeats:       ", rep_)
            print("Suammary:"
                  "At this training you did\n",
                  exercise_[0], " ", ser_[0], " x ", rep_[0],
                  exercise_[1], " ", ser_[], " x ", rep_[0],
                  exercise_[0], " ", ser_[0], " x ", rep_[0],)
        except KeyError:
            print("Wrong name")
            self.search_dict()

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
            self.search_dict()
            self.run_app()
        if x == 3:
            print("exit")

if __name__ == "__main__":
    s = Tools()
    s.run_app()
    print(s.notes_into_dict)
