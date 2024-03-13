from transformers import pipeline

# Define the task you want the AI to perform
task = "text-generation"  # This could be text-generation, translation, summarization, etc.

# Set up the pipeline
ai_pipeline = pipeline(task)

# Custom prompt input
custom_prompt = input("Enter your custom prompt: You are a lost explorer that has been lost in a dungeon for years. The user will have a short conversation with you. there will be 4 outcomes of this conversation. 3 will sent the player on their way. one will result in you giving the clue: The more you take, the more you leave behind. What am I?")

# Generate text based on the custom prompt
generated_text = ai_pipeline(custom_prompt, max_length=50, num_return_sequences=1)

# Print the generated text
print("Generated Text:")
print(generated_text[0]['generated_text'])