import subprocess
from flask import Flask, request, render_template

app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        k = request.form.get('k')
        pred_mode = request.form.get('pred_mode')
        command = "python predict_model.py -res_epoch `Best Validation Epoch` -onlyTest -restore -name `model name` -margin 10 -l2 0.00 -neg_sample 5 -gpu 0 -data_type yago -version large -k {} -pred_mode '{}'".format(k, pred_mode)
        result = subprocess.run(command, shell=True, capture_output=True)
        return result.stdout.decode('utf-8')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)