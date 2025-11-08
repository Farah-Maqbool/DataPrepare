# 🧹 DataPrepare - AI-Powered Data Preprocessing for ML

DataPrepare is an AI/ML tool that automatically preprocesses raw datasets for machine learning.  

It cleans data, handles missing values, encodes categorical features, scales numeric columns, and lets users download an ML-ready dataset — all in one click. The MVP uses smart automation to make preprocessing decisions based on dataset analysis, and future versions will integrate an LLM agent to suggest actions interactively.

## 🚀 Features
✅ Upload raw CSV or Excel file   
✅ Automatic data type detection  
✅ Handle missing values intelligently  
✅ Encode categorical columns  
✅ Scale numeric features  
✅ Optional user overrides for preprocessing decisions  
✅ Download cleaned dataset  
✅ Built with Streamlit for easy usage and deployment

## 🧠 Tech Stack
- **Python**
- **Streamlit** – UI framework
- **pandas**, **scikit-learn** – data preprocessing
- **OpenAI / LLM API (future)** – interactive agent for smart decisions
- **FastAPI (optional)** – backend logic for larger datasets
- **SQLite (optional)** – for saving user project history

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
Upload your raw dataset (CSV or Excel). <br>
The app automatically analyzes the dataset. <br>
Missing values, encoding, and scaling are handled automatically. <br> 
Optional: override agent suggestions for each column. <br>
Download your cleaned, ML-ready dataset. 

## 🧩 Future Enhancements
LLM agent integration for interactive preprocessing decisions <br>
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