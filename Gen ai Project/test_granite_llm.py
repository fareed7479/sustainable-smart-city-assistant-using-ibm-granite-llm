from granite_llm import granite_llm

prompt = "What are sustainable energy sources?"
response = granite_llm.ask(prompt)

with open("llm_response.txt", "w", encoding="utf-8") as f:
    f.write(response)
