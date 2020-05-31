class primer:  
    def __init__(self, primer_string, reverse):  
        self.primer_string = primer_string 
        self.reverse = reverse 
        
    def reverse_string(self, arg):
        return self.primer_string[::-1]
    def replace_string(self, arg):
        return self.primer_string.replace('A', '%temp%').replace('T', 'A').replace('%temp%', "T").replace('C', '%temp%').replace('G', 'C').replace('%temp%', 'G')
    def check_primer(self, checking_string):
            if(self.reverse == True):
                self.primer_string = self.reverse_string(self.primer_string) 
                self.primer_string = self.replace_string(self.primer_string)
            if self.primer_string in checking_string:
                print('genom zawiera primer ' + self.primer_string)
            else:
                print('nie zawiera')


class genom_file:
    def __init__(self, file, genom_string):
        self.file = file
        self.genom_string = genom_string

    def open_file(self, method):
        with open(self.file, method) as data:
            self.genom_string = data.read().split()

    def delete_integer(self, data):
        no_integers = [x for x in data if not (x.isdigit() 
        or x[0] == x[1:].isdigit())]
        return no_integers

    def make_file_one_string(self):
        self.genom_string = ''.join(self.delete_integer(self.genom_string)).upper()
    
    def init_new_string(self, method):
        self.open_file(method)
        self.make_file_one_string()

new_file = genom_file('genom.txt', 'test')
new_file.init_new_string('r')
searching_string = new_file.genom_string


first_primer = primer('TAATCAGACAAGGAACTGATTA', False)
first_primer.check_primer(searching_string)

second_primer = primer('CGAAGGTGTGACTTCCATG', True)
second_primer.check_primer(searching_string)

third_primer = primer('GCAAATTGTGCAATTTGCGG', True)
third_primer.check_primer(searching_string)