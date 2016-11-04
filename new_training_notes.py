import csv


class Application(object):

    def __init__(self, data_file_name="big6.csv"):
        self._data_file_name = data_file_name

    def new_note(self):
        with open(self._data_file_name, "a+", newline="") as f:
            note_name = self._note_name()
            start_time = self._start_time
            exercises = self.generate_list_of_exercises()
            series =
            repeats = {}

            if input("Note name")
            csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow(note_name,)


    def _note_name(self):
        note_name = input("Note name: ")
        try:
            if self.notes_into_dict[note_name] is not None:
                print("This note name already exist")
                self._note_name()
            elif self.notes_into_dict[note_name] is KeyError:
                pass
        except KeyError:
            return note_name

    def _start_time(self):
        print("At first input just hour, accept and enter minutes")
        h_str = input("Hour: ")
        try:
            int(h_str)
        except ValueError:
            print("Input number please.")
            self._start_time()
        m_str = input("Minutes: ")
        try:
            int(m_str)
        except ValueError:
            print("Input number please.")
            self._start_time()
        start_time = ("{}:{}".format(h_str, m_str))
        return start_time

    #  Exercises: 1 - just number, 2 - genertor, 3 - run generator
 #  1
    def number_of_exercises(self):
        noe = input("How many different exercises did you do today?: ")
        try:
            int(noe)
        except ValueError:
            print("Input number please.")
            self.number_of_exercises()
        return noe
 #  2
    def gen_of_exercises_names(self, vert):
        for item in range(int(vert)):
            yield input("Exercise name: ")
 #  3
    def generate_list_of_exercises(self):
        noe = int(self.number_of_exercises())
        w = self.gen_of_exercises_names(noe)
        return [next(w) for _ in range(0, noe)]

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