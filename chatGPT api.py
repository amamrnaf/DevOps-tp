import openai 


openai.api_key = "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"


response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system","content":"you are an airline client service employee,you answer some commonely asked questions,do not break character,answers must not surpass 300 letters"},
              {"role":"user","content":"hello what is the stuff i cannot carry with me on the plane"}]
)
print(response.choices[0].message.content)


