from flask import Flask, render_template
import Data
app = Flask(__name__)

@app.route('/query1')
def query1():
    cursor = Data.Query1();
    return render_template('query1.html',cursor=cursor)
@app.route('/query2')
def query2():
    cursor = Data.Query2();
    return render_template('query2.html',cursor=cursor)

@app.route('/query3/<genres>')
def query3(genres):
    cursor = Data.Query3(genres);
    return render_template('query3.html',cursor=cursor,genres = genres)
@app.route('/query4')
def query4():
    cursor = Data.Query4();
    return render_template('query4.html',cursor=cursor)
@app.route('/query5')
def query5():
    cursor = Data.Query5();
    return render_template('query5.html',cursor=cursor)
@app.route('/query6')
def query6():
    cursor = Data.Query6();
    return render_template('query6.html',cursor=cursor)
@app.route('/')
def home():
    return render_template('home.html',title="Implement Database")

if __name__ == '__main__':

  app.run(port=4500)