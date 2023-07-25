import altair as alt
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math

def main():
    sheet_id = "1QsP2rfSIC5TkpqNpsccigQHO5ydps2msozFKmsoNCXk"
    
    source = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=1607729660")    
    source["ID SLS"] = source["ID SLS"].astype(str)
    source["Kode Provinsi"] = source["Kode Provinsi"].astype(str).str.zfill(2)
    source["Kode Kab/Kota"] = source["Kode Kab/Kota"].astype(str).str.zfill(2)
    source["Kode Kecamatan"] = source["Kode Kecamatan"].astype(str).str.zfill(3)
    source["Kode Desa"] = source["Kode Desa"].astype(str).str.zfill(3)
    source["Kode SLS"] = source["Kode SLS"].astype(str).str.zfill(6)
    
    source3 = source.groupby(["Nama Koseka", "Nama PML"])['Rating'].mean()
    source3 = source3.reset_index()
    source3 = source3.sort_values("Rating")
    source3["Rating"] = source3["Rating"].apply(lambda x : round(x,2))
    
    x = alt.Chart(source3).encode(
        x='Rating',
        y='Nama PML',
        text='Rating',
        color=alt.condition(
            alt.datum.Rating < 6,
            alt.value("orange"),  # The positive color
            alt.value("green")  # The negative color
        )
    ).properties(
        width=200,
        height=1800
    )
    
    d = x.mark_bar() + x.mark_text(align='left', dx=6)
    st.altair_chart(d, use_container_width=True)

if __name__ == "__main__":
    main()
