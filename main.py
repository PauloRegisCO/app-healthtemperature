import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Temperatura_1ano.csv').iloc[:, 1:] # Ano de 2020
df['Datetime'] = df['Datetime'].values.astype('datetime64[s]')
df['WTG'] = df['WTG'].astype('string')
df['Month'] = df['Datetime'].dt.month.astype('string')
df['Year'] = df['Datetime'].dt.year.astype('string')

st.set_page_config(page_title=' Main bearing analysis',
                   page_icon=':bar_chart:',
                   layout='wide')

# 0) Side Bar
year = st.sidebar.multiselect(key = 1, 
                               label = 'Year', 
                               options = df['Year'].unique(),
                               default = df['Year'].unique())

month = st.sidebar.selectbox(key = 2, 
                               label = 'Month', 
                               options = df['Month'].unique())

df = df.query('Month == @month and Year == @year')

# 1) Main bearing analysis

st.header(':bar_chart: WTG TEMPERATURE HEALTH REPORT')
st.markdown('#')
st.markdown("""### Main bearing analysis""")

col1, col2 = st.columns(2)

# Coluna 1
df_mainbearing = df.groupby(['WTG']).mean(numeric_only=True).reset_index()[['WTG', 'Rotor bearing temp (°C)']]
df_mainbearing = df_mainbearing.melt(id_vars=['WTG'], 
        var_name="Bearing", 
        value_name="Temperature").sort_values(by='WTG', ascending=False)

fig_mainbearing = px.scatter(df_mainbearing, x='Temperature', y='WTG', color = 'Bearing', width=700, height=400, color_discrete_sequence=px.colors.qualitative.Bold)
fig_mainbearing.add_vline(x=40, line_width=2, line_dash="dash", line_color="orange")
fig_mainbearing.add_vline(x=50, line_width=2, line_dash="dash", line_color="red")
fig_mainbearing.update_layout(title_text='Main Bearing Temperature Average',title_x=0.05, showlegend=True, legend_title=None,template="plotly_white", xaxis_title="Temperature", 
                              yaxis_title="WTG", legend=dict(orientation="h", yanchor="bottom", y=0.98, xanchor="right", x=1))
fig_mainbearing.update_xaxes(dtick=5, range=[5, 95])

col1.plotly_chart(fig_mainbearing)

#Coluna 2
df_mainbearing_col2 = df[['WTG', 'Rotor bearing temp (°C)']]
df_mainbearing_col2 = df_mainbearing_col2.melt(id_vars=['WTG'], 
        var_name="Bearing", 
        value_name="Temperature").sort_values(by='WTG', ascending=False)

fig_mainbearing_col2 = px.box(df_mainbearing_col2, x='Temperature', y='WTG', color = 'Bearing', width=700, height=400, color_discrete_sequence=px.colors.qualitative.Bold)
fig_mainbearing_col2.add_vline(x=40, line_width=2, line_dash="dash", line_color="orange")
fig_mainbearing_col2.add_vline(x=50, line_width=2, line_dash="dash", line_color="red")
fig_mainbearing_col2.update_layout(title_text='Main Bearing Temperature Boxplot',title_x=0.05, showlegend=True, legend_title=None,template="plotly_white", xaxis_title="Temperature", 
                              yaxis_title="WTG", legend=dict(orientation="h", yanchor="bottom", y=0.98, xanchor="right", x=1))
fig_mainbearing_col2.update_xaxes(dtick=5, range=[5, 95])

col2.plotly_chart(fig_mainbearing_col2)


# 2) Gearbox analysis
st.markdown('#')
st.markdown("""### Gearbox analysis""")

col1, col2 = st.columns(2)

# Coluna 1
df_gearbearing = df.groupby(['WTG']).mean(numeric_only=True).reset_index()[['WTG', 'Front bearing temperature (°C)','Rear bearing temperature (°C)']]
df_gearbearing = df_gearbearing.melt(id_vars=['WTG'], 
        var_name="Bearing", 
        value_name="Temperature").sort_values(by='WTG', ascending=False)

