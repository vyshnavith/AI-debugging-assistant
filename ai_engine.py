openai.api_key = "your-api-key-here"
def explain_bug(erroe_log:str) -> str:
  prompt = f"""
you are an AI Debugging Assistant. A User pasted this error log:
{error_log}
your task:
1.Pinpoint the exact line and variable where the error occurred.
2. explain the bug in simple in english.
3.show the corrected version of that line with reasoning.
4.suggest a full fix if needed.
5.offer a teaching tip for new programmers.
respond clearly and concisely.
"""
  respones = openai.chatcompletion.create
  (
    model = "gpt-4",
    message =[{"role":"user","content":prompt}],
    temperature=0.7

)
return response['choices'][0]['message']['content']
