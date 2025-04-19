import plotly.graph_objects as go
import pandas as pd

def zscore(g):
    return (g - g.mean()) / g.std(ddof=0)

path = 'Results_21Mar2022.csv'

data = pd.read_csv(path)
groups = ['fish', 'meat', 'meat100', 'meat50', 'vegan', 'veggie']
names = ['Fish-eaters',
         'Medium meat-eaters(50-99g/d)',
         'High meat-eaters(>= 100g/d)',
         'Low meat-eaters(< 50g/d)',
         'Vegans',
         'Vegetarians']
categories = ["GHG (Green House Gas) Emissions",
        "GHG from CH4 emissions from livestock management measured",
        "GHG from N2O emissions associated with fertilizer use",
        "Agricultural Land Use",
        "Biodiversity Impact",
        "Agricultural Water Usage",
        "Acidification Potential",
        "Eutrophication Potential"
        ]
categories.append(categories[0])
colours = ['rgba(0,0,128,0.7)',
           'rgba(128,0,0,0.7)',
           'rgba(255,0,0,0.7)',
           'rgba(200,200,0,0.7)',
           'rgba(0,255,0,0.7)',
           'rgba(0,128,0,0.7)']

a = data.groupby("diet_group")
ghgs = zscore(a["mean_ghgs"].mean())
ghgsch4 = zscore(a["mean_ghgs_ch4"].mean())
ghgsn2o = zscore(a["mean_ghgs_n2o"].mean())
land = zscore(a["mean_land"].mean())
bio = zscore(a["mean_bio"].mean())
watuse = zscore(a["mean_watuse"].mean())
acid = zscore(a["mean_acid"].mean())
eut = zscore(a["mean_eut"].mean())

fig = go.Figure()
for i in range(len(groups)):
    x = groups[i]
    fig.add_trace(go.Scatterpolar(
        r = [ghgs[x], ghgsch4[x], ghgsn2o[x], land[x], bio[x], watuse[x], acid[x], eut[x], ghgs[x]],
        theta = categories,
        fill='none',
        line=dict(color=colours[i]),
        name = names[i]
    ))
fig.update_layout(
    title='GHG emissions, land use, water use, acidification, eutrophication and biodiversity impact level by diet group<br />(All results are presented as Z-scores of the mean value of each group from a Monte Carlo analysis with 1,000 iterations.)',
    showlegend=True)
fig.show()