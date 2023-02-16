import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io

with st.sidebar:
    choose = option_menu("스마트도시연구본부", ["Green Remodeling", "Metro", "GHG Emission"],
                         icons=['house', 'bi bi-train-freight-front', 'bi bi-thermometer-high'],
                         menu_icon="bi bi-list-ul", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#6e6a6a"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-weight":"bolder","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#000000"},
        "nav-link-selected": {"background-color": "#0a0a0a"},
    }
    )