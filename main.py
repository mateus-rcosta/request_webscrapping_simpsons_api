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
    search_query_name= st.text_input("Enter a name: ")
    popular_characters = ss.get_popular_characters(search_query_name)

    if popular_characters:
        for character in popular_characters:
            col1, col2 = st.columns([1, 2])

            with col1:
                if character["image"]:
                    st.image(character["image"], use_container_width=True)

            with col2:
                st.subheader(character["name"])
                st.write(f"Age: {character['age']}")
                st.write(f"Status: {character['status']}")
    else:
        st.info("No popular characters matched that name.")



if __name__ == "__main__":
    main()
