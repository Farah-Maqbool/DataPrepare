# 🧹 DataPrepare - Prepare your data for ML Algorithms

DataPrepare is a simple AI/ML tool that automatically preprocesses raw datasets for machine learning.  

It cleans data, handles missing values, encodes categorical features, scales numeric columns, and lets users download an ML-ready dataset — all in one click.

---

## 🚀 Features
✅ Upload raw CSV or Excel file  
✅ Automatic data type detection  
✅ Handle missing values  
✅ Encode categorical columns  
✅ Scale numeric features  
✅ Download cleaned dataset  
✅ Built with Streamlit (easy to use and deploy)

---

## 🧠 Tech Stack
- **Python**
- **Streamlit** – UI framework
- **pandas**, **scikit-learn** – preprocessing
- **FastAPI (optional)** – for backend logic (future)
- **SQLite (optional)** – for saving user history (future)

---

## 🗂️ Project Structure
auto-prep/
│
├── app.py # Streamlit UI
├── backend.py # Core preprocessing logic
├── requirements.txt # Dependencies
├── .gitignore # Ignored files
├── data/ # Sample datasets
└── README.md # Project documentation

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/<your-username>/auto-prep.git
cd auto-prep

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

4. Install dependencies
pip install -r requirements.txt

6. Run the app
streamlit run app.py

## 📊 Example Workflow
Upload your raw dataset (CSV or Excel).
The app automatically detects data types.
Missing values, encoding, and scaling are handled.
Download your cleaned, ML-ready dataset.

## 🧩 Future Enhancements
FastAPI backend integration
Auto EDA summary (visual insights)
Pipeline export (sklearn compatible)
User authentication & project history
Deployment on custom domain

## 👩‍💻 Author
Farah
AI/ML Engineer | Building end-to-end ML solutions
🌐 Portfolio: https://farahmaqbool.lovable.app/
💼 LinkedIn: https://www.linkedin.com/in/farah-maqbool/
