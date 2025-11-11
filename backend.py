# backend.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

def execute_preprocessing(df: pd.DataFrame, decisions: dict):
    """
    Execute preprocessing actions based on agent decisions.
    Supports multiple actions per column.
    
    df: original pandas dataframe
    decisions: dict returned by agent + user overrides
    """
    df_processed = df.copy()
    action_log = {}

    for col, col_decision in decisions["columns"].items():
        actions = col_decision.get("actions", [])
        action_log[col] = {"actions": actions, "reasons": col_decision.get("reasons", [])}

        for action in actions:
            # Skip if action is none
            if action in ["none", "keep"]:
                continue

            # --- Imputation ---
            if action == "fill_median":
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    df_processed[col] = df_processed[col].fillna(df_processed[col].median())
            elif action == "fill_mean":
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    df_processed[col] = df_processed[col].fillna(df_processed[col].mean())
            elif action == "fill_mode":
                df_processed[col] = df_processed[col].fillna(df_processed[col].mode()[0])
            elif action == "fill_unknown":
                df_processed[col] = df_processed[col].fillna("Unknown")

            # --- Drop column ---
            elif action == "drop":
                df_processed = df_processed.drop(columns=[col])
                break  # stop further actions for this column

            # --- Encoding ---
            elif action == "one_hot":
                df_processed = pd.get_dummies(df_processed, columns=[col], drop_first=False)
                # Convert boolean columns to int (0/1)
                for c in df_processed.select_dtypes(include='bool').columns:
                    df_processed[c] = df_processed[c].astype(int)
                break  # column replaced, stop further actions
            elif action == "label":
                le = LabelEncoder()
                df_processed[col] = le.fit_transform(df_processed[col].astype(str))

            # --- Scaling ---
            elif action in ["standard", "minmax"]:
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    scaler = StandardScaler() if action == "standard" else MinMaxScaler()
                    df_processed[col] = scaler.fit_transform(df_processed[[col]])

            # --- Outlier Handling ---
            elif action == "drop_outliers":
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    Q1 = df_processed[col].quantile(0.25)
                    Q3 = df_processed[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower = Q1 - 1.5 * IQR
                    upper = Q3 + 1.5 * IQR
                    df_processed = df_processed[(df_processed[col] >= lower) & (df_processed[col] <= upper)]
            elif action == "cap_outliers":
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    Q1 = df_processed[col].quantile(0.25)
                    Q3 = df_processed[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower = Q1 - 1.5 * IQR
                    upper = Q3 + 1.5 * IQR
                    df_processed[col] = df_processed[col].clip(lower, upper)

            # --- Feature Engineering ---
            elif action == "log_transform":
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    df_processed[col] = np.log1p(df_processed[col])
            elif action == "sqrt_transform":
                if pd.api.types.is_numeric_dtype(df_processed[col]):
                    df_processed[col] = np.sqrt(df_processed[col])
            elif action.startswith("interaction_term"):
                # Could implement interaction term logic here if needed
                pass

    return df_processed, action_log
