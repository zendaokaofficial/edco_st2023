import altair as alt
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math
import numpy as np 

def main():
    sheet_id = "1QsP2rfSIC5TkpqNpsccigQHO5ydps2msozFKmsoNCXk"
    
    source = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=1607729660")    
    source["ID SLS"] = source["ID SLS"].astype(str)
    source["Kode Provinsi"] = source["Kode Provinsi"].astype(str).str.zfill(2)
    source["Kode Kab/Kota"] = source["Kode Kab/Kota"].astype(str).str.zfill(2)
    source["Kode Kecamatan"] = source["Kode Kecamatan"].astype(str).str.zfill(3)
    source["Kode Desa"] = source["Kode Desa"].astype(str).str.zfill(3)
    source["Kode SLS"] = source["Kode SLS"].astype(str).str.zfill(6)
    
    source3 = source
    source2 = source3[source3["Waktu"].notnull()]

    source2 = source2[source2["Status"] == "Dikembalikan ke Koseka"]
    source2.loc[:,"Waktu"] = pd.to_datetime(source2["Waktu"], format = "%m/%d/%Y")

    source2["Waktu Saat ini"] = np.datetime64('today')

    source2["Lama Pengembalian"] = source2["Waktu Saat ini"] - source2["Waktu"]

    source4 = source2.loc[:,["Nama Kecamatan", "Nama Desa", "Nama SLS", "Nama Koseka", "Nama PML", "Waktu", "Lama Pengembalian"]].reset_index(drop=True)
    source4["Lama Pengembalian"] = source4["Lama Pengembalian"].dt.days

    st.subheader("Dokumen Dikembalikan")

    st.dataframe(source4, use_container_width=True)

if __name__ == "__main__":
    main()
