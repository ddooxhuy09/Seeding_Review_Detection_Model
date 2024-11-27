from flask import Flask, request, render_template, send_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():   
    product_url = request.form['product_url']
    review_url = product_url.replace("dp", "product-reviews") + "?pageNumber=1"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36', 
        'Accept-Language': 'en-US, en;q=0.5'
    }
    
    review_list = []
    resp = requests.get(review_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'data-hook': "review"})
    
    for item in reviews:
        review = {
            'id': uuid.uuid4(),
            'review_title': item.find('a', {'data-hook': "review-title"}).text.strip(),
            'rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
            'review_body': item.find('span', {'data-hook': 'review-body'}).text.strip()
        }
        review_list.append(review)
    
    df = pd.DataFrame(review_list)
    df.to_csv('amazon_reviews.csv', index=False, encoding='utf-8')
    
    return send_file('amazon_reviews.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
