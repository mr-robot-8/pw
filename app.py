import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='templates')
model = pickle.load(open('model.pkl','rb'))
model1=pickle.load(open('model1.pkl','rb'))
@app.route('/')
def home():
    return render_template('./temp.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    proc=['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14']
    int_features=[]
    for n in proc:
        int_features.append(int(request.form.get(n)))
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    return render_template('./prediction1.html', prediction_text1='You are a procrastinator of {} level'.format(str(output)))

@app.route('/predict1',methods=['GET','POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    am=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23']
    int_features1=[]
    for n in am:
        print(n)
        print(int(request.form.get(n)))
        int_features1.append(int(request.form.get(n)))
    int_features1.append(int(1))   
    final_features = [np.array(int_features1)]
    prediction1 = model1.predict(final_features)

    output1 = prediction1[0]
    return render_template('./prediction2.html', prediction_text2='You are {} towards your academics'.format(str(output1)))
if __name__ == "__main__":
    app.run(debug=True) 
     
       


         
     
      

     

