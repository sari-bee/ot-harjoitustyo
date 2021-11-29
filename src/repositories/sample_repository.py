from entities.sample import Sample


class SampleRepository:

    def __init__(self):
        self.samples = []

    def add_sample(self, sample: Sample):
        for ex in self.samples:
            if ex.sample_id == sample.sample_id:
                return False
        self.samples.append(sample)
        return True

    def get_sample(self, sample_id: str):
        for sample in self.samples:
            if sample.sample_id == sample_id:
                return sample
        return None
