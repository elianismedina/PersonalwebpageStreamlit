from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Elianis Medina", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style",unsafe_allow_html=True)

local_css("style/style.css")


# ---LOAD ASSETS ---
lottie_leader = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_8udmnhsx.json")
img_contact_form = Image.open("images/video1.png")

# ----HEADER SECTION ----
with st.container():

    st.subheader("Hi, I am Elianis :wave:")
    st.title("A team leader from Colombia")
    st.write("I am passionate about leading teams to reach their full potential while driving excellent performance")
    st.write("[Learn more >](https://www.linkedin.com/in/elianis-medina/)")
# ---WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            

            """
        )
        st.write("[YouTube channel >](https://www.youtube.com/channel/UCSpa16D5IK-e8N38zw1YrVg)")
    with right_column:
        st_lottie(lottie_leader,height=300,key= "leader")
# ---MY PROJECTS ---
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st. subheader("Fundamentos del programa de Ing. Multimedia en la UNAD")
        st.write(
            """
            """
        )
        st.markdown("[Watch video..](https://www.youtube.com/watch?v=XAVR3ZSR2tA)")
# ---CONTACT FORM ---
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/elianismedina05@outlook.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="Your name" required>
      <input type="email" name="email" placeholder="Your email" required>
      <textarea name="message" placeholder="Your message here" required></textarea>
      <button type="submit">Send</button>
    </form>

    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()