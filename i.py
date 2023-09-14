# Code
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    'https://raw.githubusercontent.com/namanNagelia/airplaneDataAnalysis/main/Airplane%20Strikes%20Dataset.csv')
pd.set_option('display.max_columns', None)
year_counts = df.groupby("Incident Year").size(
).reset_index(name="Incident Count")
state_incidents = df.groupby("State").size().reset_index(name="Incident Count")
species_incidents = df.groupby(
    "Species Name").size().reset_index(name="Incident Count")
Flight_Phase = df.groupby("Flight Phase").size(
).reset_index(name="Incident Count")

df2 = pd.DataFrame()

for i in range(37, len(df.columns)):
    column_name = df.columns[i]
    df2[column_name] = df[column_name]

df2 = df2.sum()
series = df2.squeeze()
total_sum = series.sum()
percentages = (series / total_sum) * 100
percentage_df = pd.DataFrame(
    {'Damage Type': percentages.index, '%': percentages.values})
print(percentage_df)


pd.set_option('display.max_columns', None)
# Print the DataFrame

fig = px.line(year_counts, x="Incident Year", y="Incident Count",
              title="Incidents per Year", line_shape='linear')
fig_state = px.bar(state_incidents, x="State",
                   y="Incident Count", title="Incidents Per State")
fig_state_map = px.scatter_geo(state_incidents,
                               locations="State",
                               locationmode="USA-states",
                               color="Incident Count",
                               hover_name="State",
                               title="Incidents Per State (Map)",
                               scope="usa", color_continuous_scale=['#87CEFA', 'darkred']
                               )

# Customize the map layout
fig_state_map.update_geos(
    showland=True, landcolor="rgb(245, 245, 245)",
    showsubunits=True, subunitcolor="rgb(200, 200, 200)",
    countrycolor="rgb(200, 200, 200)",
    showlakes=True, lakecolor="rgb(255, 255, 255)",
)


fig_species = px.bar(species_incidents, x="Species Name",
                     y="Incident Count", title="Incidents per Species")
fig_Phase = px.bar(Flight_Phase, x="Flight Phase",
                   y="Incident Count", title="Incidents per phase of flight")
fig_damage = px.bar(percentage_df, x="Damage Type", y="%",
                    title="Percentage of Incidents")
st.title("Raymond Yang Data Analysis")
st.plotly_chart(fig)
st.plotly_chart(fig_state)
st.plotly_chart(fig_state_map)
st.plotly_chart(fig_species)
st.plotly_chart(fig_Phase)
st.plotly_chart(fig_damage)
