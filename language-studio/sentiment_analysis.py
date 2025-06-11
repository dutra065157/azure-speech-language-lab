from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "F0EZ7qWYWK5bsLs4cifRdvY1k9bIwBtGT0za3IJ9Fy4qyEgNUUA4JQQJ99BFACYeBjFXJ3w3AAAaACOGHTnI"
endpoint = "eastus"

def analyze_sentiment(text):
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    result = client.analyze_sentiment([text])[0]
    print(f"Sentimento: {result.sentiment}")
    print(f"Confiança: Positivo={result.confidence_scores.positive:.2f}")

analyze_sentiment("Adorei a casa de praia, mas o Wi-Fi era lento.")
