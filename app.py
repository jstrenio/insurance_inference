import torch
from insurance import NN
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<result>')
def success(result):
      result = round(float(result), 2)
      if result < 0.5:
         return 'predicted insurance classification: opt out ' + str(result)
      else:
         return 'predicted insurance classification: likely interested ' + str(result)

@app.route('/index',methods = ['GET', 'POST'])
def index():
   if request.method == 'POST':
      inputs = [1]
      inputs.append(int(request.form['gender']))
      inputs.append(int(request.form['age']))
      inputs.append(int(request.form['licensed']))
      inputs.append(int(request.form['region']))
      inputs.append(int(request.form['insured']))
      inputs.append(int(request.form['car_age']))
      inputs.append(int(request.form['damaged']))
      inputs.append(int(request.form['policy']))
      inputs.append(int(request.form['vintage']))

      model = NN()

      PATH = 'insurance_model.pt'
      model.load_state_dict(torch.load(PATH))

      output = model(torch.FloatTensor(inputs))
      output = output.item()

        # return model output
      return redirect(url_for('success',result = output))
   else:
      return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)