import pandas as pd
import folium
class FoliumTest:
    def __init__(self):
        self.context = "./data"

    def hook(self):
        self.show_map()

    def show_map(self):
        state_geo = self.context + "/us-states.json"
        state_unmployment = self.context + "/US_Unemployment_Oct2012.csv"
        state_date = pd.read_csv(state_unmployment)
        m = folium.Map(location=[37, -102], zoom_start=5)
        #속성값
        m.choropleth(
            geo_data = state_geo,
            name = "choropleth",
            data = state_date,
            columns = ["State", "Unemployment"],
            key_on = "feature.id",
            fill_color = "YlGn",
            fill_opacity = 0.7,
            line_opacity = 0.2,
            lengend_name = "Unemployment Rate (%)"
        )
        folium.LayerControl().add_to(m)
        m.save("./saved_data/USA.html")