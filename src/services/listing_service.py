from entities.sample import Sample


class ListingService:

    @classmethod
    def revert_reactions(cls, reaction_strength: int):
        if reaction_strength == 5:
            reaction = "DP"
        else:
            reaction = str(reaction_strength)
        return reaction

    @classmethod
    def list_samples(cls, samples: list, sample_index: int):
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
                f"Näyte {sample.sample_id} (tallennettu {time}): Anti-A {anti_a}, Anti-B {anti_b}, Anti-D {anti_d}, Kontrolli {control}, A1-solu {a1_cell}, B-solu {b_cell}. \n Tulkinta: {sample.run_checks()} \n  Kommentti: {sample.comment} \n \n"
        return listing

    @classmethod
    def get_one_sample(cls, sample: Sample):
        timeparts = sample.timestamp.split(".")
        time = timeparts[0]
        anti_a = ListingService.revert_reactions(sample.anti_a)
        anti_b = ListingService.revert_reactions(sample.anti_b)
        anti_d = ListingService.revert_reactions(sample.anti_d)
        control = ListingService.revert_reactions(sample.control)
        a1_cell = ListingService.revert_reactions(sample.a1_cell)
        b_cell = ListingService.revert_reactions(sample.b_cell)
        sample_data = f"Näyte {sample.sample_id} (tallennettu {time}): Anti-A {anti_a}, Anti-B {anti_b}, Anti-D {anti_d}, Kontrolli {control}, A1-solu {a1_cell}, B-solu {b_cell}. \n Tulkinta: {sample.run_checks()}"
        return sample_data
