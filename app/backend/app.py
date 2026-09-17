from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api')
def api():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3063,
            user='root',
            password='root',
            database='mydb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from Database!' AS message")
        result = cursor.fetchone()
        conn.close()
        return jsonify({"message": result[0]})
    except Exception as e:
        return jsonify({"message": f"DB error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
