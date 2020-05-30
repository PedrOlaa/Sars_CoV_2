with open('genom.txt', 'r') as file:
    data = file.read().split()

def delete_integer():
    no_integers = [x for x in data if not (x.isdigit() 
        or x[0] == x[1:].isdigit())]
    return no_integers

def reverse_list(primer_list):
    new_list = []
    for primer in primer_list:
        new_list.append(primer[::-1])
    return new_list

def replace(primer_list):
    new_list = []
    for primer in primer_list:
        replace_primer = primer.replace('A', '%temp%').replace('T', 'A').replace('%temp%', "T").replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')
        new_list.append(replace_primer)
    return new_list

def check_primers(primer_list):
    for primer in primer_list:
        if primer in genom_string:
            print('genom zawiera primer ' + primer)
        else:
            print('nie zawiera')

Primers = ["TAATCAGACAAGGAACTGATTA", "CGAAGGTGTGACTTCCATG", "GCAAATTGTGCAATTTGCGG"]

genom_string = ''.join(delete_integer()).upper()
reverse_primers = reverse_list(Primers)
reverse_replace_primers = replace(reverse_primers)
check_primers(reverse_replace_primers)
