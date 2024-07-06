
from flask import Flask, render_template, request, redirect, url_for , send_file , abort
from GSTR2A import reco_itr_2a
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = { 'csv', 'xlsx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'], )
def page():
    return "IT WORKS!"
    


@app.route('/upload/files', methods=['GET', 'POST'], )
def index():
    


    if request.method == 'POST':

        SHEET_NAME = request.form['sheetname']
        print('SHEET_NAME',SHEET_NAME)
        # Check if the post request has the file part
        if 'file1' not in request.files or 'file2' not in request.files:
            return redirect(request.url)
        

        file1 = request.files['file1']
        file2 = request.files['file2']

        if os.path.exists('GSTR_ITR_RECO.xlsx'):
            print('does exist')
            os.remove('GSTR_ITR_RECO.xlsx')
            print('GSTR_ITR_RECO.xlsx removed successfully!')


        if os.path.exists(file1.filename):
            print('does exist')
            os.remove(file1.filename)
            print(f'{file1.filename} removed successfully!')

        if os.path.exists(file2.filename):
            print('does exist')
            os.remove(file2.filename)
            print(f'{file2.filename} removed successfully!')

        
        

        

        # If user does not select file, browser also
        # submit an empty part without filename
        if file1.filename == '' or file2.filename == '':
            return redirect(request.url)
        
        file1.save(file1.filename)
        file2.save(file2.filename)
        print(file1.filename)

        
    

        fun = reco_itr_2a(file1 , file2 ,SHEET_NAME)
        print(fun)
  


        
    # filenames = os.listdir(app.config['UPLOAD_FOLDER'])

    return render_template('index.html')

@app.route('/download')
def download():
    path = 'GSTR_ITR_RECO.xlsx'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


