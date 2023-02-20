import streamlit as st
from streamlit_option_menu import option_menu
# from st_on_hover_tabs import on_hover_tabs
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io


# # hide the hamburger menu?
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidde;}
        footer:after {content:'Copyright @ 2023: ssongssognssong all rights reserved';
        display:block;
        opsition:relatiive;
        color:tomato;
        padding:5px;
        top:100px;}

        </style>
        """

# st.set_page_config(layout="wide", page_title="ssongssognssong")
st.markdown(hide_menu_style, unsafe_allow_html=True) # hide the hamburger menu?





# sidebar menu
with st.sidebar:
    choose = option_menu("기술연구소", ["Green Remodeling", "Metro", "GHG Emission"],
                         icons=['house', 'bi bi-bus-front', 'bi bi-thermometer-high'],
                         menu_icon="bi bi-list-ul", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#6e6a6a"},
        "icon": {"color": "white", "font-size": "30px"}, 
        "nav-link": {"font-weight":"bolder","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
        "nav-link-selected": {"background-color": "#F6CECE"},
    }
    )

