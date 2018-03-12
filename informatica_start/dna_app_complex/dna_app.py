from flask import Flask, render_template, request, session
from dna_modify import DNA
from db_context_manager import UseDatabase
from checker import check_logged_in


app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user':'jurre',
                          'password':'snoeksnoek#107',
                          'database':'dna_log_db',}


def log_request(req, res):
    with UseDatabase (app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (dna, ip, browser_string, dna_up, dna_rev, dna_comp, dna_rev_comp, rna, protein)
                values
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (  req.form['sequence'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res['dna_up'],
                                res['dna_rev'],
                                res['dna_comp'],
                                res['dna_rev_comp'],
                                res['rna'],
                                res['protein'],))


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
    results = {'dna_up': dna_up,
               'dna_rev': dna_rev,
               'dna_comp': dna_comp,
               'dna_rev_comp': dna_rev_comp,
               'rna': rna,
               'protein': protein}
    log_request(request, results)
    return render_template('results.html',
                           the_title='DNA manipulation results',
                           the_dna_up = dna_up,
                           the_dna_rev = dna_rev,
                           the_dna_comp = dna_comp,
                           the_dna_rev_comp = dna_rev_comp,
                           the_rna = rna,
                           the_protein = protein,)


@app.route('/viewlog')
@check_logged_in
def view_the_log():
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select id, ts, dna, ip, browser_string, dna_up, dna_rev, dna_comp, dna_rev_comp, rna, protein from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('id', 'ts', 'Form Data', 'Remote addr', 'browser', 'DNA', 'rev', 'comp', 'rev_comp', 'rna', 'protein')
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents,)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to manipulate DNA sequences on the web!')


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


app.secret_key = 'kljdsflkjdflks12312'


if __name__ == '__main__':
    app.run(debug=True)
