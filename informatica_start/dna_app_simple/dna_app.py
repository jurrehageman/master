from flask import Flask, render_template, request
from dna_modify import DNA

app = Flask(__name__)


@app.route('/output', methods=['POST'])
def output_page():
    dna_seq = request.form['sequence'].strip()
    dna_obj = DNA(dna_seq)
    if not dna_obj.is_valid_dna():
        return render_template('results_not_valid.html',
                               the_title='Invalid DNA sequence',
                               the_dna_up=dna_seq,)
    dna_up = dna_obj.seq
    dna_rev = dna_obj.reverse()
    dna_comp = dna_obj.complement()
    dna_rev_comp = dna_obj.reverse_complement()
    rna = dna_obj.transcribe()
    protein = dna_obj.translate()
    return render_template('results.html',
                           the_title='DNA manipulation results',
                           the_dna_up = dna_up,
                           the_dna_rev = dna_rev,
                           the_dna_comp = dna_comp,
                           the_dna_rev_comp = dna_rev_comp,
                           the_rna = rna,
                           the_protein = protein,)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to manipulate DNA sequences on the web!')



if __name__ == '__main__':
    app.run(debug=True)
