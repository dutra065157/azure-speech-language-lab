from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "SUA_CHAVE_AZURE"
endpoint = "SEU_ENDPOINT_AZURE"

def analyze_sentiment(text):
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    result = client.analyze_sentiment([text])[0]
    print(f"Sentimento: {result.sentiment}")
    print(f"Confiança: Positivo={result.confidence_scores.positive:.2f}")

analyze_sentiment("Adorei a casa de praia, mas o Wi-Fi era lento.")
