from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory('public/videos', filename)

@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(f'public/{path}'):
        return send_from_directory('public', path)
    # Fallback to index.html for any unmapped routes
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
