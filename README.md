# Climate Change Analysis Dashboard (Week 0 Challenge)

A comprehensive data science project that transforms raw NASA POWER atmospheric data into an interactive monitoring tool. This project analyzes climate risk across **Ethiopia, Sudan, Kenya, Nigeria, and Tanzania**.

---

## 📸 Final Dashboard Overview
![Single View](visualization/figure1%28single%20view%29.png)

![Regional Comparison](visualization/regional_comparison.png)

*Figure 1: The "Single Country View" featuring the high-contrast Blue-White theme.*
*Figure 2: The "regional comparative analysis" featuring the high-contrast Blue-White theme.*

---

## 🛠️ Project Evolution (Task-Based Development)
This repository followed a structured development lifecycle, preserved in individual task branches:

### **Task 1: EDA & Data Cleaning Pipeline**
- **Branch:** `task-1-eda`
- **Scope:** In-depth Exploratory Data Analysis for 5 countries.
- **Process:** Cleaned raw meteorological data, handled missing values, and standardized date formats.
- **Output:** Individual country CSVs in `data/cleaned_data/`.

![EDA Results](visualization/EDA.png)


### **Task 2: Regional Comparison & Data Merging**
- **Branch:** `task-2-merging`
- **Scope:** Statistical merging of datasets.
- **Process:** Performed cross-country comparisons of temperature and rainfall volatility using a master pivot-table approach.
- **Output:** `data/master_climate_data.csv`.

![Comparative View](visualization/figure2%20%28Comparative%20view%29.png)


### **Task 3: Interactive Dashboard Development**
- **Branch:** `task-3-dashboard`
- **Scope:** Frontend engineering with Streamlit.
- **Process:** Implemented a full-black "Control Room" UI with Plotly visualizations.

![Regional Comparison](visualization/regional_comparison.png)

---

## Repository Structure
```text
climate-challenge-week0/
├── app/
│   └── main.py                 # Final Streamlit Application
├── data/
│   ├── raw_data/               # Task 1: Original NASA POWER files
│   ├── cleaned_data/           # Task 1: Processed CSVs
│   └── master_climate_data.csv # Task 2: Final Merged Dataset
├── images/
│   └── dashboard_dark_mode.png # README visual assets
├── notebooks/
│   ├── ethiopia_eda.ipynb      # EDA Notebooks
│   ├── ...                     # (Kenya, Nigeria, Sudan, Tanzania)
│   └── comparison_analysis.ipynb # Task 2: Comparative Logic
├── .gitignore                  # Exclusion of venv/ and cache files
└── requirements.txt            # Project Dependencies

🚀 Key Technical Features
***High-Contrast UI:*** Customized CSS and Plotly layouts for a pitch-black background with blue-white data visibility.

***Vulnerability Context:*** Integrated policy-driven insights regarding the Addis Ababa Declaration for regional climate adaptation.

***Comparative Analytics:*** Dedicated module for visualizing rainfall standard deviation and temperature hotspots.

⚙️ How to Run Locally
Clone & Enter:

Bash
git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
cd climate-challenge-week0
Environment Setup:

Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Bash
streamlit run app/main.py


🧑‍🔬 Author
Sinen Dirirsa / computer science major at AAU
10 Academy week-0 challenge