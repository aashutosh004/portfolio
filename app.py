import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_facial = Image.open("images/facial-recog.jpeg").resize((500, 250))
img_pravah = Image.open("images/pravah.png").resize((400, 270))
img_real_fake = Image.open("images/images (2).jpeg").resize((400, 300))

# ---- HEADER SECTION ----
# with st.container():
#     st.subheader("Namaste, I am Ashutosh Sharma 👨‍💻")
#     st.title("A Computer Science and AIML Engineer")
#     st.write(
#         """I am an AI&ML enthusiast , currently pursuing B.Tech in Computer Science And Engineering (Artificial Intelligence And Machine Learning).
#         Passionate to learn about new technologies in the filed of Engineering and Science and also excited to work on projects."""
#     )
#     st.write("[Linkedin](www.linkedin.com/in/ashutosh-sharma-443710253)")

with st.container():
    left_column, right_column = st.columns((2, 1))  # 2:1 ratio for text:image
    with left_column:
        st.subheader("Namaste, I am Ashutosh Sharma 👨‍💻")
        st.title("A Computer Science and AIML Engineer")
        st.write(
            """I am an AI&ML enthusiast , currently pursuing B.Tech in Computer Science And Engineering (Artificial Intelligence And Machine Learning).
            Passionate to learn about new technologies in the filed of Engineering and Science and also excited to work on projects."""
        )
        st.markdown("[Linkedin](https://www.linkedin.com/in/ashutosh-sharma-443710253) | [Kaggle Profile](https://www.kaggle.com/ashu009) | [Instagram](https://www.instagram.com/09_ashu_04)", unsafe_allow_html=True)

    with right_column:
        # Load and resize profile picture (optional: adjust size as needed)
        profile_pic = Image.open("images/profile.jpg").resize((400, 300))
        st.image(profile_pic, use_container_width=False)

        

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do ?")
        # st.write("##")
        st.write(
            """
                My expertise lies in Machine Learning, Deep Learning, and Generative AI, where I actively work on innovative projects that push the boundaries of AI-driven automation and predictive modeling.

                My Focus Areas:\n
                ✅ Machine Learning & Deep Learning – Building intelligent models for data-driven insights and automation.\n
                ✅ Generative AI – Exploring cutting-edge AI techniques for content generation and creative applications.\n
                ✅ AI Research & Development – Continuously learning and implementing advanced AI methodologies.\n
                ✅ Project Development – Applying AI to real-world challenges, from predictive analytics to intelligent automation.\n

                I am passionate about leveraging AI to solve complex problems and drive impactful innovations. 🚀
            """
        )
        st.write("[GitHub](https://github.com/aashutosh004)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_real_fake)
    with text_column:
        st.subheader("Fake-or-Real-Audio-Classification")
        st.write(
            """
            Fake audio can be used maliciously to spread misinformation. This project leverages Deep Learning techniques (Recurrent Neural Networks (RNN) with Long Short-Term Memory (LSTM)) to create a model capable of detecting fake audio. It provides a robust tool to combat audio-based misinformation by offering a reliable classification system.\n

            This project proposes an automated solution to classify audio as real or fake. It includes the following steps:\n

            Preprocessing raw audio files using Librosa to extract meaningful features. Training a robust model using TensorFlow. Deploying a user-friendly interface for real-time testing using Streamlit.    
            """
        )
        st.markdown("[Code](https://github.com/aashutosh004/Fake-or-Real-Audio-Classification)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_pravah)
    with text_column:
        st.subheader("Pravah")
        st.write(
            """
            Developed an AI-powered biodiversity monitoring system leveraging machine learning and time-series analysis to predict species population trends and conservation needs.\n
            Implemented predictive models to classify species as endangered or extinct, aiding ecological intervention strategies.\n
            Designed an interactive data visualization dashboard to assist policymakers with actionable insights for conservation efforts.
            """
        )
        st.markdown("[Code](https://github.com/aashutosh004/bio)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_facial)
    with text_column:
        st.subheader("Face-Recognition-Model")
        st.write(
            """
            Developed a facial recognition system using Python, OpenCV, and DeepFace. Implemented features for dataset creation, training with FaceNet embeddings, and real-time face recognition, including age, gender, and emotion analysis, with a user-friendly interface for capturing and identifying faces.
            """
        )
        st.markdown("[Code](https://github.com/aashutosh004/Face-Recognition-Model)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
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
