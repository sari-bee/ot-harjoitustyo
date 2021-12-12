from pathlib import Path
from entities.sample import Sample


class SampleRepository:

    """Luokka, joka huolehtii näyteolioiden tallentamisesta ja lukemisesta csv-tiedostoon.

    Attributes:
        path: Polku konekohtaiseen csv-tiedostoon.
    """

    def __init__(self, path):
        """Luokan konstruktori, joka luo ohjelman käynnistyskertakohtaisen näyterepositoryn.

        Args:
            path (str): Polku konekohtaiseen csv-tiedostoon.
        """
        self.path = path

    def read(self):
        """Metodi lukee talletettujen näytteiden tiedot konekohtaisesta csv-tiedostosta ja muuntaa ne listaksi näyteolioita.

        Returns:
            Lista: Tallennetut näyteoliot
        """
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
        """Metodi tallentaa näyteoliot konekohtaiseen csv-tiedostoon.

        Args:
            samples (list): Lista näyteolioita
        """
        Path(self.path).touch()
        with open(self.path, "w") as file:
            for sample in samples:
                row = f"{sample.sample_id};{sample.comment};{sample.anti_a};{sample.anti_b};{sample.anti_d};{sample.control};{sample.a1_cell};{sample.b_cell};{sample.timestamp}\n"
                file.write(row)

    def add_sample(self, added_sample):
        """Lisää uuden näyteolion tallennettujen näytteiden tiedostoon.

        Args:
            added_sample (Sample): Näyteolio

        Returns:
            False: jos lisättävän näytteen näytetunniste löytyy jo tallennettujen näytteiden listalta
            True: jos näytteen lisäys onnistui (eli näytetunniste oli uniikki)
        """
        samples = self.read()
        for sample in samples:
            if sample.sample_id == added_sample.sample_id:
                return False
        samples.append(added_sample)
        self.write(samples)
        return True

    def get_sample_by_id(self, wanted_sample_id):
        """Noutaa näyteolion näytetunnisteen perusteella

        Args:
            wanted_sample_id (str): Halutun näytteen näytetunniste

        Returns:
            Sample: Haluttu näyteolio
            None: jos etsittävää näytetunnistetta ei löydy
        """
        samples = self.read()
        for sample in samples:
            if sample.sample_id == wanted_sample_id:
                return sample
        return None
