import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

def main():
    st.set_page_config(
        page_title="Dashboard IPM VS Konsumsi Alkohol",
        layout="centered"
    )

    st.markdown("# Korelasi Indeks Pembangunan Manusia (IPM) dan Konsumsi Alkohol Per Kapita")
    st.markdown("## Pendahuluan")
    st.markdown("Indeks Pembangunan Manusia (IPM) seringkali digunakan sebagai indikator untuk mengukur kualitas hidup manusia pada suatu negara. Sedangkan mengonsumsi minuman beralkohol berlebihan diketahui dapat memberikan dampat negatif bagi kesehatan dan psikis seseorang")
    st.markdown("Maka dari itu, muncul suatu pertanyaan:")
    st.markdown("##### _\"Apakah terdapat hubungan antara konsumsi alkohol terhadap IPM negara Indonesia?\"_")
    st.markdown("Analisis hubungan IPM dengan konsumsi alkohol dapat memberikan _insight_ yang berharga bagi negara Indonesia untuk meningkatkan Indeks Pembangunan Manusia atau IPM.")


    st.markdown("## Apa Itu Indeks Pembangunan Manusia?")
    st.markdown(
        "Dikutip dari Badan Pusat Statistik (BPS), IPM menjelaskan bagaimana penduduk dapat mengakses hasil pembangunan dalam memperoleh pendapatan, kesehatan, pendidikan, dan sebagainya."
    )
    st.markdown("## Data dan Tren")
    st.markdown("Seluruh data bersumber dari Badan Pusat Statistik dan dapat dipertanggungjawabkan. Link sumber : https://www.bps.go.id/")
    st.markdown("Mari mulai memahami tren dengan melihat visualisasi data dari tahun ke tahun.")

    options = ["Indeks Pembangunan Manusia (IPM)", "Konsumsi Alkohol di Perkotaan (L/kapita)", "Konsumsi Alkohol di Pedesaan (L/kapita)", "Konsumsi Alkohol di Perkotaan dan Pedesaan (L/kapita)"]
    visualization = st.selectbox(
        label = "Pilih opsi",
        options = options
    )

    df = pd.read_excel("./dataset_2.xlsx", sheet_name="Sheet1", header=0)
    df["Tahun"] = df["Tahun"].astype(str)
    # df["Tahun"] = pd.to_datetime(df["Tahun"])
    df.set_index("Tahun", inplace=True)
    # st.dataframe(df) 
    df = df.iloc[:, :].astype("float64")
    # df.info()

    df_reset_index = df.reset_index()
    for i in range(len(options)):
        if visualization == options[i]:
            # st.line_chart(df.iloc[:, i])
            y_label = "index" if i == 0 else "L/Kapita"
            chart = (
                alt.Chart(
                    data=df_reset_index,
                    title=options[i],
                )
                .mark_line()
                .encode(
                    x=alt.X("Tahun", axis=alt.Axis(title="Tahun", labelAngle=0)),
                    y=alt.Y(df_reset_index.columns[i+1], axis=alt.Axis(title=y_label))
                )
            )
            st.altair_chart(chart, use_container_width=True)

    st.markdown("##### Insight:")
    st.markdown("1. Terlihat bahwa IPM terus meningkat dari tahun 2015-2022")
    st.markdown("2. Terlihat bahwa di perkotaan, volume konsumsi alkohol fluktuatif dari tahun 2015-2018, tetapi terus menurut setelah tahun 2018.")
    st.markdown("3. Terlihat bahwa di pedesaan, volume konsumsi fluktuatif dari tahun 2015 - 2017, tetapi kembali berkurang setelah tahun 2017.")
    st.markdown("4. Terlihat bahwa di perkotaan dan pedesaan, volume konsumsi alkohol fluktuatif dari tahun 2015-2017, tetapi kembali berkurang setelah tahun 2017.")

    corr_matrix = df.corr()
    
    # Create a heatmap using seaborn
    fig, ax = plt.subplots(figsize=(10, 8))
    heatmap = sns.heatmap(corr_matrix, annot=True, 
    cmap="coolwarm", fmt=".2f", ax=ax, annot_kws={"fontsize": 20})


    st.markdown("## Uji Korelasi")
    st.markdown("Uji korelasi berguna dalam analisis data untuk memahami hubungan antara variabel-variabel dan dapat memberikan wawasan tentang pola atau tren yang ada dalam data. Korelasi Positif artinya meningkatnya satu variabel cenderung diikuti dengan meningkatnya variabel yang lain. Sedangkan, korelasi negatif artinya meningkatnya satu variabel cenderung diikuti dengan menurunnya variabel lain.")
    st.markdown("Hubungan statistik antara Indeks Pembangunan Manusia (IPM) dengan konsumsi alkohol dapat dicari dengan menggunakan uji korelasi")
    st.markdown("### Heatmap Korelasi Indeks Pembangunan Manusia (IPM) dan Konsumsi Alkohol")
    ax.set_title("Korelasi Indeks Pembangunan Manusia dengan Konsumsi Alkohol di Desa/Kota", fontdict={"fontsize": 16})

    met_1, met_2, met_3 = st.columns(3)
    # with met_1:
    #     st.metric("Di Pedesaan", round(corr_matrix.iloc[0, 1], 2))
    # with met_2:
    #     st.metric("Di Perkotaan", round(corr_matrix.iloc[0, 2], 2))
    # with met_3:
    #     st.metric("Keseluruhan", round(corr_matrix.iloc[0, 3], 2))


    met_1, met_2, met_3 = st.columns(3)

    # Define custom CSS styling for metrics
    style = """
        .metric-container {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .metric-label {
            font-size: 16px;
            color: #888888;
        }
    """

    # Apply the custom CSS styling
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

    with met_1:
        st.markdown(
            f'<div class="metric-container">'
            f'<div class="metric-value">{round(corr_matrix.iloc[0, 1], 2)}</div>'
            f'<div class="metric-label">Di Pedesaan</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with met_2:
        st.markdown(
            f'<div class="metric-container">'
            f'<div class="metric-value">{round(corr_matrix.iloc[0, 2], 2)}</div>'
            f'<div class="metric-label">Di Perkotaan</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with met_3:
        st.markdown(
            f'<div class="metric-container">'
            f'<div class="metric-value">{round(corr_matrix.iloc[0, 3], 2)}</div>'
            f'<div class="metric-label">Keseluruhan</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    
    st.markdown("##### Insight:")
    
    st.markdown("Secara keseluruhan, dapat disimpulkan bahwa ada korelasi negatif antara konsumsi alkohol dengan Indeks Pembangunan Manusia.")

    heatmap.set_xticklabels(heatmap.get_xticklabels(), fontdict={"fontsize": 12})
    
    heatmap.set_yticklabels(heatmap.get_yticklabels(), fontdict={"fontsize": 12})


    ax.set_title("Korelasi Indeks Pembangunan Manusia dengan Konsumsi Alkohol di Desa/Kota")

    df_normalized = df / df.max()
    # st.dataframe(df_normalized)

    st.pyplot(fig)


    st.markdown("# Perubahan Tahunan Ternormalisasi")
    st.markdown("Sekarang mari kita lihat bagaimana perubahan IPM dengan konsumsi alkohol secara bersamaan.")
    perkotaan = st.checkbox("Perkotaan", value=True)
    pedesaan = st.checkbox("Pedesaan", value=True)
    perkotaan_dan_pedesaan = st.checkbox("Perkotaan dan Pedesaan", value=False)

    active = [0]
    
    if perkotaan:
        active.append(1)
    if pedesaan:
        active.append(2)
    if perkotaan_dan_pedesaan:
        active.append(3)
    st.line_chart(df_normalized.iloc[:, active])
    st.markdown("##### Insight:")
    st.markdown("Terlihat bahwa jarak antara konsumsi alkohol dan IPM cenderung membesar, terutama setelah tahun 2017 dan 2018 sehingga memperlihatkan korelasi negatif.")

    st.markdown("## Kesimpulan")
    st.markdown("Hasil analisis korelasi menunjukkan bahwa memang terdapat hubungan statistik antara konsumsi alkohol terhadap IPM suatu negara. Konsumsi alkohol yang lebih kecil cenderung diikuti dengan kenaikan Indeks Pembangunan Manusia di negara Indonesia")

if __name__ == "__main__":
    main()
