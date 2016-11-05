import csv


class Application(object):

    def __init__(self, data_file_name="big6.csv"):
        self._data_file_name = data_file_name

    def new_note(self):
        line_of_text = []
        line_of_text.append(self._note_name())
        line_of_text.append(self._start_time())
        exercises = self.generate_list_of_exercises()
        series = self._series(exercises)
        line_of_text.append(exercises)
        line_of_text.append(series)
        line_of_text.append(self._repeats(exercises, series))
        with open(self._data_file_name, "a+", newline="") as f:

            csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL).\
                writerow(line_of_text)

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
            return self.number_of_exercises()
        return int(noe)
#  2

    def gen_of_exercises_names(self, vert):
        for item in range(int(vert)):
            yield input("Exercise name: ")
#  3

    def generate_list_of_exercises(self):
        noe = self.number_of_exercises()
        w = self.gen_of_exercises_names(noe)
        return [next(w) for _ in range(0, noe)]

    def _series(self, exercises):
        series = []
        for ex in exercises:
            ex = int(input("Number of series {}: ".format(ex)))
            series.append(ex)
        return series

    def _repeats(self, exercises, series):
        repeats = []
        for x in range(len(series)):
            repeats.append([])
        series_counter = 1
        for ex in exercises:
            n2 = 1
            print(series[series_counter-1])
            print(type(series[series_counter-1]))
            for serie in range(0, int(series[series_counter-1])):
                x = int(input("Number of repeats in {} serie {} : ".format(ex, n2)))
                repeats[n2-1].append(x)
                n2 += 1
                return repeats[n2-2]  # <<there, return one list with integer and ends loop, how to make it loop again?
            series_counter += 1


    @property
    def notes_into_dict(self):
        data_ceeper = {}
        with open(self._data_file_name, "r") as f:
            f_reader = csv.reader(f, delimiter=' ', quotechar='|')
            for row in f_reader:
                try:
                    data_ceeper.update({row[0]: [row[1], row[2], row[3], row[4], row[5]]})
                except IndexError:
                    continue
        return data_ceeper

    def search_dict(self):
        search_in = self.notes_into_dict
        try:
            print("Note names list: ")
            print(sorted([key for key in search_in.keys()]))
            note_name = input("Input note name to read: ")
            return search_in[note_name]
        except KeyError:
            print("Wrong note name. Try again.")
            return self.search_dict()

if __name__ == "__main__":
    d = Application()
    d.new_note()
