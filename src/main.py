import cowsay
from entities.sample import Sample

cowsay.cow("Tervetuloa veriryhmäapuriin!")
print(" ")
initial_id = 0
sample = Sample(initial_id)
while True:
    print(" ")
    id = input("Anna näytenumero, 'lopeta' lopettaa: ")
    if id == "lopeta":
        break
    else:
        print(" ")
        sample.id = id
        print("Anna reaktiovoimakkuudet numeroina 0 - 4 tai kaksoispopulaatio DP:")
        anti_a = input("anti-A: ")
        anti_a_reaction = sample.validate_reaction(anti_a)
        anti_b = input("anti-B: ")
        anti_b_reaction = sample.validate_reaction(anti_b)
        anti_d = input("anti-D: ")
        anti_d_reaction = sample.validate_reaction(anti_d)
        control = input("control: ")
        control_reaction = sample.validate_reaction(control)
        a = input("A1-solu: ")
        a_reaction = sample.validate_reaction(a)
        b = input("B-solu: ")
        b_reaction = sample.validate_reaction(b)
        sample.input_reactions(anti_a_reaction, anti_b_reaction, anti_d_reaction, control_reaction, a_reaction, b_reaction)
        print(" ")
        print(sample.run_checks())


