class DNA:
    _comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    def __init__(self, seq):
        self.seq = seq.upper()


    def transcribe(self):
        return self.seq.replace('T', 'U')


    def reverse(self):
        """returns reverse seq"""
        return self.seq[::-1]


    def complement(self):
        _comp_seq = ''.join([DNA._comp[i] for i in list(self.seq)])
        return _comp_seq


    def reverse_complement(self):
        _rev_comp_seq = ''.join([DNA._comp[i] for i in list(self.seq)])[::-1]
        return _rev_comp_seq


    def is_valid_dna(self):
        valids = "ATCG"
        for i in self.seq:
            if not i in valids:
                return False
        return True


def main():
    seq_obj = DNA("tta")
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

if __name__ == "__main__":
    main()