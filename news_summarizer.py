from google import genai
import ast

class NewsSummarizer:

    def __init__(self, news: list, model_name, prompt, api_key):
        self.news = news
        self.model_name = model_name
        self.prompt = prompt
        self.api_key = api_key

    def categorize_and_summarize_titles(self) -> dict:
        client = genai.Client(api_key=self.api_key)
        while True:
            try:
                response = client.models.generate_content(
                    model=self.model_name,
                    contents=self.prompt,
                )
                categories = ast.literal_eval(response.text)
                return categories
    
            except Exception as e:
                print(f'Failed with: {e}, retrying...')
