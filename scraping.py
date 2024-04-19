import facebook
from textblob import TextBlob
import csv

# Token akses dari Facebook Developers
ACCESS_TOKEN = 'TOKEN'

# Inisialisasi klien Graph API
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version="3.1")

# ID Halaman atau Grup Facebook
group_id = 'ID-HALAMAN-ATAU-GROUP'

# Mengumpulkan postingan dari grup
posts = graph.get_object(id=group_id, fields='posts')['posts']['data']

# Membuka file CSV untuk menulis data
with open('sentiment_analysis.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Menulis header
    writer.writerow(['Postingan', 'Skor Sentimen', 'Sentimen'])
    
    for post in posts:
        if 'message' in post:
            message = post['message']
            # Analisis sentimen menggunakan TextBlob
            blob = TextBlob(message)
            sentiment_score = blob.sentiment.polarity
            
            sentiment = ''
            if sentiment_score > 0:
                sentiment = 'Positif'
            elif sentiment_score < 0:
                sentiment = 'Negatif'
            else:
                sentiment = 'Netral'
            
            # Menulis data ke file CSV
            writer.writerow([message, sentiment_score, sentiment])

print('Data telah disimpan dalam sentiment_analysis.csv')
