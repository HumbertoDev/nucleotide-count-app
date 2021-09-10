#####################
# Import Libraries
#####################

from os import rename
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


#####################
# Page Header
#####################

image = Image.open('dna-counter-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This Web Application counts your Nucleotide composition.

## What is a Nucleotide?

A nucleotide is the essential part of our DNA. It is composed by 4 elements:

1. Adenine (A)
2. Thymine (T)
3. Guanine (G)
4. Cytosine (C)

Every human being have **3 billion nucleotide pairs**. that's make us unique from others.

***
""")

#####################
# Imput Text Box
#####################

st.header('Are You Ready? Write Your DNA Sequence Here!')

# This will be the example dna input
sequence_input = ">Enter Your DNA right bellow:\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# Asign the user input to a variable call sequence. 

sequence = st.text_area('Sequence Input', sequence_input, height=275) #  This will create a text box
sequence = sequence.splitlines() # this will separate out DNA input into an array with 4 elements
sequence = sequence[1:] # We just select the lines we need to the nucleotide count
sequence = ''.join(sequence)

#####################
# Create a function that make a dict of the DNA elements
#####################

def dnaCounter(seq):
    d = dict([
                ('A', seq.count('A')),
                ('T', seq.count('T')),
                ('G', seq.count('G')),
                ('C', seq.count('C')),
                ])
    return d

y = dnaCounter(sequence)

#####################
# Displaying the data in a Data Frame
#####################
st.subheader('Nucleotide Count')

y_df = pd.DataFrame.from_dict(y, orient='index')
y_df = y_df.rename({0:'Count'}, axis='columns')
y_df.reset_index(inplace=True)
y_df = y_df.rename(columns = {'index':'Nucleotide'})
y_df

#####################
# Displaying the data in a Chart
#####################

st.write("""
### Nucleotide Chart
""")

chart = alt.Chart(y_df).mark_bar().encode(
    x = 'Nucleotide',
    y='Count',
)

chart = chart.properties(
    width=alt.Step(80)
)

st.write(chart)