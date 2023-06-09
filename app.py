from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def pred():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)

