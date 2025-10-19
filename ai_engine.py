openai.api_key = "your-api-key-here"
def explain_bug(erroe_log:str) -> str:
  prompt = f"""
you are an AI Debugging Assistant. A User pasted this error log:
{error_log}
your task:
1. explain the bug in simple in english.
2.trace the cause-effect reasoning chian.
3.suggest a logic-aware fix using static analysis.
4.offer a teaching tip for new programmers.
respond clearly and concisely.
"""
  respones = openai.chatcompletion.create
  (
    model = "gpt-4",
    message =[{"role":"user","content":prompt}],
    temperature=0.7

)
return response['choices'][0]['message']['content']
  
