# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on metadata and feature similarity. The application uses machine learning techniques and cosine similarity to identify movies with comparable characteristics and presents recommendations through an interactive Streamlit interface.

## Live Demo

https://movierecommendersystem-dl2dwthc9xjjcg6qm2xlz9.streamlit.app/

## Overview

Finding relevant movies from large catalogs can be challenging. This project addresses that problem by building a recommendation engine that analyzes movie attributes and recommends similar titles based on learned feature representations.

The system processes a dataset containing over 5,000 movies and generates recommendations using vectorized movie features and cosine similarity.

## Features

* Content-based movie recommendation engine
* Recommendations generated in real time
* Database of 5,000+ movies
* Movie poster integration using TMDB API
* Interactive web application built with Streamlit
* Pre-computed similarity matrix for fast inference

## Technology Stack

| Category                | Technologies     |
| ----------------------- | ---------------- |
| Programming Language    | Python           |
| Machine Learning        | Scikit-learn     |
| Data Processing         | Pandas, NumPy    |
| Frontend                | Streamlit        |
| Development Environment | Jupyter Notebook |
| External API            | TMDB API         |

## Recommendation Pipeline

1. Movie metadata is collected and cleaned.
2. Relevant textual features are combined into a single representation.
3. Feature vectors are generated using text vectorization techniques.
4. Cosine similarity is computed between all movie pairs.
5. Similarity scores are stored for efficient retrieval.
6. The top matching movies are displayed to the user.

## Project Structure

```text
movie_recommender_system/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/bhutamanav11/movie_recommender_system.git
cd movie_recommender_system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Dataset

The recommendation engine is trained using a movie dataset containing metadata such as genres, cast, crew, keywords, and movie descriptions. These attributes are transformed into feature vectors used for similarity calculations.

## API Configuration

The application uses the TMDB API to retrieve movie posters and related metadata.

Create an account and generate an API key from:

https://www.themoviedb.org/settings/api

Update the API key in the application configuration before running the project.

## Future Improvements

* Hybrid recommendation system using collaborative filtering
* Personalized recommendations based on user history
* User authentication and watchlists
* Deployment using Docker and cloud infrastructure
* Deep learning based recommendation models

## License

This project is licensed under the MIT License.
