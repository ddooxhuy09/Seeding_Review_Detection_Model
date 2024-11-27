import requests
import time
import random
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

# Cấu hình logging
logging.basicConfig(
    filename="crawler.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Cấu hình cookie và header
cookies = {
    '_trackity': 'b53bc421-3342-a446-ef6a-ef42abb221a4',
    '_hjSessionUser_522327': 'eyJpZCI6IjE2N2JjOTZiLWIzY2EtNWNiYi1hZTlhLTQ2OTdkMTVmMTE2YSIsImNyZWF0ZWQiOjE3MjcwMDE2Mzg4NDIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gcl_gs': '2.1.k1$i1731572846$u165506106',
    '_ga': 'GA1.1.85032210.1731572849',
    '_gcl_aw': 'GCL.1731572852.CjwKCAiA3Na5BhAZEiwAzrfagBplOkg6FJA3XgKuf0MCTe5chU2AMJ__R63SEjJyFwnvN0SHa1EydhoCBC4QAvD_BwE',
    '_gcl_au': '1.1.163346958.1731572852',
    '__uidac': '0166dc64e2c074618e1e56780bfbf93b',
    '__RC': '5',
    'dtdz': '_PID.1.80fbb29ab7da5184',
    '__utm': 'source=google|medium=cpc|campaign=SEA_NBR_GGL_PMA_DAP_ALL_VN_ALL_UNK_UNK_C.PMAX_X.21434089152_Y.167617706789_V._W.DT_A._O.CIR',
    '__iid': '749',
    '__su': '0',
    '__R': '3',
    '__tb': '0',
    '_fbp': 'fb.1.1731572853198.832251549424170266',
    '__IP': '1953478811',
    'delivery_zone': 'Vk4wNjcwMDcwMjY=',
    'tiki_client_id': '85032210.1731572849',
    'TOKENS': '{"access_token":"4MroWJz30U1EOAmH6NlifRg92DtyCnLI","expires_in":157680000,"expires_at":1889498334116,"guest_token":"4MroWJz30U1EOAmH6NlifRg92DtyCnLI"}',
    '_dtdcTime': '1731832572',
    '__adm_upl': 'eyJ0aW1lIjoxNzMxODM4MzQ4LCJfdXBsIjoiMC0yODU3MTk3NzgxMjA4OTI1MjkyIn0=',
    'cto_bundle': 'iKFgeF96azQ5eUtpQnlkdHZmc20lMkY5Y1NpWklFeE14eGRaVCUyQnd6bkxoZ0lJcGhBM2tXTCUyQmdEJTJCYWVpYmk0R0hma3pacEpjVnBZcmZDWkh5TEtWdjJaODJFS2dXZ3NsY3VCcWEzTzRXMURNaUFESE93JTNE',
    '__uif': '__uid:2857197781208925292|__ui:-1|__create:1731572851',
    'amp_99d374': 'LQ6BXKWR_CLE5K-oGpw9z1.MTc1OTU3MDY=..1ict4086o.1ict408pp.9b.ck.lv',
    '_ga_S9GLR1RQFJ': 'GS1.1.1731849125.12.0.1731849125.60.0.0'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': '9Fg8wT342xibyHJf6nYk5pXAzsSWPBvh',
    'Connection': 'keep-alive',
}

params_id = {
    'limit': '40',
    'include': 'advertisement',
    'aggregations': '2',
    'trackity_id': 'b53bc421-3342-a446-ef6a-ef42abb221a4',
    'page': '1',
    'category': '8322',}

params_data = {'platform': 'web'}

params_comment = {
    'sort': 'score|desc,id|desc,stars|all',
    'page': '1',
    'limit': '5',
    'include': 'comments,contribute_info,attribute_vote_summary'
}

session = requests.Session()  # Sử dụng session


# Hàm parser dữ liệu sản phẩm
def parser_product(json):
    return {
        'id': json.get('id'),
        'name': json.get('name'),
        'category': json.get('categories', {}).get('name'),
        'price': json.get('price'),
        'original_price': json.get('original_price'),
        'description': json.get('description'),
        'number_sold': json.get('quantity_sold', {}).get('value'),
        'number_reviews': json.get('review_count'),
        'source': 'tiki.vn'
    }


# Hàm parser dữ liệu comment
def parser_comment(json, product_id):
    return {
        'id': json.get('id'),
        'product_id': product_id,
        'content': json.get('content'),
        'rating': json.get('rating'),
        'user_id': json.get('created_by', {}).get('id'),
        'post_time': json.get('timeline', {}).get('post_time'),
        'update_time': None,
        'source': 'tiki.vn'
    }

# Hàm parser dữ liệu user
def parser_user(json):
    return {
        'id': json.get('id'),
        'name': json.get('name'),
        'full_name': json.get('full_name'),
        'source': 'tiki.vn'
    }


# Hàm lấy ID sản phẩm
def crawl_product_id():
    product_id_set = set()
    for page in range(1, 11):
        params_id['page'] = page
        try:
            response = session.get('https://tiki.vn/api/v2/products', headers=headers, params=params_id)
            response.raise_for_status()
            data = response.json().get('data', [])
            product_id_set.update(record.get('id') for record in data)
            logging.info(f"Fetched page {page} with {len(data)} products")
        except Exception as e:
            logging.error(f"Error fetching page {page}: {e}")
        time.sleep(random.uniform(1, 3))  # Giảm thời gian chờ
    return list(product_id_set)


# Hàm crawl dữ liệu sản phẩm với retry


# Kết nối tới cụm Cassandra
def connect_to_cassandra():
    cluster = Cluster(['localhost'])  # Thay thế bằng host Cassandra của bạn
    session = cluster.connect()
    session.set_keyspace('ai_spam_detection')
    return session

# Hàm chèn dữ liệu sản phẩm vào Cassandra
def insert_product(session, product):
    insert_query = """
    INSERT INTO product (id, name, category, price, original_price, description, number_sold, number_reviews, source)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    session.execute(insert_query, (
        product['id'], product['name'], product['category'], product['price'],
        product['original_price'], product['description'], product['number_sold'],
        product['number_reviews'], product['source']
    ))

# Hàm chèn dữ liệu comment vào Cassandra
def insert_comment(session, comment):
    insert_query = """
    INSERT INTO comment (id, user_id, product_id, comment_dl, star_rating, post_time, update_time, source)
    VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
    """
    session.execute(insert_query, (comment['id'], comment['user_id'], comment['product_id'], comment['content'], 
                                   comment['rating'], comment['post_time'], comment['update_time'], comment['source']
    ))

# Hàm chèn dữ liệu user vào Cassandra
def insert_user(session, user):
    insert_query = """
    INSERT INTO user (id, name, full_name, source)
    VALUES (%s, %s, %s,%s)
    """
    session.execute(insert_query, (
        user['id'], user['name'], user['full_name'], user['source']
    ))

# Hàm crawl dữ liệu sản phẩm với retry
def crawl_product(pid):
    retry_count = 3
    while retry_count > 0:
        try:
            response = session.get(f'https://tiki.vn/api/v2/products/{pid}', headers=headers, params=params_data)
            response.raise_for_status()
            return parser_product(response.json())
        except Exception as e:
            logging.error(f"Error fetching product ID {pid}: {e}")
            retry_count -= 1
            time.sleep(random.uniform(2, 4))
    return None

# Sử dụng đa luồng để crawl dữ liệu sản phẩm
def crawl_product_data(product_ids, cassandra_session):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(crawl_product, pid): pid for pid in product_ids}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Crawling Product Data"):
            data = future.result()
            if data:
                insert_product(cassandra_session, data)


# Crawl dữ liệu comment với đa luồng
def crawl_product_comments(product_ids, cassandra_session):
    def fetch_comments(pid):
        for page in range(1, 3):
            params_comment['product_id'] = pid
            params_comment['page'] = page
            try:
                response = session.get('https://tiki.vn/api/v2/reviews', headers=headers, params=params_comment, cookies=cookies)
                response.raise_for_status()
                data = response.json().get('data', [])
                for comment in data:
                    comment_data = parser_comment(comment, pid)
                    insert_comment(cassandra_session, comment_data)
                    user_data = parser_user(comment.get('created_by', {}))
                    insert_user(cassandra_session, user_data)
            except Exception as e:
                logging.error(f"Error fetching comments for product ID {pid}, page {page}: {e}")
            time.sleep(random.uniform(1, 2))

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_comments, pid): pid for pid in product_ids}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Crawling Comments"):
            future.result()

def main():
    print("Crawling Product IDs...")
    product_ids = crawl_product_id()
    print(f"Found {len(product_ids)} product IDs")

    cassandra_session = connect_to_cassandra()

    print("Crawling Product Data...")
    crawl_product_data(product_ids, cassandra_session)

    print("Crawling Comments...")
    crawl_product_comments(product_ids, cassandra_session)

    cassandra_session.shutdown()

if __name__ == "__main__":
    main()