# 📊 AI-Powered Sri Lanka Tourism Demand & Market Intelligence Forecaster

An interactive, multi-dimensional predictive analytics web application built using **Python**, **Streamlit**, and **Advanced Machine Learning**. This platform transforms historical, multi-variable tourism inflow statistics into actionable predictive intelligence, providing macroeconomic analysts, hospitality stakeholders, and corporate data teams with an automated forecasting workflow.

🔗 **Live Deployment Link:** [View Live Application](https://sl-tourism-predictor-6b8lidpm9g2kpvyxgpmby2.streamlit.app/)

---

## 🚀 Technical Features

* **Structural Data Transmutation:** Reshapes multi-year wide matrix formats into dynamic, time-series compliant tidy records using advanced data wrangling frameworks.
* **Random Forest Regressor Architecture:** Implements a non-linear ensemble machine learning pipeline via `Scikit-Learn` to extract and learn country-specific growth trajectories.
* **Categorical Feature Vectorization:** Executes structural One-Hot Encoding (`pd.get_dummies`) to dynamically map text-based national identities into algorithmic binary matrices.
* **Persistent Model Optimization:** Leverages serialization utilities (`Pickle`) to decouple training heavy-lifting from front-end interface processes, achieving sub-second operational execution.

---

## 🏛️ Macroeconomic Frameworks & Predictive Metrics Explained

The dashboard computes and visualizes critical pillars of national economic performance, functioning as a real-time sovereign analytics tool:

### 1. Market-Wise Sovereign Inflows (Tourist Arrivals)
* **Mathematical Objective:** $f(\text{Year}, \text{Country Vector}) \rightarrow \hat{y} \text{ (Projected Arrivals)}$
* **Economic Significance:** Acts as a leading volume indicator for the foreign currency reserve generation pipeline. In macroeconomic planning, localized volume projections drive structural capacity management within aviation networks, hospitality infrastructure, and regional employment distribution frameworks.

### 2. Random Forest Regression Ensemble
* **Algorithmic Mechanics:** Constructs a meta-estimator that fits $N$ independent decision tree regressors in parallel over bootstrapped training sub-samples.
* **Predictive Value:** By aggregating multi-tree variances via democratic averaging, the architecture minimizes overfitting and accurately models severe structural macroeconomic shifts—such as the rapid industry recovery curves following historical global interruptions.

### 3. One-Hot Category Matrix Mapping
* **Mathematical Definition:** $$\mathbf{x}_{\text{country}} \in \{0, 1\}^K \text{ where } \sum_{i=1}^{K} x_i = 1$$
* **Data Engineering Significance:** Ensures zero numerical rank bias during learning iterations. Converting sparse nominal fields into independent binary arrays prevents the algorithm from misinterpreting text inputs as ordinal steps, validating spatial accuracy across separate geopolitical source markets.

---

## 🤖 Data Analysis & Engineering Workflow

This application implements a complete, end-to-end Data Analysis Lifecycle, making it an enterprise-grade case study for Data Analysis and Predictive Modeling roles:

### 1. Data Ingestion & Structural Reshaping
* Aggregated authentic multi-year national arrival records published by the **Sri Lanka Tourism Development Authority (SLTDA)**.
* Utilized Pandas `.melt()` operations to pivot cross-tabulated periodic column matrices down into unified, time-series index rows suited for regression processing.

### 2. Vectorization & Feature Engineering
* Built isolated pipeline arrays by mapping nominal text labels to explicit binary vectors, maintaining a deterministic schema footprint.
* Extracted and enforced explicit timestamp integer structures to empower the regressor with temporal trend perception across multi-year cycles.

### 3. Supervised Machine Learning Pipeline
* Segmented chronological structural elements into feature parameters ($X$) and label boundaries ($y$).
* Instantiated an ensemble of decision trees with randomized feature splits to evaluate baseline performance indicators, evaluating predictive convergence via Root Mean Squared Error (RMSE) and $R^2$ variance markers.

### 4. Model Optimization & Persistence Pipelines
* Implemented serialization mechanisms to freeze trained algorithmic parameter weights directly into localized binary payloads (`.pkl`).
* Exported explicit array metadata shapes to guarantee total matrix alignment during real-time web-application interface operations.

### 5. Streamlit Executive Dashboard Implementation
* Abstracted deep matrix operations behind an intuitive, human-centered presentation layer using **Streamlit**.
* Formatted computed numeric forecasts into scaled, localized comma-separated integer objects to enable rapid business decision-making.

---

## 🛠️ Future Enhancement Plan

To upgrade this platform into an enterprise-ready intelligence suite, the following roadmap has been established:

### 1. Advanced Time-Series Modeling
* Integrate deep sequence networks such as **Prophet** or **LSTM (Long Short-Term Memory)** to map complex month-on-month seasonality patterns that standard regressors miss.

### 2. Macroeconomic & Exogenous Feature Integration
* Expand the feature matrix by incorporating external economic indicators such as global inflation rates, currency exchange rate fluctuations ($USD \rightarrow LKR$), and changing aviation fuel cost matrices.

### 3. Automated Data Pipelines
* Establish a live ETL (Extract, Transform, Load) pipeline using **Apache Airflow** or **GitHub Actions** to automatically fetch and update the model as soon as new monthly records are published by the SLTDA.

### 4. Market Sentiment & External Insights Dashboard
* Incorporate NLP (Natural Language Processing) models to scrape and analyze travel forums and social media sentiment metrics, providing a qualitative layer to numerical inflow forecasts.

---

## 📦 Tech Stack Used

* **Language:** Python 3.11+
* **Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning Engine:** Scikit-Learn (`ensemble.RandomForestRegressor`)
* **Serialization Protocols:** Pickle

---

## 🔧 Installation & Local Setup

Follow these steps to run the web application locally on your machine:

### 1. Clone the repository:
```bash
git clone [https://github.com/methmi2004/SL-Tourism-Predictor.git](https://github.com/methmi2004/SL-Tourism-Predictor.git)
cd SL-Tourism-Predictor
```
### 2. Install required dependencies:
pip install streamlit pandas numpy scikit-learn

### 3. Run the Streamlit application:
streamlit run app.py
