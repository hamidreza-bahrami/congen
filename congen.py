import streamlit as st
from openai import OpenAI
import time

def generator(keyword, writing_style, word_count):
    response = client.chat.completions.create(model = "gpt-3.5-turbo", messages = [{"role":"user", "content": "Write a SEO optimized word article about" + keyword},
                                                                                 {"role":"user", "content": "This article should be in style" + writing_style},
                                                                                 {"role":"user", "content": "The article lenght should be" + str(word_count)}])
    result = ''
    for choice in response.choices:
         result += choice.message.content
    return result

def show_page():
    st.write("<h1 style='text-align: center; color: gold;'>دستیار تولید مقاله 📝</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: gray;'>Gen Ai تولید محتوا با</h2>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")

    st.write("<h6 style='text-align: right; color: gray;'>:کلمه کلیدی خودتو وارد کن</h6>", unsafe_allow_html=True)
    Keyword = st.text_input('')

    st.write("<h6 style='text-align: right; color: gray;'>دوست داری محتوا چطور باشه؟</h6>", unsafe_allow_html=True)
    writing_style = st.selectbox('', ['Funny','Critical','Academic'])

    st.write("<h6 style='text-align: right; color: gray;'>تعداد کلمات مقاله رو مشخص کن</h6>", unsafe_allow_html=True)
    word_count = st.slider('', 300, 1500, 400)


    submit_button = st.button('تولید مقاله')
    if submit_button:
        with st.chat_message("assistant"):
            with st.spinner('''در حال تولید محتوا'''):
                time.sleep(3)
                st.success(u'\u2713''انجام شد')
                article = generator(Keyword, writing_style, word_count)
                st.write(article)
                st.download_button('txt دانلود فایل', article)



with st.sidebar:
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image('icon.png')
        st.write("<h2 style='text-align: right; color: black;'>معرفی مدل</h2>", unsafe_allow_html=True)
        st.write("<h3 style='text-align: right; color: gray;'>سلام، من بهت کمک می کنم مقاله بنویسی</h3>", unsafe_allow_html=True)
        st.write("<h3 style='text-align: right; color: gray;'>برای شروع کار با من، ای پی آی خودتو وارد کن</h3>", unsafe_allow_html=True)
        user_key = st.text_input('API')
        client = OpenAI(api_key = user_key)

show_page()