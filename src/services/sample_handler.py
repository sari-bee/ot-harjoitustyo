from datetime import datetime
from repositories.sample_repository import SampleRepository
from entities.sample import Sample
from services.listing_service import ListingService
from config import SAMPLES_FILEPATH


class SampleHandler:

    """Luokka, joka hoitaa kaiken näytteisiin liittyvän logiikan käyttöliittymän kanssa.

    Attributes:
        sample_repository: Ohjelman käynnistyskertakohtainen näyterepository
    """

    def __init__(self):
        """Luokan konstruktori, joka luo näytepalvelun ja näyterepositoryn
        """

        self.sample_repository = SampleRepository(SAMPLES_FILEPATH)

    @classmethod
    def check_input(cls, anti_a, anti_b, anti_d, control, a1_cell, b_cell):
        """
        Metodi tarkistaa, ovatko annetut reaktiovoimakkuudet ohjelman hyväksymän muotoisia.
        Oikea muoto perustuu siihen, minkälaisia tuloksia menetelmä voi ylipäätään antaa.

        Args:
            anti_a (str): Anti-A-reaktiovoimakkuus
            anti_b (str): Anti-B-reaktiovoimakkuus
            anti_d (str): Anti-D-reaktiovoimakkuus
            control (str): Kontrollin reaktiovoimakkuus
            a1_cell (str): A1-solun reaktiovoimakkuus
            b_cell (str): B-solun reaktiovoimakkuus

        Returns:
            True: jos kaikki reaktiovoimakkuudet ovat hyväksyttäviä
            Merkkijono: listaus havaituista poikkeamista
        """

        valid_reactions = ["0", "1", "2", "3", "4", "DP"]
        problems = ""

        if anti_a not in valid_reactions:
            problems = problems + "- Anti-A \n"
        if anti_b not in valid_reactions:
            problems = problems + "- Anti-B \n"
        if anti_d not in valid_reactions:
            problems = problems + "- Anti-D \n"
        if control not in valid_reactions:
            problems = problems + "- Kontrolli \n"
        if a1_cell not in valid_reactions:
            problems = problems + "- A1-solu \n"
        if b_cell not in valid_reactions:
            problems = problems + "- B-solu \n"

        if problems == "":
            return True
        return problems

    @classmethod
    def convert_reactions(cls, reaction):
        """Metodi muuntaa merkkijonomuotoiset reaktiovoimakkuudet kokonaisluvuiksi tulkintaa varten

        Args:
            reaction (str): Reaktio merkkijonomuodossa

        Returns:
            reaction_strength (int): Reaktiovoimakkuus kokonaislukuna
        """

        if reaction == "DP":
            reaction_strength = 5
        else:
            reaction_strength = int(reaction)

        return reaction_strength

    def add_sample_data(
            self, sample_id_raw, comment, anti_a,
            anti_b, anti_d, control, a1_cell, b1_cell):
        """Lisää näyterepositoryyn uuden näyteolion

        Args:
            sample_id (str): Näytetunniste
            comment (str): Näytekommentti
            anti_a (str): Anti-A
            anti_b (str): Anti-B
            anti_d (str): Anti-D
            control (str): Kontrolli
            a1_cell (str): A1-solu
            b1_cell (str): B-solu
        Returns:
            False: jos lisättävän näytteen näytetunniste löytyy jo näytteiden listalta
            True: jos näytteen lisäys onnistui (eli näytetunniste oli uniikki)
        """

        anti_a_reaction = SampleHandler.convert_reactions(anti_a)
        anti_b_reaction = SampleHandler.convert_reactions(anti_b)
        anti_d_reaction = SampleHandler.convert_reactions(anti_d)
        control_reaction = SampleHandler.convert_reactions(control)
        a1cell_reaction = SampleHandler.convert_reactions(a1_cell)
        b1cell_reaction = SampleHandler.convert_reactions(b1_cell)

        sample_id = sample_id_raw.upper()
        timestamp = datetime.now()

        sample = Sample(sample_id, comment, anti_a_reaction, anti_b_reaction,
                        anti_d_reaction, control_reaction, a1cell_reaction,
                        b1cell_reaction, timestamp)
        return self.sample_repository.add_sample(sample)

    def get_all_samples(self, sample_index):
        """Hakee kaikki talletetut näytteet ja kutsuu ListingServiceä näytelistauksen luomiseksi

        Args:
            sample_index (int): Indeksi, josta lähtien näytteet halutaan palauttaa

        Returns:
            Merkkijono: Listaus talletetuista näytteistä tai tieto, että näytteitä ei ole talletettu
        """

        samples = self.sample_repository.read()
        if len(samples) == 0:
            return "Ei tallennettuja näytteitä."
        return ListingService.list_samples(samples, sample_index)

    def get_number_of_samples(self):
        """Palauttaa talletettujen näytteiden määrän

        Returns:
            Kokonaisluku: näytteiden määrä
        """

        samples = self.sample_repository.read()
        return len(samples)

    def get_sample_by_id(self, sample_id_raw):
        """Palauttaa näytteen tiedot näytenumeron perusteella

        Args:
            sample_id (str): Näytetunniste

        Returns:
            Merkkijono: Näytteen tiedot merkkijonomuodossa tai tieto, että näytettä ei löydy
        """
        sample_id = sample_id_raw.upper()
        sample = self.sample_repository.get_sample_by_id(sample_id)
        if sample is None:
            return "Näytetunnisteella ei löydy näytettä"
        return ListingService.get_one_sample(sample)

    def get_samples_by_several_ids(self, sample_ids, sample_index):
        """Palauttaa näytteiden tietoja näytetunnistelistauksen perusteella

        Args:
            sample_ids (list): Lista näytteiden tunnisteita, joita halutaan tarkastella
            sample_index (int): Indeksi, josta lähtien näytetietoja halutaan tarkastella

        Returns:
            Merkkijono: Näytteiden tiedot merkkijonomuodossa
        """

        samples = self.sample_repository.read()
        wanted_samples = []

        for sample in samples:
            if sample.sample_id in sample_ids:
                wanted_samples.append(sample)

        return ListingService.list_samples(wanted_samples, sample_index)

    def get_results(self, sample_id):
        """Hakee näytteen tulkinnan näytetunnisteen perusteella

        Args:
            sample_id (str): Näytetunniste

        Returns:
            Merkkijono: Näytteen tulosten tulkinta
        """

        sample = self.sample_repository.get_sample_by_id(sample_id)
        return sample.run_checks()
