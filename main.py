from news_scraper import NewsScraper
from news_summarizer import NewsSummarizer
from dict_to_html import DictToHtml
from datetime import datetime

# Get news (list) from Ansa.it using NewsScraper

ansa_scraper = NewsScraper('https://www.ansa.it', selector='h3.title')
news = ansa_scraper.get_titles()
# Summarize news using NewsSummarizer

summarizer_prompt = """
genera la stringa corrispondente al dizionario python con categoria
di notizie come chiave e riassunto organico delle notizie della
categoria come valore.
scrivi solo il dizionario, il primo carattere del tuo output deve
essere l'inizio del dizionario e l'ultimo carattere del tuo output
deve essere l'ultimo carattere del dizionario. Non mettere backticks.
Non lasciare dettagli ma non essere nemmeno troppo prolisso.
queste sono le notizie: """ + '\n'.join(news)

summarizer = NewsSummarizer(
    news,
    'gemini-2.5-flash',
    summarizer_prompt,
    'api_key'
)
categories = summarizer.categorize_and_summarize_titles()

# Generate html from categories (dict) using DictToHtml

today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

DictToHtml(
    categories,
    'it', 'ANSA.it AI Overview',
    'https://rubensabatini.com', 'by Ruben Sabatini',
    f'Riassunto delle notizie di Ansa.it di oggi {today_date} fatto da Google Gemini',
    'index.html', 'style.css'
).generate_html()
