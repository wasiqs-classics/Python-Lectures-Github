import streamlit as st

# Configuration

st.set_page_config(page_title="My Streamlit App", page_icon=":shark:", layout="centered", initial_sidebar_state="expanded")

# Streamlit Text Based Features..

st.title("My Streamlit App")
st.header("This is some heading")
st.subheader("This is a subheading")
st.text("This is some normal text")
st.markdown('"Almost **everything** will work again if you **unplug** it for a few minutes, including **you**." — Anne Lamott"')

code = """
def hello():
    print('Hello World')
"""

st.code(code, language='python')
st.caption("This is a caption")

st.divider()

st.image("dogo.jpg", caption="A dog running fast")

st.image("https://pakdrive.com.pk/wp-content/uploads/2024/08/Microlino-car.webp", caption="Sample Image", width=250)

st.video("https://www.youtube.com/watch?v=zZ_a3WjoPEM")

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.download_button("Click to download", "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")


import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.table(df)

edit_df = st.data_editor(df)

st.write(edit_df)

dict = {
    "Name": "Alice",
    "Age": 25
}

st.json(dict)

st.warning("This is some warning")

st.error("This is an error")

st.success("This is a success message")

button = st.button("Click me")
if button:
    st.write("Button clicked")
    st.balloons()

import numpy as np

data_for_chart = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data_for_chart)
st.bar_chart(data_for_chart)
st.area_chart(data_for_chart)

scatter_xy = pd.DataFrame({
    'x': np.random.randn(50),
    'y': np.random.randn(50)
})

st.scatter_chart(scatter_xy)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # If a file is uploaded, read it using pandas
    df_new = pd.read_csv(uploaded_file)
    st.write("Data from the CSV file:", df_new)


# Streamlit forms

name = st.text_input("Enter your name")
st.write("You entered:", name)
height = st.slider("Select your height", 100, 200, 150)
date_of_birth = st.date_input("Enter your date of birth")
gender = st.selectbox("Select gender", ["Male", "Female"])