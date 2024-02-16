import streamlit as st
import pandas as pd

st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# Racer Page 🎈")

st.write(' # Mariokart *Stats Website*') # "write" is like streamlit's version of print

df_racer = pd.read_csv('streamlit_template/data/racer_stats.csv') # read the csv file with panda

# st.write(df_racer) # this option will load in the entire dataset

st.dataframe(df_racer.style # by putting the "." at the end, we are altering the dataframe
             .highlight_max(color = 'lightgreen', axis = 0, subset = ['Speed', 'Acceleration', 'Weight'])
             .highlight_min(color = 'red', axis = 0, subset = ['Speed', 'Acceleration', 'Weight'])
) # loading it in as a dataframe gives more control. The "subset" parameter allows you to select only the columns you want.

st.line_chart(df_racer, x = 'Speed', y = ['Acceleration', 'Weight', 'Handling', 'Traction/Grip', 'Mini-Turbo']) # With the brackets, we can have multiple data values represented on the same graph

st.header("Racer Speed does not seem to correlate to number of races a character has won.") # Another way to "print", but this has default formatting for a header aka Bold, larger text, etc.
x = st.slider('How Many Racers to Show', 1, len(df_racer)) # st.slider('TITLE', min_value, max_value)

left_column_1, right_column_1 = st.columns(2) # This allocates space for these columns and basically gives them a place to live. This makes the variable "left_column_1" represent an actual position on the page. This way, whatever we do in these with statements will show up in those columns.

with left_column_1:
    st.write("Racers by Speed")
    df_fastest_racers = df_racer[['Character', 'Speed']].sort_values("Speed", ascending = False).iloc[0:x] # This creates a new dataframe called "fastest_racers" and just pulls in the 'Character' and 'Speed' columns. The iloc will look at the slider and limit the rows from 0 to x(whatever the slider is set to)
    st.dataframe(df_fastest_racers) # This line will display the data by making fastest racers a dataframe


with right_column_1:
    st.write("Racers by Win Percent")
    df_best = df_racer[['Character', 'Times First Place', 'Total Races']]
    df_best['Win Percent'] = df_best['Times First Place']/df_best['Total Races'] * 100 # This line creates a new column called "Win Percent" and makes it a calculated field
    df_best = df_best[['Character', 'Win Percent']].sort_values('Win Percent', ascending = False).iloc[0:x]
    st.dataframe(df_best)


character_dictionary = {
    "Lemmy Koopa":"One of Bowser's minions. While they are small and is not all that bright, this guy can really pack a punch.",
    "Baby Mario":"Everyone's favorite character, now in fun size.",
    "Baby Luigi":"Goes to show you how long luigi has been a true loyal brother to Mario's cause.",
    "Bowser Jr":"Bowser's kid, even more... if that is even possible",
    "Toadette":"No affiliation to Toad, Has a Mushroom on her head",
    "Toad":"He's really just a man with a mushroom on his head",
    "Daisy":"Use to be evil and work for Bowser, but fell in love with luigi and cnaged sides",
    "Shy Guy":"You never really see his face, is that because when you race that you are always behind him?",
    "Yoshi":"Now we will be able to see Yoshi's true potentiall without a plumber on his back",
    "Tanooki Mario":"Super suits make all the difference",
    "Link":"Wait, why is he apart of this universe? don't you have your own game?",
    "Waluigi":"Luigi's Torment, although he is just the unloyal compainion to Wario",
    "Wario":"Wacky Mustache and weird colored pants may just be the perfect advantage",
    "Metal Mario":"Looks Like Mario put on some weight!",
    "Mario":"Crowd Favorite",
    "Luigi":"Loyal Companion",
    "Peach":"The Essence of Royalty, and don't get me wrong, Peach can totally hold her own",
    "Donkey Kong": "King of the Jungle",
    "Bowser":"Big and Bad, Everything is fire and brimstone."
}

st.header('Individual Racer Stats')

left_column_2, right_column_2 = st.columns(2)

with right_column_2:
    chosen = st.selectbox('Pick a Racer', df_racer['Character']) # This is a dropdown where the values in the 'character' column can be selected
    description = character_dictionary[chosen] # This will make description equal to the pair that coordinates with the chosen value.
    st.write(description) 

with left_column_2:
    st.image(f"streamlit_template/images/{chosen}.png", width = 200) # This will select an image and it will look for an image with the title of chosen + .png


df_single_racer = df_racer.loc[df_racer['Character'] == chosen].drop(columns = ['Character', 'Times First Place', 'Total Races']) # This will first validate if and display the data only for the character in the dataset that's equal to chosen. Then, it will show all of the available info except for those columns
# st.write(df_single_racer)
df_unp_racer = df_single_racer.unstack().rename_axis(['Category', 'Row Number']).reset_index().drop(columns = 'Row Number').rename({0:"Strength"}, axis =1)
# st.write(df_unp_racer)

st.bar_chart(df_unp_racer, x = 'Category', y = 'Strength')

if st.checkbox('Show All Racers'):
    st.bar_chart(df_racer, x = 'Character', y = ['Speed', 'Acceleration', 'Weight', 'Handling', 'Traction/Grip', 'Mini-Turbo'])