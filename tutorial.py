import streamlit as st
st.set_page_config(page_title='Luffy',page_icon='random')
mymenu=st.sidebar.selectbox('my menu',('home','fill form','download'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1-160x90.png')
st.title('onlei technologies')
st.header('by abhinav shrivastava')
st.text('this is a tutorial of streamlit library')
if (mymenu=='home'):    
    st.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)
    st.video('https://youtu.be/ekgUjyWe1Yc?si=v-rfDxEe58Irr6Ag')
elif (mymenu=='fill form'):
    with st.form('my form'):
        name=st.text_input('enter name ')
        dob=st.date_input('choose dob ')
        marks=st.slider('choose marks ')
        k=st.form_submit_button('submit form')
        if k:
            st.write('Name=',name,'DOB=',dob,'Marks=',marks)

elif(mymenu=='download'):
    st.header('DOWNLOADS')
    st.download_button('Downlaod now','this a downloaded data of streamlit tutorial','onlei.txt')
    
