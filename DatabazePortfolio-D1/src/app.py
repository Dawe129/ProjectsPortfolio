from flask import Flask
import oracledb
import configparser
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from routes.api_routes import api_bp

app = Flask(__name__)

# Registrace blueprintu
app.register_blueprint(api_bp)

@app.route('/')
def home():
    try:
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'database.ini')
        config.read(config_path)
        
        dsn = oracledb.makedsn(
            config['DEFAULT']['host'],
            int(config['DEFAULT']['port']),
            service_name=config['DEFAULT']['service_name']
        )
        
        return f"""
        <h1>🎉 PROJEKT FUNGUJE!</h1>
        <p>Flask: ✅</p>
        <p>oracledb: ✅</p>
        <p>Config načteno: {config['DEFAULT']['host']}</p>
        <p>DSN vytvořen: {dsn}</p>
        <p><a href="/books">/books</a></p>
        """
    except Exception as e:
        return f"Chyba: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
