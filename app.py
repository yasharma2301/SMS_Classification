from flask import Flask, render_template, request
import pandas as pd
import pickle
import sklearn
import mimetypes
import regex as re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/javascript', '.js')


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

smsModel = pickle.load(open('sms_classification.pkl','rb'))
cv = pickle.load(open('countVectorizer.pkl','rb'))

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == 'POST':
        message = request.form['sms_text']
        
        ps = PorterStemmer()

        try:
            nltk.download('stopwords')
        except:
            print('error downloading stopwords')

        review = re.sub('[^a-zA-Z]',' ',message)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)

        X = cv.transform([review])
        prediction = smsModel.predict(X)
        
        return "Bwawhhh! It's a spam message!⚠️" if prediction[0]==1 else "Looks like this message is ham🤙"
        
if __name__ == "__main__":
    debug = True
    app.run()