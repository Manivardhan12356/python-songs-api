from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_songs():
    # Replace 'YOUR_URL_HERE' with the actual URL
    api_url = 'https://songs-api-qdtk.onrender.com/'  

    # Fetch data from the API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
