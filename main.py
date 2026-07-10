from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def d():
    return render_template('d.html')



if __name__=='__main__':
    app.run(debug=True)
