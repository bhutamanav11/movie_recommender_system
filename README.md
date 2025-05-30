Checkout the website : https://movierecommendersystem-dl2dwthc9xjjcg6qm2xlz9.streamlit.app/
Here's a clean and detailed `README.md` for your **Movie Recommender System** project, with all the essential sections like overview, features, installation steps, usage, and model file instructions:

---

## 📽️ Movie Recommender System

A personalized movie recommendation web app built using **Machine Learning**, **Streamlit**, and **Python**. It suggests similar movies based on a selected movie using **cosine similarity** and a pre-trained dataset.

---

### 🚀 Features

* 🎬 Get instant movie recommendations
* 🔍 Search from a list of 5000+ movies
* 📊 Backend logic using cosine similarity
* 🧠 Trained model stored as `similarity.pkl`
* 🌐 Simple web interface using **Streamlit**

---

### 🛠️ Tech Stack

* Python
* Jupyter Notebook
* Streamlit
* Scikit-learn
* Pandas / Numpy
* TMDB API (for posters)

---

## 🧠 How It Works

1. Movie titles are converted into numerical vectors using text-based feature engineering.
2. Cosine similarity is calculated between movies.
3. Top 5 most similar movies are returned as recommendations.

---

## 📦 Installation & Setup

> Make sure Python 3.8+ is installed.

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie_recommender_system.git
cd movie_recommender_system
```

### 🔹 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Add the `similarity.pkl` file

This file is **not included in the repo due to size limits.**
➡️ [Download similarity.pkl from GitHub Releases](https://github.com/yourusername/movie_recommender_system/releases)
Place it in the **main project directory**.

### 🔹 5. Run the App

```bash
streamlit run app.py
```
---

## 📁 Project Structure

```
movie_recommender_system/
│
├── app.py                # Streamlit frontend
├── similarity.pkl        # ML model file (externally downloaded)
├── movie_list.pkl        # List of movie data
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔐 API Key Note

This app uses TMDB API to fetch movie posters.
Make sure to replace the API key in `app.py` with your own key.
➡️ Get yours at: [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

---

## 🤝 Contributing

Pull requests and suggestions are welcome!
Feel free to fork the repo and submit improvements.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---
