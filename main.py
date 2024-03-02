import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title("Streamlit For Beginner")

st.write("Progress bar showing")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.05)

"Done!!!"


left_column, right_column = st.columns(2)
button = left_column.button("Show text on left column")
if button:
    right_column.write("This is right column.")

expander = st.expander("Inquiry")
expander.write("Write your inquiry.")

text = st.text_input("What is your fav thing?")
"Your fav thing is...", text

condition = st.slider("What is your condition?", min_value=0, max_value=100)
"My condition is...", condition


# option = st.selectbox(
#     "Your favorite number?",
#     list(range(1,11))
# )
# "Your favorite number is,", option, "right?"


# if st.checkbox("Show image"):
#     img = Image.open("001.jpg")
#     st.image(img, caption="riorsk", use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )


# st.dataframe(df.style.highlight_max(axis=0))
# st.map(df)