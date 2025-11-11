import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv
import numpy as np

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-chat-v3-0324"

def convert_to_json_safe(obj):
    if isinstance(obj, dict):
        return {k: convert_to_json_safe(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_json_safe(v) for v in obj]
    elif isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)
    elif isinstance(obj, (np.bool_)):
        return bool(obj)
    elif pd.isna(obj):
        return None
    else:
        return obj

def analyze_with_agent(dataset_summary: dict):
    """
    Send dataset summary to LLM (DeepSeek via OpenRouter)
    to decide preprocessing actions + generate explanations.
    Supports multiple actions per column.
    """
    if not OPENROUTER_API_KEY:
        raise ValueError("Missing OpenRouter API key. Set OPENROUTER_API_KEY in environment.")

    prompt = f"""
You are an intelligent AI data preprocessing agent.

You are given a dataset summary in JSON. Your job is to decide preprocessing actions for each column
and explain your reasoning. You may return multiple actions per column, in the order they should be applied.

Allowed actions:
- Missing value handling: 'drop', 'fill_median', 'fill_mean', 'fill_mode', 'fill_unknown'
- Encoding: 'one_hot', 'label'
- Scaling: 'standard', 'minmax'
- Outlier handling: 'drop_outliers', 'cap_outliers'
- Feature engineering: 'none', 'log_transform', 'sqrt_transform', 'interaction_term'
- Drop columns: 'drop' (only if constant or >50% missing)

Return valid JSON like this:

{{
  "columns": {{
    "ColumnName": {{
      "actions": ["fill_mean", "standard", "cap_outliers"],
      "reasons": [
        "5% missing numeric values; suitable for mean imputation.",
        "Scale after imputation for consistency.",
        "Cap extreme values to reduce outlier effect."
      ]
    }},
    "Category": {{
      "actions": ["fill_unknown", "one_hot"],
      "reasons": [
        "Missing categorical values filled as 'Unknown'.",
        "Convert to numerical representation."
      ]
    }}
  }},
  "global_actions": {{
    "scaling": "standard",
    "feature_engineering": ["none"]
  }}
}}

Now analyze this dataset summary and decide accordingly:
{json.dumps(convert_to_json_safe(dataset_summary), indent=2)}
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a data preprocessing decision maker."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"LLM API Error: {response.status_code} - {response.text}")

    result = response.json()
    message = result["choices"][0]["message"]["content"]

    try:
        decisions = json.loads(message)
    except json.JSONDecodeError:
        start = message.find("{")
        end = message.rfind("}") + 1
        decisions = json.loads(message[start:end])

    return decisions
