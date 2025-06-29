import requests
import logging
from config import settings

logging.basicConfig(level=logging.DEBUG)

class GraniteLLM:
    def __init__(self):
        self.api_key = settings.WATSONX_API_KEY
        self.base_url = settings.WATSONX_BASE_URL
        self.project_id = settings.WATSONX_PROJECT_ID
        self.model_id = settings.WATSONX_MODEL_ID
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def ask(self, prompt: str) -> str:
        url = f"{self.base_url}/ml/v2/infer"
        payload = {
            "model_id": self.model_id,
            "project_id": self.project_id,
            "input": prompt
        }
        try:
            logging.debug(f"Sending request to Granite LLM: {payload}")
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            logging.debug(f"Received response: {data}")
            if "results" in data and len(data["results"]) > 0:
                return data["results"][0]
            else:
                return "No response from LLM."
        except requests.RequestException as e:
            logging.error(f"Error communicating with Granite LLM: {str(e)}")
            return f"Error communicating with Granite LLM: {str(e)}"

granite_llm = GraniteLLM()
