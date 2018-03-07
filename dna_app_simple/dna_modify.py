class DNA:
    """This class manipulates DNA sequences"""
    #class variables
    _comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


    def __init__(self, seq):
        """The constructor"""
        self.seq = seq.upper()


    def is_valid_dna(self):
        valids = "ATCG"
        for i in self.seq:
            if not i in valids:
                return False
        return True



    def reverse(self):
        """returns reverse seq"""
        return self.seq[::-1]


    def complement(self):
        """Returns the complementary sequence"""
        _comp_seq = []
        for base in self.seq:
            _comp_seq.append(DNA._comp[base])
        return "".join(_comp_seq)


    def reverse_complement(self):
        """Returns the reverse complementary sequence"""
        _comp_seq = []
        for base in self.seq:
            _comp_seq.append(DNA._comp[base])
        return "".join(_comp_seq)[::-1]


    def transcribe(self):
        """Transcribes to RNA"""
        return self.seq.replace('T', 'U')


    def translate(self):
        """Translates to protein"""
        _codon_table = DNA._read_codon_table(self)
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


    def _read_codon_table(self):
        """Reads the codon table"""
        _codon_table = {}
        for _line in open('helper/codon_table.txt'):
            _line = _line.strip()
            _line = _line.split()
            _aa = _line[1]
            _codons = _line[2:]
            for _codon in _codons:
                _codon_table.update({_codon:_aa})
        return _codon_table



def main():
    """Testing module"""
    seq_obj = DNA("atcatcatccccccccccccctaccc")
    #print(dir(seq_obj))
    valid_dna = seq_obj.is_valid_dna()
    print(valid_dna)
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