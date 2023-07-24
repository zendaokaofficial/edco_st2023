import altair as alt
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math

def main():
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    sheet_id = "1QsP2rfSIC5TkpqNpsccigQHO5ydps2msozFKmsoNCXk"
    source = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=1607729660")
    
    source["ID SLS"] = source["ID SLS"].astype(str)

    source["Kode Provinsi"] = source["Kode Provinsi"].astype(str).str.zfill(2)
    source["Kode Kab/Kota"] = source["Kode Kab/Kota"].astype(str).str.zfill(2)
    source["Kode Kecamatan"] = source["Kode Kecamatan"].astype(str).str.zfill(3)
    source["Kode Desa"] = source["Kode Desa"].astype(str).str.zfill(3)
    source["Kode SLS"] = source["Kode SLS"].astype(str).str.zfill(6)

    ## Date
    source2 = source.iloc[:,[0,1,2,3,4,5,6,7,8,9,14,15,18]]
    source2.fillna('', inplace=True)
    
    lstPetugas = list(source["Petugas Edcod"].unique())
    lstPetugas.insert(0, "PILIH PETUGAS EDCOD")

    lstPetugas = [x for x in lstPetugas if str(x) != 'nan']

    Filter = st.selectbox("Nama Petugas Edcod", lstPetugas, 0)
    if Filter != "PILIH PETUGAS EDCOD":
        source3 = source2[source2["Petugas Edcod"] == Filter]
        source3.reset_index(drop=True, inplace=True)
        #source3 = source3.reset_index()

        #source3.index = source3.index + 1
        st.dataframe(source3, use_container_width=True)
        csv = convert_df(source3)

        st.download_button(
            "Press to Download",
            csv,
            f"Progress Editing Coding {datetime.now().day}{datetime.now().month}{datetime.now().year}_{datetime.now().minute}{datetime.now().second}.csv",
            "text/csv",
            key='download-csv'
        )
    else:
        st.dataframe(source2, use_container_width=True)
        csv = convert_df(source2)

        st.download_button(
            "Press to Download",
            csv,
            f"Progress Editing Coding {datetime.now().day}{datetime.now().month}{datetime.now().year}_{datetime.now().minute}{datetime.now().second}.csv",
            "text/csv",
            key='download-csv'
        )

if __name__ == "__main__":
    main()