fig_gearbearing = px.scatter(df_gearbearing, x='Temperature', y='WTG', color = 'Bearing', width=700, height=400, color_discrete_sequence=px.colors.qualitative.Bold)
fig_gearbearing.add_vline(x=80, line_width=2, line_dash="dash", line_color="orange")
fig_gearbearing.add_vline(x=90, line_width=2, line_dash="dash", line_color="red")
fig_gearbearing.update_layout(title_text='Gearbox Bearings Temperature Average',title_x=0.05, showlegend=True, legend_title=None,template="plotly_white", xaxis_title="Temperature", yaxis_title="WTG",
                              legend=dict(orientation="h", yanchor="bottom", y=0.98, xanchor="right", x=1))
fig_gearbearing.update_xaxes(dtick=5, range=[5, 95])

col1.plotly_chart(fig_gearbearing)

#Coluna 2
df_gearbearing_col2 = df[['WTG', 'Front bearing temperature (°C)','Rear bearing temperature (°C)']]
df_gearbearing_col2 = df_gearbearing_col2.melt(id_vars=['WTG'], 
        var_name="Bearing", 
        value_name="Temperature").sort_values(by='WTG', ascending=False)

fig_gearbearing_col2 = px.box(df_gearbearing_col2, x='Temperature', y='WTG', color='Bearing', width=700, height=400, color_discrete_sequence=px.colors.qualitative.Bold)
fig_gearbearing_col2.add_vline(x=80, line_width=2, line_dash="dash", line_color="orange")
fig_gearbearing_col2.add_vline(x=90, line_width=2, line_dash="dash", line_color="red")
fig_gearbearing_col2.update_layout(title_text='Gearbox Bearings Temperature Boxplot',title_x=0.05, showlegend=True, legend_title=None,template="plotly_white", xaxis_title="Temperature", 
                              yaxis_title="WTG", legend=dict(orientation="h", yanchor="bottom", y=0.98, xanchor="right", x=1))
fig_gearbearing_col2.update_xaxes(dtick=5, range=[5, 95])

col2.plotly_chart(fig_gearbearing_col2)

# 3) Generator analysis
st.markdown('#')
st.markdown("""### Generator analysis""")

col1, col2 = st.columns(2)

#Coluna 1
df_genbearing = df.groupby(['WTG']).mean(numeric_only=True).reset_index()[['WTG', 'Generator bearing rear temperature (°C)','Generator bearing front temperature (°C)']]
df_genbearing = df_genbearing.melt(id_vars=['WTG'], 
        var_name="Bearing", 
        value_name="Temperature").sort_values(by='WTG', ascending=False)

fig_genbearing = px.scatter(df_genbearing, x='Temperature', y='WTG', color = 'Bearing', width=700, height=400, color_discrete_sequence=px.colors.qualitative.Bold)
fig_genbearing.add_vline(x=60, line_width=2, line_dash="dash", line_color="orange")
fig_genbearing.add_vline(x=70, line_width=2, line_dash="dash", line_color="red")
fig_genbearing.update_layout(title_text='Generator Bearings Temperature Average',title_x=0.05, showlegend=True, legend_title=None,template="plotly_white", xaxis_title="Temperature", yaxis_title="WTG",
                             legend=dict(orientation="h", yanchor="bottom", y=0.98, xanchor="right", x=1))
fig_genbearing.update_xaxes(dtick=5, range=[5, 95])

col1.plotly_chart(fig_genbearing)

#Coluna 2
df_genbearing_col2 = df[['WTG', 'Generator bearing rear temperature (°C)','Generator bearing front temperature (°C)']]
df_genbearing_col2 = df_genbearing_col2.melt(id_vars=['WTG'], 
        var_name="Bearing", 
        value_name="Temperature").sort_values(by='WTG', ascending=False)

fig_genbearing_col2 = px.box(df_genbearing_col2, x='Temperature', y='WTG', color='Bearing', width=700, height=400, color_discrete_sequence=px.colors.qualitative.Bold)
fig_genbearing_col2.add_vline(x=60, line_width=2, line_dash="dash", line_color="orange")
fig_genbearing_col2.add_vline(x=70, line_width=2, line_dash="dash", line_color="red")
fig_genbearing_col2.update_layout(title_text='Generator Bearings Temperature Boxplot',title_x=0.05, showlegend=True, legend_title=None,template="plotly_white", xaxis_title="Temperature", 
                              yaxis_title="WTG", legend=dict(orientation="h", yanchor="bottom", y=0.98, xanchor="right", x=1))
fig_genbearing_col2.update_xaxes(dtick=5, range=[5, 95])

col2.plotly_chart(fig_genbearing_col2)