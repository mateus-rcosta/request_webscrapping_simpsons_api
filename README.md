# Request BeautifulSoup

## Objective

This project scrapes data from `thesimpsonsapi.com` and consumes its public API to display Simpsons character information in a Streamlit app.

## How to run

1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
uv sync
```

If you are not using `uv`, install the packages manually:

```bash
pip install streamlit beautifulsoup4 requests
```

3. Start the app:

```bash
streamlit run main.py
```

## Access

Open your browser and go to:

```text
http://localhost:8501
```

The app will also be available on your network IP if Streamlit exposes it.
