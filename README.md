# 🧹 DataPrepare - AI-Powered Data Preprocessing for ML

DataPrepare is an AI/ML tool that automatically preprocesses raw datasets for machine learning.  

It cleans data, handles missing values, encodes categorical features, scales numeric columns, and lets users download an ML-ready dataset — all in one click. The MVP uses smart automation to make preprocessing decisions based on dataset analysis, and integrate an LLM agent to suggest actions interactively.

## 🚀 Features
✅ Upload raw CSV or Excel file   
✅ Automatic data type detection  
✅ Handle missing values intelligently  
✅ Encode categorical columns  
✅ Scale numeric features  
✅ user overrides for preprocessing decisions  
✅ Download cleaned dataset  
✅ Built with Streamlit for easy usage and deployment

## 🧠 Tech Stack
- **Python**
- **Streamlit** – UI framework
- **pandas**, **scikit-learn** – data preprocessing
- **LLM Agent** – interactive agent for smart decisions

## 🗂️ Project Structure
DataPrepare/ <br>
│
├── app.py # Streamlit UI <br>
├── backend.py # Core preprocessing engine <br>
├── analyzer.py # Dataset analyzer (summary stats, missing %, types) <br>
├── agent.py # LLM agent / orchestrator logic <br>
├── requirements.txt # Dependencies <br>
├── .gitignore # Ignored files <br>
├── data/ # Sample datasets <br>
│ └── sample.csv <br>
├── utils/ # Helper functions (pipeline export, logging) <br>
│ └── export_pipeline.py <br>
└── README.md # Project documentation 


## ⚙️ Setup Instructions

### 1. Clone the repository

git clone <repo-link> <br>
cd DataPrepare 

### 2. Create a virtual environment
python -m venv venv <br>
source venv/bin/activate   # Mac/Linux <br>
venv\Scripts\activate      # Windows 

### 3. Install dependencies
pip install -r requirements.txt 

### 4. Run the app
streamlit run app.py 

## 📊 Example Workflow
User uploads CSV → Show loading spinner <br>
Analyzer runs → Shows summary sections: <br>
• Data shape + columns <br>
• Missing % per column <br>
• Unique values (top few) <br>
• Outliers count <br>
• Correlation summary <br>
• Duplicate count
📊 Display all in simple expandable sections in Streamlit <br>
Send summary to LLM Agent → Agent analyzes and returns preprocessing plan <br>
UI shows plan table <br>
User clicks Confirm → Backend executes plan → Show progress + “Download Processed CSV” <br>

## Limitations
•	Input: CSV only, ~50k rows / 50 cols <br>
•	Data types: Numeric, categorical, boolean <br>
•	Analysis: Only statistical summaries, missing %, unique values, correlation, duplicates, outliers (simple) <br>
•	Agent decisions: Imputation, encoding, scaling, simple outlier treatment, basic feature engineering <br>
•	Backend: Executes only agent-approved actions <br>
•	Visualizations: Minimal (mostly tables) <br>
•	Exclusions for MVP: <br>
    o	Large datasets (>50k rows) <br>
    o	Complex feature engineering <br>
    o	Charts, plots (optional later) <br>
    o	NLP, images, or time series special preprocessing <br>
    o	Multi-dataset support


## 🧩 Future Enhancements
Auto EDA summary (visual insights) <br>
Preprocessing pipeline export (sklearn compatible) <br>
User authentication & project history <br>
FastAPI backend for large dataset processing <br>
Deployment on a custom domain 

## Author
Farah <br>
AI/ML Engineer | Building end-to-end ML solutions <br>
🌐 Portfolio: https://farahmaqbool.lovable.app/ <br>
💼 LinkedIn: https://www.linkedin.com/in/farah-maqbool/