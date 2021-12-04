from flask import *
from calculations import *
import pandas
import openpyxl
import os
import zipfile
import glob


app = Flask(__name__)


@app.route('/f1', methods=['GET'])
def get_file():
    return send_file('./output/marksheets.zip', as_attachment=True)


@app.route('/f2', methods=['GET'])
def get_file2():
    return send_file('./output/concise_marksheet.csv', as_attachment=True)


@app.route('/')
def home():
    return render_template('MarksheetGenerator.html')


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    name = request.form['name']
    mst = request.files['mst']
    stu = request.files['stu']
    pos = request.form['pos']
    neg = request.form['neg']

    f_name_mst = 'input/' + mst.filename
    uploadmst = os.path.join(f_name_mst)
    mst.save(uploadmst)

    f_name_stu = 'input/' + stu.filename
    uploadstu = os.path.join(f_name_stu)
    stu.save(uploadstu)

    status = generate(name, pos, neg)
    if status == "no answer":
        return render_template('MarksheetGenerator.html', status=status)

    else:
        op()
        return render_template('Marksheet.html', status=status)


@app.route('/rst', methods=['GET', 'POST'])
def rst():
    reset()
    return render_template('MarksheetGenerator.html')


if __name__ == "__main__":
    app.run(debug=True)

