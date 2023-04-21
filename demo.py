# -*- coding: utf-8 -*-

# Libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

import time

#=====================================================================
# Functions
def rand_team_mate(namelist):

    # pre_rand = np.random.permutation(namelist)

    # full_empt = np.array(['Nobody' for _ in range(10 - len(pre_rand))])

    # res_arr = pre_rand.astype(str) + full_empt.astype(str) #np.zeros((10 - len(pre_rand),), dtype='string')

    ##

    pre_rand = pd.Series(namelist).sample(frac=1).tolist()

    res_arr = pre_rand + ['都沒人' for _ in range(10 - len(pre_rand))]

    return np.array(res_arr).reshape(5, 2)


#=====================================================================
# Header
st.set_page_config(
    page_title='Civil War of DCT | AhKai',
    page_icon=':cat:',
    # layout='wide'
)

#=====================================================================
# Body
st.image('./static/images/dct.png')

# if "visibility_input" not in st.session_state:
#     st.session_state.visibility_input = "visible"
#     st.session_state.disabled_input = False

#----------------------------------------------------------------
# 名單還沒人
if "name_list" not in st.session_state:
    st.session_state.name_list = [] # 名單
    st.session_state.label_text = "內戰了啦？我開房 👌"
    # st.session_state.visibility_input = "visible" # 輸入框
    st.session_state.disabled_input = False
    st.session_state.placeholder = "來，ID這邊"

# 滿房
elif len(st.session_state.name_list) == 10:
    st.session_state.disabled_input = True
    st.session_state.label_text = "滿了？不然我讓，我去煮泡麵 🍜"
    st.session_state.placeholder = "OP，掰掰 👋"

else:
    st.session_state.label_text = "該打了吧？全部等你一個 👇"

#----------------------------------------------------------------
# ID輸入框
input_name = st.text_input(
        st.session_state.label_text,
        # label_visibility=st.session_state.visibility_input,
        disabled=st.session_state.disabled_input,
        placeholder=st.session_state.placeholder,
    )
if input_name != '':
    # 寫入名單
    st.session_state.name_list.append(input_name)
    # if len(st.session_state.name_list) == 0:
    #     st.session_state.name_list = [input_name]
    # else:
    #     st.session_state.name_list.append(input_name)


#----------------------------------------------------------------
# 玩家列表
# if len(st.session_state.name_list) <= 5:
#     st.write(st.session_state.name_list)

# else:
#     st.write(st.session_state.name_list)

# 玩家列表
hero_list = st.multiselect(
    '⚔ 戰士們 ⚔',
    options=st.session_state.name_list,
    default=st.session_state.name_list,
    # on_change=,
    max_selections=10,
    key='hero_list',
)

if len(st.session_state.hero_list) < len(st.session_state.name_list):
    st.session_state.name_list = st.session_state.hero_list

#----------------------------------------------------------------
# 分組

if st.button('分組'):
    st.write(rand_team_mate(st.session_state.name_list))


# df = pd.DataFrame({
#     'name': ['台北101', '帝寶樓', '故宮博物院'],
#     'lat': [25.0338, 25.0357, 25.1029],
#     'lon': [121.5645, 121.6163, 121.5486]
# })

# st.sidebar.map(df)

