from bs4 import BeautifulSoup as bsp
import request_simpsons

def get_popular_characters(query_name):
    html = request_simpsons.get_simpsons_html()

    if not html:
        return []

    soup = bsp(html, "html.parser")

    characters = []

    character_cards = soup.select('a[data-umami-event="Popular Characters character"]')
    query = (query_name or "").strip().lower()

    for card in character_cards:
        name = card.get("data-umami-event-name")

        if not name:
            continue

        if query and query not in name.strip().lower():
            continue
        
        img_tag = card.find("img")
        image = img_tag.get("src") if img_tag else None
        
        age = None
        status = None

        badges = card.select("div.inline-flex")

        for badge in badges:
            text = badge.get_text(strip=True)

            if text.startswith("Age:"):
                age = text.replace("Age:", "").strip()

            elif text in ["Alive", "Deceased"]:
                status = text

        characters.append({
            "name": name,
            "age": age,
            "status": status,
            "image": image
        })

    return characters
