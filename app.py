import streamlit as st
import pandas as pd

st.title('My first app')

st.write("Hello, world!")

st.write("Hello, again!")

import streamlit as st

st.header('Tossing a Coin')

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')

st.write('It is not a functional application yet. Under construction.')


import scipy.stats
import streamlit as st
import time

st.header('Tossing a Coin')

import pandas as pd
   
chart_data = pd.DataFrame([0.5])
chart = st.line_chart(chart_data)
   

def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
           outcome_1_count += 1
        mean = outcome_1_count / outcome_no
           
           # Convert to DataFrame
        new_data = pd.DataFrame([mean], columns=["Mean"])
        chart.add_rows(new_data)
        time.sleep(0.05)

       return mean
   

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experient of {number_of_trials} trials.')