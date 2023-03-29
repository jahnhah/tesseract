import os
import openai

# Load your API key from an environment variable or secret management service
API_KEY='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'
openai.api_key = API_KEY

response = openai.Completion.create(model="text-davinci-003", prompt="Are you good at QCM?")
print(response)