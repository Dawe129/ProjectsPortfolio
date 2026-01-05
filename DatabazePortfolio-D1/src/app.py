from flask import Flask
import cx_Oracle
import configparser
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # Test config
        config = configparser.ConfigParser()
        config.read('config/database.ini')
        
        # Test Oracle (bez připojení)
        dsn = cx_Oracle.makedsn(
            config['DEFAULT']['host'],
            config['DEFAULT']['port'],
            service_name=config['DEFAULT']['service_name']
        )
        
        return f"""
        <h1>🎉 PROJEKT FUNGUJE!</h1>
        <p>Flask: ✅</p>
        <p>cx_Oracle: ✅</p>
        <p>Config načteno: {config['DEFAULT']['host']}</p>
        <p>DSN vytvořen: {dsn}</p>
        <p><a href="/books">/books (brzy)</a></p>
        """
    except Exception as e:
        return f"Chyba: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
