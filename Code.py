class Code:

    variables = []
    regions = []
    code = ""
    past_codes = []
    result = ""
    past_results = []

    def __init__(self, path):
        self.path = path
        self.determine_regions()

    def determine_regions(self):
        if self.code == "":
            self.regions.append([0, 0])
        else:
            pass

    def write_code(self, nr_lines):
        pass

    def write_variable(self):
        pass

    def write_if_block(self):
        pass

    def write_while_block(self):
        pass

