import requests
from bs4 import BeautifulSoup
import json
import uuid
import logging

def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={"class": "a-offscreen"}).string.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={"class": "a-offscreen"}).string.strip()
        except:
            price = ""
    return price

def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", {'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating

# def total_pages(product_url, headers):
#     resp = requests.get(product_url, headers=headers)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     reviews = soup.find('div', {'data-hook': "cr-filter-info-review-rating-count"})
#     return int(reviews.text.strip().split(', ')[1].split(" ")[0].replace(",", ""))

def extract_reviews(review_url, headers):
    review_list = []
    resp = requests.get(review_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'data-hook': "review"})
    for item in reviews:
        review = {
            'username': item.find("span", {"class": "a-profile-name"}).text.strip(),
            'review_title': item.find('a', {'data-hook': "review-title"}).text.strip(),
            'rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
            'review_body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
        }
        review_list.append(review)
    return review_list

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36', 
        'Accept-Language': 'en-US, en;q=0.5'
    }

    reviews_data = []

    product_url = "https://www.amazon.com/BENGOO-G9000-Controller-Cancelling-Headphones/dp/B0982NYVQV/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.zHoOmh6S7kPeAkWr3bmSFujzmFyXR34ww0ALkmBYjkXhagdAxOb3Y7aZTuAeIHwIF_qzPLTafg14p05y5PYY-uHzX2_ciOG67H0XZ_9tAdt3AKRC6HzSEtie8T4KjId0Vx_kLy2c9QX2ncsOPH7quKmttStTWxHed4cG5NIILD5ICSvcv2EAu06J45jZ0xSRrcJ0H3QZ3IakZdH1559wSDD7S0lVJmFZ_vWRbF-hqZw.n-4GV3Upn3UaSUXWYRfEaPRd8z5wpDaVyhgKkvBBeYc&dib_tag=se&keywords=gaming%2Bheadsets&pd_rd_r=bd5ed9d3-3573-4446-8d81-d7375181a15e&pd_rd_w=7ksi8&pd_rd_wg=mg6oK&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=8X28HGF3RM76XBTSNJ2K&qid=1730012048&sr=8-1&th=1"
    
    webpage = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    product_title = get_title(soup)
    product_price = get_price(soup)
    product_rating = get_rating(soup)
    
    for i in range(1, 11):
        print(f"Running for page {i} of product {product_title}")
        try:
            review_url = product_url.replace("dp", "product-reviews") + f"?pageNumber={i}"
            reviews = extract_reviews(review_url, headers)
            reviews_data.extend(reviews)
        except Exception as e:
            print(e)

    # Save reviews data to JSON file
    output_data = {
        'product_title': product_title,
        'product_price': product_price,
        'product_rating': product_rating,
        'reviews': reviews_data
    }

    with open('product_reviews.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
