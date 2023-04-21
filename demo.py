import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

import time


df = pd.DataFrame({
    'name': ['台北101', '帝寶樓', '故宮博物院'],
    'lat': [25.0338, 25.0357, 25.1029],
    'lon': [121.5645, 121.6163, 121.5486]
})

st.sidebar.map(df)

