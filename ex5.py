#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

string_normal = input("Digite seu texto aqui: ")
print("O texto é:",string_normal)

string_reversed = string_normal[::-1]
print("O texto inverso é:", string_reversed)