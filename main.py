import streamlit as st
from rembg import remove
from PIL import Image, ImageDraw
from io import BytesIO
import base64
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from st_aggrid import AgGrid
import os
import streamlit.components.v1 as components
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    value: int


st.set_page_config(layout="wide", page_title="AI smart factory")
df = pd.read_csv("data/Nike.csv")
df_status = pd.read_csv("data/Nike_status.csv")
df_sample = pd.read_csv("data/sample.csv")

def extract_image_names(images):
    image_names = []
    for image_path in images:
        file_name = os.path.basename(image_path)
        image_name = os.path.splitext(file_name)[0]
        image_names.append(image_name)
    return image_names

large_image_path ="./data/images/Nice_Adbe123Nice_back_270.jpg"
images = [
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
]
images_origin = [
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
    "./data/images/Nice_Adbe123Nice_back_270.jpg",
]
image_info = {
    'number': "2391235",
    'device': "1",
    'time': ['2024-06-06 11:23:24'],
    'error': ['exist'],
    'orderer': ['Adbe123Nice'],
    'position': ['front']
}



st.sidebar.write("# :house: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Smartcoop",)
with st.sidebar:
    choice = option_menu("Menu", ["inspection", "Statistics", "AI-models","Data", "System", "Admin" ],
                        icons=['calendar-week', 'bar-chart-fill', 'bi bi-robot',"database", "cpu",'people-fill'],
                        menu_icon="house", default_index=0,
                        styles={
                                "container": {"padding": "4!important", "background-color": "#fafafa"},
                                "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )
    if choice == "inspection":
        sub_choice = st.selectbox("choose factory", ["factory 1", "factory 2", "factory 3"])
        
        st.selectbox("choose device", ["device 1", "device 2", "device 3"])
    if choice == "Statistics":
        sub_choice = st.selectbox("Statistics Options", ["1", "2", "3"])



# inspcetion 내용
if choice == "inspection":
    st.write("## Live monitor")
    st.write(
        "You can inspect the product's condition in the displayed screen, which shows examples of the front, back, left, right, top, and bottom views to determine any defects. The displayed screen was created [here](https://www.smartcoop.kr), please feel free to inquire about any questions you may have.:grin:"
    )

    st.divider()
    # monitor1, nomitor2 = st.columns(2)
    # with monitor1:
    #     st.selectbox("", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q")
    # with monitor2:
    #     st.selectbox("", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q")        
    button_style = """
    <style>
    .button {
        background-color: transparent;
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
    }
    .button:hover {
        color: yellow;
    }
    </style>
    """



    def load_image(image_path):
        return Image.open(image_path)

    right_column, left_column = st.columns([1, 1])
    #🔴 🟡 ⚪ 🟢
    with right_column:
                
        monitor_q = st.selectbox("Choose monitor", options=["back", "front", "top", "Q4"], index=2, key="monitor_q")

        # with status2:
        #     st.markdown("""
        #                 <style>
        #                 .custom-button {
        #                 display: flex;
        #                 background-color: white;
        #                 color: white;
        #                 margin: 100px 0px 0px 0px;
        #                 border: none;
        #                 cursor: pointer;
        #                 height: 100px;
        #                 width: 100%;
        #                 justify-content: flex-end;
        #                 text-align: right;
        #                 }
        #                 .custom-button:hover {
        #                 opacity: 0.8;
        #                 }
        #                 </style>
        #                 <button class="custom-button">back ⚪ 🟢</button>
        #                 """, unsafe_allow_html=True)

        st.image(load_image(large_image_path), use_column_width=True)
        st.write("### information")
        # df_info = pd.DataFrame(image_info)
        # col1, col2,col3 = st.columns(3)
        # with col1:
        #     transposed_df = df_info[['number', 'device']].T
        #     st.table(transposed_df)      
        # with col2:
        #     transposed_df = df_info[['time', 'error']].transpose()
        #     st.table(transposed_df)            
        # with col3:
        #     transposed_df = df_info[['orderer', 'position']].transpose()
        #     st.table(transposed_df)         

        dataF = pd.DataFrame(
            [["facoty 1","Adbe123Nice","1","back","270"]],columns=["factory","product_name","status","camera","size"]
            )
        st.dataframe(dataF,use_container_width=True, hide_index=True)


    with left_column:

        st.markdown("""
                    <style>
                    .custom-button {
                    display: flex;
                    background-color: white;
                    color: white;
                    margin: 0;
                    border: none;
                    cursor: pointer;
                    height: 10px;
                    width: 100%;
                    justify-content: flex-end;
                    text-align: right;
                    }
                    .custom-button:hover {
                    opacity: 0.8;
                    }
                    </style>
                    <button class="custom-button"> </button>
                    """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:

            st.image(load_image(images[0]), use_column_width=True,caption="front")
            st.image(load_image(images[1]), use_column_width=True,caption="left")
            st.image(load_image(images[2]), use_column_width=True,caption="right")
        with col2:
            st.image(load_image(images[3]), use_column_width=True,caption="top")
            st.image(load_image(images[4]), use_column_width=True,caption="bottom")
            st.image(load_image(images[5]), use_column_width=True,caption="back")

    # 표
    st.divider()
    def highlight_non_zero(value):
        if value != 0:
            return 'background-color: #3FE87F'  # 원하는 색상으로 변경 가능
        else:
            return 'background-color: #F05650'
    styled_df = df.style.applymap(highlight_non_zero, subset=['status'])
    st.dataframe(styled_df, hide_index=True)

    # 에러 이미지들
    st.divider()
    st.title("Defective Product")

    # 2*3 그리드 레이아웃으로 이미지 표시
    cols = st.columns(6)
    for i, col in enumerate(cols):
        col.image(images_origin[i], use_column_width=True, caption=f"product {i+350232}")

    # 이미지 선택 시 크게 표시
    image_name = extract_image_names(images)
    selected_image = st.selectbox("choose error iamge.", image_name)
    if selected_image:
        # image1, image2 = st.columns(2)
        # with image1 :
        st.image(large_image_path, caption="선택한 이미지" , width= 800)
        # with image2 :
            
if choice == "Statistics":

    URL = "data/datata.csv"

    df = pd.read_csv(URL)

    st.title("Amount of products")
    st.markdown("Source table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)")

    with st.expander("See full data table"):
        st.write(df)

    with st.form("products-form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("Choose a starting date")
            start_quarter = st.selectbox("Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q")
            start_year = st.slider("Year", min_value=1991, max_value=2023, value=1991, step=1, key="start_y")

        with col2:
            st.write("Choose an end date")
            end_quarter = st.selectbox("Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=0, key="end_q")
            end_year = st.slider("Year", min_value=1991, max_value=2023, value=2023, step=1, key="end_y")
            
        with col3:
            st.write("Choose a device")
            target = st.selectbox("Choose a device", options=df.columns[1:], index=0)

        submit_btn = st.form_submit_button("Analyze", type="primary")

    start_date = f"{start_quarter} {start_year}"
    end_date = f"{end_quarter} {end_year}"

    def format_date_for_comparison(date):
        if date[1] == 2:
            return float(date[2:]) + 0.25
        elif date[1] == 3:
            return float(date[2:]) + 0.50
        elif date[1] == 4:
            return float(date[2:]) + 0.75
        else:
            return float(date[2:])

    def end_before_start(start_date, end_date):
        num_start_date = format_date_for_comparison(start_date)
        num_end_date = format_date_for_comparison(end_date)

        if num_start_date > num_end_date:
            return True
        else:
            return False

    def display_dashboard(start_date, end_date, target):
        tab1, tab2 = st.tabs(["products change", "Compare"])
        
        with tab1:
            st.subheader(f"{target} change from {start_date} to {end_date}")

            col1, col2 = st.columns(2)
            
            with col1:
                initial = df.loc[df['Quarter'] == start_date, target].item()
                final = df.loc[df['Quarter'] == end_date, target].item()

                percentage_diff = round((final - initial) / initial * 100, 2)
                delta = f"{percentage_diff}%"
                st.metric(start_date, value=initial)
                st.metric(end_date, value=final, delta=delta)
            
            with col2:
                start_idx = df.loc[df['Quarter'] == start_date].index.item()
                end_idx = df.loc[df['Quarter'] == end_date].index.item()
                filtered_df = df.iloc[start_idx: end_idx+1]

                fig, ax = plt.subplots()
                ax.plot(filtered_df['Quarter'], filtered_df[target])
                ax.set_xlabel('Time')
                ax.set_ylabel('products')
                ax.set_xticks([filtered_df['Quarter'].iloc[0], filtered_df['Quarter'].iloc[-1]])
                fig.autofmt_xdate()
                st.pyplot(fig)

        with tab2:
            st.subheader('Compare with other devices')
            all_targets = st.multiselect("Choose other  devices", options=filtered_df.columns[1:], default=[target])
            
            fig, ax = plt.subplots()
            for each in all_targets:
                ax.plot(filtered_df['Quarter'], filtered_df[each])
            ax.set_xlabel('Time')
            ax.set_ylabel('products')
            ax.set_xticks([filtered_df['Quarter'].iloc[0], filtered_df['Quarter'].iloc[-1]])
            fig.autofmt_xdate()
            st.pyplot(fig)

    if start_date not in df['Quarter'].tolist() or end_date not in df['Quarter'].tolist():
        st.error("No data available. Check your quarter and year selection")
    elif end_before_start(start_date, end_date):
        st.error("Dates don't work. Start date must come before end date.")
    else:
        display_dashboard(start_date, end_date, target)

        st.divider()

        st.write("## Detail options")
        col1, col2, col3 = st.columns(3)
        with col1:
            factory = st.selectbox('Factory', options=["ALL", "factory 1","factory 2"])
            line = st.selectbox('Line', options=["line 1", "line 2","line 3"])
        with col2:
            date = st.date_input(label="Date")
            time = st.time_input(label="Time")
        with col3:
            position = st.selectbox('Position', options=["ALL","Front", "Back","Left","Right","Top","Bottom"])
            st.write("See only ")
            check1, check2 = st.columns(2)
            with check1:
                defective = st.checkbox("Normal items" )
            with check2:
                Normal= st.checkbox("Defective items")
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


        st.divider()

        def highlight_non_zero(value):
            if value != 0:
                return 'background-color: #3FE87F'  # 정상
            else:
                return 'background-color: #F05650'  # 비정상
        styled_df_status = df_status.style.applymap(highlight_non_zero, subset=['status'])
        statistics1,statistics2 = st.columns(2)
        with statistics1:
            st.write("### Product")
            st.dataframe(styled_df_status, hide_index=True)
        with statistics2:
            st.write("### Daily production")
            st.line_chart(df_sample, x="date", y =["error","total","normal"])
        
        st.divider()

