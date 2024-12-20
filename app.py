import streamlit as st
import os

st.set_page_config(
    page_title = "BCN Aire",
    page_icon = '🌍',
    layout = "wide"
)

st.title("Barcelona Aire")
st.markdown("""
    ### About The App:
    This app is being developed to help visualise historical data about air contaminants in Barcelona.  
    All maps are interactive. If you scroll on the map it will zoom in or out. To scroll the page, ensure that the cursor is in a white space at either side.

    ### About the Data:
    The data displayed in this application was obtained through the AMB Open Data [API](https://opendata.amb.cat/help.html), with available datasets spanning from 2019 through to November 2024.

    ### Contaminant Monitoring:
    At present, this app only contains data on the levels of $NO_2$, $O_3$, $PM_{10}$, and $SO_2$.
    Other contaminants are measured at some stations; however, their coverage across stations is minimal and therfore not included at the moment
    """)

MAPS_DIR = "maps"

stations_map_path = os.path.join(MAPS_DIR, "stations.html")
contaminant_maps = [file for file in os.listdir(MAPS_DIR) if "_map.html" in file]

if not os.path.exists(stations_map_path):
    st.warning("Stations map not found")
else:
    st.markdown("""
    # Air contaminant monitoring stations
    The following map shows the locations of 8 air contaminant monitoring stations in the BarcelonaMetropolitan Area (AMB).  
    1. Click on a station marker to view weekly average timeplots for the contaminants measured at that station.  
    2. Use the drop down menu in the chart to change between contaminants or choose to displaya plot of all contaminants.
    3. Click and drag to move the map if necessary.
    """)
    with open(stations_map_path, "r") as m:
        st.components.v1.html(m.read(), height=600)

if not contaminant_maps:
    st.warning("No contaminant maps found")
else:
    st.markdown("""
    # Timelapse Maps
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