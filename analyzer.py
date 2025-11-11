import pandas as pd
from agent import analyze_with_agent

def analyze_dataset(file_path):
    df = pd.read_csv(file_path)
    
    # Basic info
    df_shape = df.shape
    df_dtypes = df.dtypes.apply(str).to_dict()
    df_missing = (df.isnull().mean() * 100).to_dict()
    df_duplicates = df.duplicated().sum()
    
    # Unique values
    df_unique_count = df.nunique().to_dict()
    
    # Top categorical values
    top_values = {}
    for col in df.select_dtypes(include='object'):
        top_values[col] = df[col].value_counts().head(10).to_dict()
    
    # Numeric description
    df_describe = df.describe().to_dict()
    
    # Outliers (IQR)
    outliers = {}
    for col in df.select_dtypes(include=['int64', 'float64']):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers[col] = df[(df[col] < lower) | (df[col] > upper)][col].count()
    
    # Correlation (flatten numeric correlations)
    corr = df.select_dtypes(include=['int64','float64']).corr().to_dict()
    
    # Constant columns
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    
    # Categorical cardinality
    cat_cardinality = df.select_dtypes(include='object').nunique().to_dict()
    
    # Memory usage in MB
    memory_usage_mb = round(df.memory_usage(deep=True).sum() / (1024**2), 2)
    
    summary = {
        "shape": df_shape,
        "dtypes": df_dtypes,
        "missing_percent": df_missing,
        "duplicate_rows": df_duplicates,
        "unique_counts": df_unique_count,
        "top_values": top_values,
        "numeric_describe": df_describe,
        "outliers": outliers,
        "correlation": corr,
        "constant_columns": constant_cols,
        "categorical_cardinality": cat_cardinality,
        "memory_usage_mb": memory_usage_mb
    }
    
    return summary

result = analyze_with_agent(analyze_dataset("data/sample_data.csv"))

print(result)