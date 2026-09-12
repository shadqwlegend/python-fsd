n=int(input("enter the number of question"))
temp=[0.0,0.7,1.4]
for i in range(n):
  question=input("enter the question:")
  result = ask_llm(question,system_prompt="Answer in at most 2 points",temperature=temp[i])
  print(result.choices[0].message.content)
  print("  Prompt tokens:", result.usage.prompt_tokens)
  print("  Completion tokens:", result.usage.completion_tokens)
  print("  Total tokens:", result.usage.total_tokens)