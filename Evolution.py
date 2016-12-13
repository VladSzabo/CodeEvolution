from Code import Code
import os


class Evolution:

    generation = 1
    pause = False
    run = True
    codes = []
    stage = 0

    def __init__(self, species_per_generation, processes_per_run, lines_per_generation, run_time):
        self.species_per_generation = species_per_generation
        self.processes_per_run = processes_per_run
        self.lines_per_generation = lines_per_generation
        self.run_time = run_time
        self.create_generation()

    def run_evolution(self):

        while self.run:

            if not self.pause:
                if self.stage == 0:
                    self.read_generation()
                elif self.stage == 1:
                    self.mutate_species()
                elif self.stage == 2:
                    self.test_species()
                elif self.stage == 3:
                    self.selection()
                elif self.stage == 4:
                    self.results()

    def create_generation(self):
        folders = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\gen\\")
        survived_species = len(folders)

        for i in range(self.species_per_generation - survived_species):
            self.codes.append(Code("gen/s" + str(i) + "/code.py", ""))
            os.makedirs("gen/s" + str(i))
            open("gen/s" + str(i) + "/code.py", 'a').close()
            open("gen/s" + str(i) + "/output.txt", 'a').close()

    def read_generation(self):

        folders = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\gen\\")

        for i in folders:
            code = open("gen/" + i + "/code.py").read()

            if len(code) > 3:
                self.codes[int(i[1:])].past_results.append(self.codes[int(i[1:])].result)
                self.codes[int(i[1:])].past_codes.append(self.codes[int(i[1:])].code)
                self.codes[int(i[1:])].code = code
            else:
                self.codes[int(i[1:])].code = ""

        self.stage = 1

    def mutate_species(self):
        pass

    def test_species(self):
        pass

    def selection(self):
        pass

    def results(self):
        pass




