
# 🌍 COVID-19 Data Dashboard & Analysis

This project provides a detailed exploratory data analysis and an interactive dashboard for global COVID-19 data using the [Our World in Data](https://ourworldindata.org/covid-cases) dataset.

## 📌 Project Objectives

- Load, clean, and preprocess COVID-19 data.
- Analyze and visualize trends in cases, deaths, vaccinations, and hospitalizations.
- Build an interactive dashboard with Streamlit for dynamic country/date selection.
- Provide actionable insights and visual storytelling.

## 🛠️ Tools & Libraries Used

- **Python 3**
- **pandas** — data manipulation
- **matplotlib / seaborn** — static visualizations (in Jupyter)
- **plotly** — interactive charts in Streamlit
- **streamlit** — dashboard app framework
- **Jupyter Notebook** — report and EDA

## 🚀 How to Run the Project

1. Clone/download the repository.
2. Ensure the dataset `owid-covid-data.csv` is present in the same directory.
3. Run the Streamlit app with the following command:

```bash
streamlit run covid dashboard.py
```

You can also open the `covid (1).ipynb` notebook to explore the data analysis and insights.

## 💡 Key Insights

- The **US and India** recorded the highest total cases.
- **Vaccination rates** varied significantly across countries, highlighting global disparities.
- **ICU and hospital patient trends** can indicate the pressure on healthcare systems during surges.
- Lower reported cases in some countries may reflect **testing/reporting limitations**, not necessarily fewer infections.

---

Created with ❤️ for data storytelling and public health awareness.
