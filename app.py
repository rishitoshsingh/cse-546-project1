from flask import Flask, request
import pandas as pd

app = Flask(__name__)

def read_classification_result(file_name):
    df = pd.read_csv("s3://cse-546-project/face-results-1000.csv")
    return df[df['Image'] == file_name.split(".")[0]]['Results'].values[0]

@app.route('/', methods=['POST'])
def root_post():
    if 'inputFile' not in request.files:
        return "No file part in the request", 400

    input_file = request.files['inputFile']
    response = f"{input_file.filename}:{read_classification_result(input_file.filename)}"
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)