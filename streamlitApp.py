import streamlit as st
import pandas as pd

st.title("What's on your mind today?")
input_text = st.text_input("Ask anything")

#conditional logic with widgets
name =  st.text_input("Enter Your name : ")
if st.button("Greet"):
   st.success(f"Hello, {name}!")

upload_file = st.file_uploader("Upload a csv ", type='csv')
if upload_file:
   df = pd. read_csv(upload_file)
   st.dataframe(df)

st.header("This is a header")
st.subheader("This is a sub header")
st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")

st.text_input("What is your name?")
st.text_area("Write something.....")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

option = st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
   st.write("Chart would appear here")
else:
   st.write("Table would appear here")

with st.form("Login Form"):
   username = st.text_input("Username")
   password = st.text_input("Password", type= "password")
   submitted = st.form_submit_button("Login")

   if submitted:
      st.success(f"Welcome, {username}!")

st.image("https://www.bing.com/images/search?view=detailV2&ccid=uHaqRdiM&id=FD736B7D899D5D32087545913F076EB6EEFFC046&thid=OIP.uHaqRdiMzWSMCR2LzsmhtQHaEZ&mediaurl=https%3a%2f%2fimages.pexels.com%2fphotos%2f1188083%2fpexels-photo-1188083.png%3fcs%3dsrgb%26dl%3dsea-dawn-nature-1188083.jpg%26fm%3djpg&exph=3389&expw=5698&q=online+free+images&mode=overlay&FORM=IQFRBA&ck=DEA42EBA24930BFED53219D3BEDBBC31&selectedIndex=0&idpp=serp", caption = "Sample Image")

st.video("https://www.youtube.com/watch?v=QlSmlGOALNQ")