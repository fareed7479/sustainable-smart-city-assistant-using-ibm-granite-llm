from granite_llm import granite_llm
import pandas as pd

class ReportGenerator:
    def __init__(self):
        self.llm = granite_llm

    def generate_report(self, kpi_data: pd.DataFrame) -> str:
        # Prepare a summary prompt based on KPI data
        summary_text = kpi_data.describe().to_string()
        prompt = (
            "You are an AI assistant generating a sustainability report based on the following KPI data summary:\n"
            f"{summary_text}\n"
            "Please provide a concise and insightful sustainability report."
        )
        response = self.llm.ask(prompt)
        return response

report_generator = ReportGenerator()
