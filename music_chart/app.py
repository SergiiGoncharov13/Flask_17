from flask import Flask, render_template, request, jsonify


songs = [
    "Imagine Dragons - Believer",
    "Ed Sheeran - Shape of You",
    "Beyoncé - Halo",
    "The Weeknd - Blinding Lights",
    "Coldplay - Viva La Vida",
    "Adele - Rolling in the Deep",
    "Maroon 5 - Sugar",
    "OneRepublic - Counting Stars",
    "Taylor Swift - Shake It Off",
    "Post Malone - Circles",
    "Shawn Mendes - Treat You Better",
    "Justin Bieber - Love Yourself",
    "Dua Lipa - Don't Start Now",
    "Lady Gaga - Shallow",
    "Billie Eilish - Bad Guy",
    "Bruno Mars - Uptown Funk",
    "Harry Styles - Watermelon Sugar",
    "Chainsmokers - Closer",
    "Linkin Park - Numb",
    "Katy Perry - Roar",
    "Sam Smith - Stay With Me"
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/api/search', methods=['POST'])
def api_search():
    data = request.get_json()
    query = data.get('query', '').lower().strip()

    for i, song in enumerate(songs):
        if query in song.lower():
            return jsonify({
                'found': True,
                'song': song,
                'index': i + 1
            })
    return jsonify({
        'found': False
    })



if __name__ == '__main__':
    app.run(debug=True)
