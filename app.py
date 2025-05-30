import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

# ----------------- CSS -----------------
st.markdown("""
    <style>
        body {
            background-color: #141414;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #E50914;
            text-align: center;
            margin-bottom: 20px;
        }
        .movie-card {
            background-color: #1c1c1c;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        .movie-card:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(229,9,20,0.6);
        }
        .movie-title {
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
            color: white;
        }
        .movie-overview {
            font-size: 14px;
            color: #ccc;
            margin-top: 5px;
            height: 60px;
            overflow: hidden;
        }
        .rating {
            font-size: 16px;
            color: #f5c518;
            margin-top: 8px;
        }
        .stButton>button {
            background-color: #E50914;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- TMDB API -----------------
API_KEY = 'a3b0d89edc73f3aad941d61f976726c5'


def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return {
        "poster": "https://image.tmdb.org/t/p/w500" + data.get("poster_path", ""),
        "overview": data.get("overview", "No description available."),
        "rating": data.get("vote_average", "N/A")
    }


# ----------------- Recommender Logic -----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    results = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        results.append({
            "title": movies.iloc[i[0]].title,
            "poster": details["poster"],
            "overview": details["overview"],
            "rating": details["rating"]
        })
    return results


# ----------------- Load Pickles -----------------
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ----------------- UI -----------------
st.markdown('<div class="title">🎬 Movie Recommender</div>', unsafe_allow_html=True)

selected_movie_name = st.selectbox("Select from available movies:", movies['title'].values)

if st.button("Get Recommendations"):
    results = recommend(selected_movie_name)
    st.markdown("---")
    cols = st.columns(5)

    for i, movie in enumerate(results):
        with cols[i]:
            st.markdown(f"""
                <div class="movie-card">
                    <img src="{movie['poster']}" width="100%" style="border-radius:10px;" />
                    <div class="movie-title">{movie['title']}</div>
                    <div class="rating">⭐ {movie['rating']}</div>
                    <div class="movie-overview">{movie['overview']}</div>
                </div>
            """, unsafe_allow_html=True)
