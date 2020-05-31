#Funkcja usuwa liczby z pliku genom.txt
def delete_integer():
    no_integers = [x for x in data if not (x.isdigit() 
        or x[0] == x[1:].isdigit())]
    return no_integers

#Funkcja obraca primer
def reverse_list(primer):
    return primer.string[::-1]

#Funkcja zamienia zasady na komplementarne
def replace(primer):
    return primer.string.replace('A', '%temp%').replace('T', 'A').replace('%temp%', "T").replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')

#Jeżeli jest to konieczne - funkcja odwraca i zamienia primer, jeżeli reverse == True
def check_primers(primer_list):
    for primer in primer_list:
        if(primer.reverse == True):
            primer.string = reverse_list(primer)
            primer.string = replace(primer)
        if primer.string in genom_string:
            print('genom zawiera primer ' + primer.string)
        else:
            print('nie zawiera')

            
with open('genom.txt', 'r') as file:
    data = file.read().split()

#Tworzy z pliku genom.txt string
genom_string = ''.join(delete_integer()).upper()

#Klasa - w taki sposób tworzy się 1 primer. Na dole - tworzą sie nowe primery i dodawane są do listy: primer_list
class primer:  
    def __init__(self, string, reverse):  
        self.string = string 
        self.reverse = reverse 

primer_list = []

primer_list.append(primer('TAATCAGACAAGGAACTGATTA', False))
primer_list.append(primer('CGAAGGTGTGACTTCCATG', True))
primer_list.append(primer('GCAAATTGTGCAATTTGCGG', True))

#Wywołanie funkcji
check_primers(primer_list)