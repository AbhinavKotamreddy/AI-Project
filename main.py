import openai

openai.api_key = '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'

def give_quote(modifier):
    prompt = "Give me a {modifier} quote"
    response = openai.Completion.create(engine="text-davinci-003",prompt=prompt, max_tokens=50, n=1, stop=None, temperature=0.5)
    quote = response.choices[0].text.strip()
    return quote

if __name__ == '__main__':
    modifier=input("Provide a modifier: ")
    quote= give_quote(modifier)
    print(quote)