import streamlit as st
import request_simpsons as rs
import scrapper_simpson as ss

def main():
    st.title("App: Simpson Query")
    search_query = st.text_input("Enter Simpsons id: ")
    
    if search_query:
        with st.spinner("Fetching data..."):
            info_character = rs.get_simpsons(search_query)

            if info_character:
                character_name = info_character["name"].title()
                character_img_path = info_character["portrait_path"]
                info_character
                
                col1, col2 = st.columns([1, 1.5], gap="small")
                with col1:
                    st.image(f"https://cdn.thesimpsonsapi.com/1280{character_img_path}")
                    
                with col2:
                    st.subheader(f"{character_name}")
                    st.write(f"Description: {info_character['description']}")
            else:
                st.error("Character not found.")
    
    st.divider()

    st.subheader("Popular Characters")

    popular_characters = ss.get_popular_characters()

    for character in popular_characters:
        with st.container():
            st.markdown(f"### {character['name']}")
            st.write(f"Age: {character['age']}")
            st.write(f"Status: {character['status']}")
            st.divider()



if __name__ == "__main__":
    main()
