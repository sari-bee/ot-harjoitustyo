
class ListingService:

    """Luokka muodostaa listauksia muiden luokkien tarpeisiin.
    """

    @classmethod
    def revert_reactions(cls, reaction_strength):
        """Metodi muuntaa tulkinnassa käytetyt muuttujat kokonaisluvusta merkkijonoksi

        Args:
            reaction_strength (int): reaktiovoimakkuus kokonaislukutyyppisenä

        Returns:
            Merkkijono: reaktiovoimakkuus
        """

        if reaction_strength == 5:
            reaction = "DP"
        else:
            reaction = str(reaction_strength)

        return reaction

    @classmethod
    def list_samples(cls, samples, sample_index):
        """Tulostetaan listaus kaikista hakuehtoihin sopivista näytteistä

        Args:
            samples (list): Lista näyteolioita, jotka sopivat tiettyihin hakuehtoihin
            sample_index (int): Indeksi, josta näytteiden listaus aloitetaan

        Returns:
            Merkkijono: Näytteiden tiedot merkkijonomuodossa
        """

        listing = ""
        samples.sort(key=lambda sample: (sample.timestamp), reverse=True)
        begin = sample_index
        end = sample_index+5

        for sample in samples[begin:end]:
            timeparts = sample.timestamp.split(".")
            time = timeparts[0]
            anti_a = ListingService.revert_reactions(sample.anti_a)
            anti_b = ListingService.revert_reactions(sample.anti_b)
            anti_d = ListingService.revert_reactions(sample.anti_d)
            control = ListingService.revert_reactions(sample.control)
            a1_cell = ListingService.revert_reactions(sample.a1_cell)
            b_cell = ListingService.revert_reactions(sample.b_cell)
            listing = listing + \
                f"Näyte {sample.sample_id} (tallennettu {time}): Anti-A {anti_a}, Anti-B {anti_b}, Anti-D {anti_d}, Kontrolli {control}, A1-solu {a1_cell}, B-solu {b_cell}.\nTulkinta: {sample.run_checks()}\nKommentti: {sample.comment} \n \n"

        return listing

    @classmethod
    def get_one_sample(cls, sample):
        """Tulostetaan listaus yksittäisestä näytteestä

        Args:
            sample (Sample): Yksittäinen näyteolio

        Returns:
            Merkkijono: Näytteen tiedot merkkijonomuodossa
        """

        anti_a = ListingService.revert_reactions(sample.anti_a)
        anti_b = ListingService.revert_reactions(sample.anti_b)
        anti_d = ListingService.revert_reactions(sample.anti_d)
        control = ListingService.revert_reactions(sample.control)
        a1_cell = ListingService.revert_reactions(sample.a1_cell)
        b_cell = ListingService.revert_reactions(sample.b_cell)

        timeparts = sample.timestamp.split(".")
        time = timeparts[0]

        sample_data = f"Näyte {sample.sample_id} (tallennettu {time}): Anti-A {anti_a}, Anti-B {anti_b}, Anti-D {anti_d}, Kontrolli {control}, A1-solu {a1_cell}, B-solu {b_cell}.\nTulkinta: {sample.run_checks()}\nKommentti: {sample.comment}"
        return sample_data
