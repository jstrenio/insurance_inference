from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<result>')
def success(result):
   return 'predicted classification: %s' % result

@app.route('/input',methods = ['POST', 'GET'])
def input():
   if request.method == 'POST':
      inputs = []
      inputs.append(int(request.form['age']))
      inputs.append(int(request.form['years_driving']))

        # feed to model
      output = sum(inputs)

        # return model output
      return redirect(url_for('success',result = output))
   else:
      inputs = []
      inputs.append(request.args.get('nm'))

      return redirect(url_for('success',result = inputs))

if __name__ == '__main__':
   app.run(debug = True)