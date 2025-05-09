
import os
import cohere
secret_key = os.getenv("secret_key")  # Returns None if not set
print("Secret value:", secret_key)

co = cohere.ClientV2(secret_key)

# Add the user message
message = "My name is Riaz Khan"

# Create a custom system message
system_message="""## Task and Context
Generate concise responses, with maximum one-sentence."""
messages = [{'role': 'system', 'content': system_message},
              {'role': 'user', 'content': message}]
x=10
while x:
  

  # Generate the response
  response = co.chat(model="command-a-03-2025",
                    messages=messages)
  
  print(response.message.content[0].text)
  user_input = input("Enter something: ")
  r=response.message.content+[user_input]
  # Add the messages
  messages.append({'role': 'assistant', 'content': r})
  x-=1