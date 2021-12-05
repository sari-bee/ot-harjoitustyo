from pathlib import Path
from entities.sample import Sample


class SampleRepository:

    def __init__(self, path: str):
        self.path = path

    def read(self):
        samples = []
        Path(self.path).touch()
        with open(self.path) as file:
            for row in file:
                if row == "":
                    pass
                if row == "\n":
                    pass
                row = row.replace("\n", "")
                split = row.split(";")
                sample_id = split[0]
                comment = split[1]
                anti_a = int(split[2])
                anti_b = int(split[3])
                anti_d = int(split[4])
                control = int(split[5])
                a1_cell = int(split[6])
                b_cell = int(split[7])
                timestamp = split[8]
                sample = Sample(sample_id, comment, anti_a,
                                anti_b, anti_d, control, a1_cell, b_cell, timestamp)
                samples.append(sample)
        return samples

    def write(self, samples):
        Path(self.path).touch()
        with open(self.path, "w") as file:
            for sample in samples:
                row = f"{sample.sample_id};{sample.comment};{sample.anti_a};{sample.anti_b};{sample.anti_d};{sample.control};{sample.a1_cell};{sample.b_cell};{sample.timestamp}\n"
                file.write(row)

    def add_sample(self, added_sample: Sample):
        samples = self.read()
        for sample in samples:
            if sample.sample_id == added_sample.sample_id:
                return False
        samples.append(added_sample)
        self.write(samples)
        return True

    def get_sample_by_id(self, wanted_sample_id: str):
        samples = self.read()
        for sample in samples:
            if sample.sample_id == wanted_sample_id:
                return sample
        return None
