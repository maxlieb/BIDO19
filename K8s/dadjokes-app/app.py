from flask import Flask, jsonify
import requests
import random
import os

app = Flask(__name__)

@app.route('/')
def dad_joke():
    limit = os.getenv('JOKE_LIMIT', '20')
    headers = {'User-agent': 'DadJokeBot 1.0'}
    url = f'https://www.reddit.com/r/dadjokes/top/.json?t=day&limit={limit}'
    try:
        response = requests.get(url, headers=headers, timeout=5)
        posts = response.json()['data']['children']
        joke = random.choice(posts)['data']
        return jsonify({
            'title': joke['title'],
            'body': joke['selftext']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
