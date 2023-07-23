import altair as alt
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math

def main():
    st. set_page_config(layout="wide")
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    sheet_id = "1QsP2rfSIC5TkpqNpsccigQHO5ydps2msozFKmsoNCXk"
    source = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=1607729660")
    source = source.iloc[:,[14,15,18]]
    source = source[source["Petugas Edcod"].notnull()].reset_index()

    ## Date
    a = datetime.now()
    b = datetime(2023, 7, 1, 0, 0, 0, 0)
    subs = a - b
    target = math.floor(subs.days/30 * 2000)
    dftarget = pd.DataFrame({'target':[target]})

    c = alt.Chart(source).mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3
    ).encode(
        x='sum(Jumlah L2):Q',
        y='Petugas Edcod',
        color = 'Status'
    ).configure_range(
        category=alt.RangeScheme(['#fdc086', '#7fc97f'])
    ).configure_legend(
        orient='top'
    ).properties(
        width=200,
        height=600
    )

    rule = alt.Chart(dftarget).mark_rule(color='black').encode(
        x='mean(target):Q'
    ).properties(
        width=200,
        height=600
    )

    ## Olah Data
    source_new = source.groupby(['Petugas Edcod', 'Status']).agg({'Jumlah L2':'sum'})
    #source_new = source_new.set_index(['Petugas Edcod', 'Status'])

    source_new2 = source_new.unstack(level=-1).reset_index().fillna(0)
    source_new2.columns = ["Petugas Edcod", "Dikembalikan ke Koseka", "Selesai Editing Coding"]
    source_new2.index = source_new2.index + 1
    source_new2["Jumlah L2"] = source_new2["Dikembalikan ke Koseka"] + source_new2["Selesai Editing Coding"]

    st.altair_chart(c, use_container_width=True)
    st.dataframe(source_new2, use_container_width=True)

    csv = convert_df(source_new2)

    st.download_button(
        "Press to Download",
        csv,
        f"Progress Editing Coding {datetime.now().day}{datetime.now().month}{datetime.now().year}_{datetime.now().minute}{datetime.now().second}.csv",
        "text/csv",
        key='download-csv'
    )

if __name__ == "__main__":
    main()
