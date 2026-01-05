from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🎉 ZÁKLADNÍ STRUKTURA OK!</h1>
    <p>Flask běží ✅</p>
    <p>1. Flask OK</p>
    <hr>
    <h3>Další kroky:</h3>
    <ol>
    <li>pip install --upgrade pip</li>
    <li>pip install oracledb  # novější než cx_Oracle</li>
    <li>Vytvořit SQL tabulky v Oracle</li>
    <li>DAO třídy</li>
    </ol>
    """

@app.route('/status')
def status():
    return "API funguje!"

if __name__ == '__main__':
    print("Spouštím na http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
