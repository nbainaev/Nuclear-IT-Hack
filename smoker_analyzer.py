import os

from nn.nn_for_website import analyze

import streamlit as st
from streamlit_echarts import st_echarts
from PIL import Image

def update_and_save_img(img_file_buffer) -> None:
    if "img.jpg" in os.listdir():
        os.remove("img.jpg")
    
    try:
        img = Image.open(img_file_buffer)
        img.save("img.jpg")

    except AttributeError as error:
        return error

def draw_pie(data):
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "pie",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {
                    "borderRadius": 10,
                    "borderColor": "#fff",
                    "borderWidth": 2,
                },
                "label": {"show": False, "position": "center"},
                "emphasis": {
                    "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                },
                "labelLine": {"show": False},
                "data": [],
            }
        ],
    }

    options["series"][0]["data"] += data

    st_echarts(
        options=options, height="250px",
    )

st.title("Smoker analyzer", anchor=False)
st.subheader('Developed by "Десептиконы"')
st.divider()

col_1, col_2 = st.columns(2)

with col_1:
    st.subheader(":blue[О приложении]")
    st.write("Приложение определяет курящего человека на фотографии.")

with col_2:
    st.subheader(":blue[Как сохранить результат?]")
    st.write("В правом верхнем углу выберете пункт 'Print', чтобы распечатать страницу, или воспользуйтесь сочетанием 'ctrl + s', чтобы сохранить страницу.")

st.divider()
img_file_buffer = st.file_uploader(":blue[Загрузите фотографию в формате .jpg]", type='jpg')
# img_file_buffer = st.camera_input(":blue[Нажмите на кнопку, чтобы снять фото]", label_visibility='visible', disabled=False)

col_3, col_4 = st.columns(2)

if img_file_buffer is not None:
    try:
        with st.spinner('Обработка изображения…'):
            update_and_save_img(img_file_buffer)
            bounding, all_detected, smokers = analyze("img.jpg")

        with col_3:
            st.subheader(":blue[Статистика]")
            draw_pie([{"value": round(smokers / all_detected, 2) * 100, "name": "Курят"}, {"value": round(1 - smokers / all_detected, 2) * 100, "name": "Не курят"}])

        with col_4:
            st.subheader(":blue[Обработанная фотография]")
            st.image(bounding)

    except TypeError as e:
        st.warning("Объект не найден, загрузите другую фотографию!", icon="🚨")

