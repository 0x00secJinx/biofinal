#!/usr/bin/python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from random import randint
quotes = [
 "You don't like plant jokes? What stomata with you!",
 'Which biochemicals wash up on beaches? Nucleotides',
 'Where do hippos go to university? Hippocampus',
 'Biology is the only science in which multiplication is the same thing as division.',
 'It has recently been discovered that research causes cancer in rats.',
 'Why was the marine biologist so happy? He found his porpoise',
 'Bacteria is the only culture some people have',
 'What did one cell say to his sister cell that stepped on his toe? mitosis',
 'Two blood cells met and fell in love... but alas it was all in vein']
app = Flask(__name__)
Bootstrap(app)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    q = quotes[randint(0, len(quotes) - 1)]
    return render_template('index.html', quote=q)


@app.route('/experiment', methods=['GET', 'POST'])
def experiment():
    return render_template('experiment.html')


@app.route('/artifacts', methods=['GET', 'POST'])
def artifacts():
    return render_template('artifacts.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
 
@app.route('/remind', methods=['GET', 'POST'])
def remind():
 return render_template('remind.html')


if __name__ == '__main__':
    app.run()
