from custom_error import NotDnaBaseError, validate


class DNA:
    """This class manipulates DNA sequences"""
    #class variables
    _comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


    def __init__(self, seq):
        """The constructor"""
        self.seq = seq.upper()


    def is_valid_dna(self):
        try:
            validate(self.seq)
        except NotDnaBaseError as e:
            print("{}. Sequence {} contains an invalid base".format(type(e).__name__, e))



    def reverse(self):
        """returns reverse seq"""
        return self.seq[::-1]


    def complement(self):
        """Returns the complementary sequence"""
        _comp_seq = []
        for base in self.seq:
            try:
                _comp_seq.append(DNA._comp[base])
            except KeyError:
                print("Base {} not found".format(base))
        return "".join(_comp_seq)


    def reverse_complement(self):
        """Returns the reverse complementary sequence"""
        _comp_seq = []
        for base in self.seq:
            try:
                _comp_seq.append(DNA._comp[base])
            except KeyError:
                print("Base {} not found".format(base))
        return "".join(_comp_seq)[::-1]


    def transcribe(self):
        """Transcribes to RNA"""
        return self.seq.replace('T', 'U')


    def parse_codon_table(self):
        """"reads codon table"""
        codon_table = {}
        try:
            with open('codons.txt') as f:
                for line in f:
                    line = line.strip().split()
                    for codon in line[2:]:
                        codon_table[codon] = line[1]
                return codon_table
        except FileNotFoundError:
            print("no codon file found")


    def translate(self):
        """Translates to protein"""
        _codon_table = self.parse_codon_table()
        _stop_codons = "TAA TGA TAG".split()
        _protein_seq = []
        _start = self.seq.find("ATG")
        if _start == -1:
            return "No start codon found"
        _end = _start + 3
        _num_of_codons = (len(self.seq) - _start) // 3
        for _codon_num in range(_num_of_codons):
            _codon = self.seq[_start:_end]
            if not _codon in _stop_codons:
                _protein_seq.append(_codon_table[_codon])
                _start += 3
                _end += 3
            else:
                return "".join(_protein_seq)
        return "".join(_protein_seq) + ", no stop codon found"



def main():
    """Testing module"""
    seq_obj = DNA("atcatgatcccccccccctagccctacqc")
    #print(dir(seq_obj))
    valid_dna = seq_obj.is_valid_dna()
    #valid_dna = True
    if valid_dna:
        dna_up = seq_obj.seq
        print(dna_up)
        dna_rev = seq_obj.reverse()
        print(dna_rev)
        dna_comp = seq_obj.complement()
        print(dna_comp)
        dna_rev_comp = seq_obj.reverse_complement()
        print(dna_rev_comp)
        protein = seq_obj.translate()
        print(protein)


if __name__ == "__main__":
    main()