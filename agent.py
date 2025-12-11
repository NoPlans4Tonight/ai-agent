from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="your-api-key"
)

def ask_agent(prompt: str) -> str:
    print(f"Thinking about {prompt}...\n")

    response = client.chat.completions.create(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": "you are a financial research assistant helping with dividend stock analysis."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

def interact_with_agent():
    while True:
        user_input = input("Whats currently on your mind? (type 'exit' to quit) ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        response = ask_agent(user_input)
        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    print("💼 Dividend Research Agent")
    print("=" * 50)
    print("Ask me anything about dividend stocks!\n")
    interact_with_agent()