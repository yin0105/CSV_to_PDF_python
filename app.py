#!/usr/bin/env python
from flask import Flask, render_template, request, flash, redirect, url_for, g, session
from flask_bootstrap import Bootstrap
from models import MainForm
import csv
import pdfkit 
from datetime import datetime

class Config(object):
    SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def admin():
    form = MainForm(request.form)
    if request.method == 'POST':  
        f = request.files['csv']  
        fstring = f.read()[3:]
        new_string = fstring.decode(encoding="utf-8")

        for row in csv.DictReader(new_string.splitlines(), delimiter=';'): #, skipinitialspace=True
            with open('templates/sample.html', 'r') as in_file:
                with open('templates/tmp.html', 'w', newline='') as out_file:
                    for ii in in_file:
                        ss = ii.strip()
                        if ss[:2] == "__":
                            ss = ss[2:-2]
                            if ss in row: ss = row[ss]
                        out_file.write(ss + "\n")
                    now = datetime.now()
                out_file.close()
                current_time = now.strftime("%Y_%m_%d_%H_%M_%S")
                pdfkit.from_file('templates/tmp.html', 'PDF/' + current_time + '.pdf') 
            in_file.close()
    return render_template('main.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# import pdfkit 
# pdfkit.from_url('https://zuerich.usgang.ch/','shaurya.pdf') 