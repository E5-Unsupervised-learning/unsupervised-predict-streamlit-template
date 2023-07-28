"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Recommender System","Top Rated Movies","Meet the team","Our Services"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    from PIL import Image


    def show_welcome_page():
    #"Show the welcome page"
    # Displaying the image above the title
        header_image = Image.open("resources/imgs/Phoenix.png")
        st.image(header_image, use_column_width=True)    

    if page_selection == "Home":
        show_welcome_page()
        # Welcome message
        st.title("Welcome!")
        st.write("Please select an option by the navigation tab to get started.")

         # Data Exploration Page
    if page_selection == "Top Rated Movies":
        
        #st.sidebar.video("https://www.youtube.com/watch?v=555oiY9RWM4")
        #st.sidebar.video("https://www.youtube.com/watch?v=WTAg7aolyCY")
        #st.sidebar.video("https://www.youtube.com/watch?v=naQr0uTrH_s")

        #st.title("TOP RATED MOVIES")
        st.sidebar.image("resources/imgs/topr.png", use_column_width=True)
        
        st.subheader(" Fat Pizza vs Housos (2014)")        
        st.video("https://www.youtube.com/watch?v=udTm5CejuCo&pp=ygUcZmF0IHBpenphIHZzIGhvdXNvcyB0cmFpbGVyIA%3D%3D")

        st.subheader("The Fearless Young Boxer (1979)")        
        st.video("https://www.youtube.com/watch?v=B6asvY_trEE&pp=ygUoVGhlIEZlYXJsZXNzIFlvdW5nIEJveGVyICgxOTc5KSB0cmFpbGVyIA%3D%3D")

        st.subheader("A Moving Romance (2017)")        
        st.video("https://www.youtube.com/watch?v=q_aFTDRG6cc&pp=ygUgQSBNb3ZpbmcgUm9tYW5jZSAoMjAxNykgdHJhaWxlciA%3D")

        st.subheader(" Shaka Zulu: The Citadel (2001)")       
        st.video("https://www.youtube.com/watch?v=lSUJ3rJ_RA8&pp=ygUnU2hha2EgWnVsdTogVGhlIENpdGFkZWwgKDIwMDEpIHRyYWlsZXIg")

        st.subheader("Get Crazy (1983)")        
        st.video("https://www.youtube.com/watch?v=T681L5QKMGY&pp=ygUZR2V0IENyYXp5ICgxOTgzKSB0cmFpbGVyIA%3D%3D")

        st.subheader("A Royal Winter (2017)")        
        st.video("https://www.youtube.com/watch?v=2SShzDTOogM&pp=ygUeQSBSb3lhbCBXaW50ZXIgKDIwMTcpIHRyYWlsZXIg")

        st.subheader("Dawning (2009)")        
        st.video("https://www.youtube.com/watch?v=WUR-Ix8q72Q&pp=ygUXRGF3bmluZyAoMjAwOSkgdHJhaWxlciA%3D")

        st.subheader("Macondo (2014) ")       
        st.video("https://www.youtube.com/watch?v=cGI7L18pEks&pp=ygUWTWFjb25kbyAoMjAxNCl0cmFpbGVyIA%3D%3D")

        st.subheader("Windstorm 2 (2015) ")       
        st.video("https://www.youtube.com/watch?v=5BLVqhUtLCM&pp=ygUbV2luZHN0b3JtIDIgKDIwMTUpIHRyYWlsZXIg")

        st.subheader("My Christmas Love (2016)")        
        st.video("https://www.youtube.com/watch?v=sJ56p5xho2w&pp=ygUhTXkgQ2hyaXN0bWFzIExvdmUgKDIwMTYpIHRyYWlsZXIg")

        
        st.subheader("Distribution of movie ratings")
        st.image("resources/imgs/distribution.png")

        st.subheader("Average movie ratings")
        st.image("resources/imgs/average.png")
        
         # About Us Page
    if page_selection == "Meet the team":

        st.image("resources/imgs/meet.png")

        # table of contents on the sidebar


        st.subheader("Project Lead: Ayushmaan Maharaj")
        st.image("resources/imgs/ayush.jpg",width=200)

        st.subheader("Technical Lead: Karabo Lamola")
        st.image("resources/imgs/karabo.jpg",width=200)

        st.subheader("Admin Lead: Ezemba Osinachi")
        st.image("resources/imgs/ezemba.png",width=200)

        
         # Create a contact us widget
        st.header("Contact Us")
        st.markdown("If you wish to contact us please enter your details below and we will get back to as soon as possible")
        st.text_input("Full Name")
        st.text_input("Contact Number", "Optional")
        st.text_input("Email Address")
        st.text_area("Enter a message")

        def func():
            st.write("Submitted, Thank You")
            return
        if st.button("Send"):
            func()


         # About Us Page
    if page_selection == "Our Services":


        # table of contents on the sidebar
        st.sidebar.title("Table of contents")
        st.sidebar.info("The table of contents is interactive")
        class Toc3:
            def __init__(self):
                self._items = []
                self._placeholder = None

            def title(self, text):
                self._markdown(text, "h1")

            def header(self, text):
                self._markdown(text, "h2", " " * 2)

            def subheader(self, text):
                self._markdown(text, "h3", " " * 4)

            def placeholder(self, sidebar = False ):
                self._placeholder = st.sidebar

            def generate(self):
                if self._placeholder:
                    self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

            def _markdown(self, text, level, space=""):
                key = "".join(filter(str.isalnum, text)).lower()

                st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
                self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


        toc3 = Toc3()

        toc3.placeholder()


        # Our Company background story

        # Content creators who worked on this assignment
        toc3.title("Our Services")

        toc3.header("Intelligence")
        st.image("resources/imgs/intel.jpeg")
        

        toc3.header("Data Analysis")
        st.image("resources/imgs/analysis.jpg")
        
        toc3.header("Data Integration")
        st.image("resources/imgs/integraton.jpg")

        toc3.header("Predictive Analysis")
        st.image("resources/imgs/predictive.jpg")

        toc3.header("Data Science")
        st.image("resources/imgs/science.jpg")

        toc3.header("Data Visualization")
        st.image("resources/imgs/visualization.jpg")

        toc3.generate()

        
       
       

if __name__ == '__main__':
    main()
