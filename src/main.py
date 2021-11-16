import cowsay
from entities import sample

cowsay.cow("Tervetuloa veriryhmäapuriin!")

id = input("Anna näytenumero: ")

sample = sample.Sample(id)

print("Anna reaktiovoimakkuudet:")
anti_a = int(input("anti-A: "))
anti_b = int(input("anti-B: "))
anti_d = int(input("anti-D: "))
#maybe check for dp's here?
sample.input_cell_reactions(anti_a, anti_b, anti_d)
control = int(input("control: "))
sample.input_control_reaction(control)
a = int(input("A1-solu: "))
b = int(input("B-solu: "))
sample.input_plasma_reactions(a, b)

print(sample.id)
sample.print()
sample.list_all_exceptions()

