import streamlit as st
import os

st.set_page_config(
    page_title = "BCN Aire",
    page_icon = '🌍',
    layout = "wide"
)

st.title("Contaminant Heatmaps With Time for Barcelona")
st.markdown("""
    ### About The App:
    This app is being developed to help visualise historical data about air contaminants in Barcelona.  
    The first map shows the locations of air contaminant monitoring stations in the metropolitan area of Barcelona (AMB).  
    The subsequent visualisations show timelapses of the the levels of specific air contaminants across the city.  
    All maps are interactive. If you scroll on the map it will zoom in or out. To scroll the page, ensure that the cursor is in a white space at either side.


    """)

MAPS_DIR = "maps"

stations_map_path = os.path.join(MAPS_DIR, "stations.html")
contaminant_maps = [file for file in os.listdir(MAPS_DIR) if "_map.html" in file]

if not os.path.exists(stations_map_path):
    st.warning("Stations map not found")
else:
    st.markdown("""
    ## Map of air contaminant monitoring stations  
    Click on a station marker to view weekly average timeplots for the contaminants measured at that station.  
    Use the drop down menu in the chart to change between contaminants or choose to display all contaminants at the same time.
    """)
    with open(stations_map_path, "r") as m:
        st.components.v1.html(m.read(), height=600)

if not contaminant_maps:
    st.warning("No contaminant maps found")
else:
    st.markdown("""
    ## Timelapse maps of air air contaminant levels
    The following maps show timelapses of air contaminant levels between April 2019 and November 2024.  
    Use the controller bar at the top of each map to start/stop the timelapse, move to a certain timeframe, or alter the speed of the timelapse.
    """)
    contaminant_maps = sorted(contaminant_maps)

    cols = st.columns(2)
    for i, map in enumerate(contaminant_maps):
        col = cols[i % 2]
        with col:
            map_name = map.split('_')[0].upper()
            st.markdown(f'#### {map_name}')
            with open(os.path.join(MAPS_DIR, map), 'r') as f:
                st.components.v1.html(f.read(), height=400)