import os
import cohere
from utils.fetch_content import get_text_from_url
from utils.tts import synthesize_speech
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def load_prompt(template_path, variables):
    with open(template_path, "r") as file:
        prompt = file.read()
    for key, val in variables.items():
        prompt = prompt.replace("{" + key + "}", val)
    return prompt

def call_cohere(prompt):
    response = co.chat(
        model='command',
        message=prompt,  # Pass prompt as direct string
        temperature=0.7
    )
    return response.text.strip()

def main():
    url = input("Enter a URL to simplify: ")
    raw_text = get_text_from_url(url)

    simplify_prompt = load_prompt("prompts/simplify.txt", {"input": raw_text})
    simplified = call_cohere(simplify_prompt)

    Path("outputs").mkdir(exist_ok=True)
    with open("outputs/summary.txt", "w") as f:
        f.write(simplified)
    print("✅ Simplified text saved to outputs/summary.txt")

    narrate = input("Generate audio narration? (y/n): ")
    if narrate.lower() == "y":
        synthesize_speech(simplified, "outputs/narration.mp3")
        print("🔊 Audio narration saved to outputs/narration.mp3")

if __name__ == "__main__":
    main()