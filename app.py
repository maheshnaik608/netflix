from flask import Flask, render_template, request

app = Flask(__name__)

movies = [
    {"title": "Stranger Things", "genre": "Sci-Fi"},
    {"title": "Money Heist", "genre": "Thriller"},
    {"title": "Wednesday", "genre": "Mystery"},
    {"title": "The Witcher", "genre": "Fantasy"},
    {"title": "Dark", "genre": "Sci-Fi"},
    {"title": "Squid Game", "genre": "Thriller"}
]

@app.route("/")
def home():
    search = request.args.get("search", "").strip().lower()

    filtered_movies = [
        movie for movie in movies
        if search in movie["title"].lower()
        or search in movie["genre"].lower()
    ]

    return render_template(
        "index.html",
        movies=filtered_movies,
        search=search
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
