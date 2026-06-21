import requests as rq

headers_scrapping = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:151.0) Gecko/20100101 Firefox/151.0'
}

def get_simpsons(id_character):
    info_raw = rq.get(f'https://thesimpsonsapi.com/api/characters/{id_character}')
    
    if info_raw.status_code == 200:
        return info_raw.json()
    return None

def get_simpsons_html():
    raw = rq.get('https://thesimpsonsapi.com/', headers=headers_scrapping)
    
    if raw.status_code == 200:
        return raw.text
    return None
    
