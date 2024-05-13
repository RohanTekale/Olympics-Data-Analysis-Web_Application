import streamlit as st
import pandas as pd
import preprocessor
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# Check if scipy is installed, if not, install it
try:
    import scipy
except ImportError:
    st.error("scipy is not installed. Please install it using 'pip install scipy'.")

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

# Preprocess the data
if not df.empty and not region_df.empty:
    df = preprocessor.preprocess(df, region_df)
else:
    st.error("Data frame is empty. Please check the input CSV files.")

st.sidebar.image("https://imgs.search.brave.com/wgcDct35DolbhcQa1Wo5DggG87Qq-y3EupFgOs7MrUk/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9mcmFt/ZXJ1c2VyY29udGVu/dC5jb20vaW1hZ2Vz/L29LTzc3ZUc2OThH/a0dSYXliSnNjRVdm/SEduRS5wbmc", width=250, use_column_width=False)

st.sidebar.title("Olympics Analysis")
User_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-Wise Analysis', 'Athlete wise Analysis')
)

# st.dataframe(df)

if User_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, Country = helper.Country_year_list(df)
    Selected_year = st.sidebar.selectbox("Select year", years)
    Selected_Country = st.sidebar.selectbox("Select Country", Country)

    medal_tally = helper.fetch_medal_tally(df, Selected_year, Selected_Country)

    if Selected_year == 'Overall' and Selected_Country == 'Overall':
        st.title("Overall Tally")
    if Selected_year != 'Overall' and Selected_Country == 'Overall':
        st.title(" Medal tally in" + str(Selected_year) + " Olympics")
    if Selected_year == 'Overall' and Selected_Country != 'Overall':
        st.title(Selected_Country + " Overall Performance")
    if Selected_year != 'Overall' and Selected_Country != 'Overall':
        st.title(Selected_Country + " Performance in " + str(Selected_year) + " Olympics")
    st.table(medal_tally)

if User_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x='Edition', y='region')
    st.title(" Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Edition', y='Event')
    st.title(" Events over the years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x='Edition', y='Name')
    st.title(" Athletes over the years")
    st.plotly_chart(fig)

    st.title("No of Events Over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(25, 25))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(
        x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
        annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox("Select Sport",sport_list)
    x = helper.most_Successful(df, selected_sport)
    st.table(x)

if User_menu == 'Country-Wise Analysis':

    st.sidebar.title('Country-Wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    Selected_Country= st.sidebar.selectbox('Select Country',country_list)

    country_df= helper.year_wise_medal_tally(df,Selected_Country)
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(Selected_Country+" Medal tally over the years")
    st.plotly_chart(fig)

    st.title(Selected_Country + " excels in the following sports ")
    pt = helper.country_event_heatmap(df,Selected_Country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)

    st.pyplot(fig)

    st.title("Top 10 athletes of "+Selected_Country)
    top10_df = helper.most_Successful_countrywise(df,Selected_Country)
    st.table(top10_df)

if User_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)

    fig.update_layout(autosize = False,width = 800,height = 500)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']

    x = []
    name = []
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    # probability of winning medal in each sport by athletes
    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=800, height=500)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")

    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title("height Vs Weight Analysis")
    selected_sport = st.selectbox("Select a Sport", sport_list)

    temp_df= helper.weight_V_height(df,selected_sport)
    fig, ax = plt.subplots()
    ax= sns.scatterplot(x='Weight', y='Height', data=temp_df,hue=temp_df['Medal'],style=temp_df['Sex'],s=60)

    st.pyplot(fig)

    st.title("Men Vs Women Participation over The Year")
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=800, height=500)
    st.plotly_chart(fig)
