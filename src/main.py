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
        sample.id = id

        print("Anna reaktiovoimakkuudet numeroina 0 - 4:")
        anti_a = int(input("anti-A: "))
        anti_b = int(input("anti-B: "))
        anti_d = int(input("anti-D: "))
        control = int(input("control: "))
        a = int(input("A1-solu: "))
        b = int(input("B-solu: "))
        sample.input_reactions(anti_a, anti_b, anti_d, control, a, b)

        sample.run_checks()


