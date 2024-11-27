import re
import requests

def parser_product(json):
    item = json.get('data', {}).get('item', {})
    models = item.get('models', [{}])
    sold = models[0].get('sold', 0) if models else 0
    return {
        'id': item.get('item_id'),
        'name': item.get('title'),
        'category': item.get('categories', [{}])[0].get('display_name'),
        'price': item.get('price'),
        'original_price': item.get('price_before_discount'),
        'description': item.get('description'),
        'number_sold': sold,
        'number_reviews': item.get('cmt_count'),
        'source': 'shopee.vn'
    }

url = "https://shopee.vn/S%C3%A1ch-C%C3%A2y-Cam-Ng%E1%BB%8Dt-C%E1%BB%A7a-T%C3%B4i-(Nh%C3%A3-Nam-HCM)-i.404602141.9338588760?sp_atk=bb05aab0-83ef-45f0-98e2-3fa581c0568a&xptdk=bb05aab0-83ef-45f0-98e2-3fa581c0568a"

# Biểu thức chính quy để trích xuất shop_id và item_id
match = re.search(r'i\.(\d+)\.(\d+)', url)
if match:
    shop_id = match.group(1)
    item_id = match.group(2)
    print(f"shop_id: {shop_id}")
    print(f"item_id: {item_id}")

    # Tạo URL API
    api_url = f"https://shopee.vn/api/v4/pdp/get_pc"
    
    # Định dạng cookie thành JSON
    cookies = {
        'SPC_F': '2S3KdUqD98a12Fd6801BC52Ukx5HrNG3',
        'REC_T_ID': '450d9347-6f33-11ef-b5da-a24986d58f89',
        '_QPWSDCXHZQA': 'ebce5646-6bf2-4a8c-a17d-6a531d25a7d9',
        'REC7iLP4Q': 'cf764513-b639-4c6b-a608-6572fc8d39fc',
        '_gcl_au': '1.1.24672565.1725945147',
        '_fbp': 'fb.1.1726031734168.371161192420180184',
        '_hjSessionUser_868286': 'eyJpZCI6ImM2YzM3YzUwLTY0ZGYtNTcwMC05Y2I5LTFiMDYxOTc2MjEyZCIsImNyZWF0ZWQiOjE3MjYzODQwODI2MjUsImV4aXN0aW5nIjp0cnVlfQ==',
        'SPC_CLIENTID': 'MlMzS2RVcUQ5OGExtbatucezehrhbixl',
        'SC_DFP': 'gZVXyFkUCNzakraqYPaoDSOroVIRUjSu',
        '_ga_3XVGTY3603': 'GS1.1.1727058732.1.0.1727058740.52.0.0',
        '_fbc': 'fb.1.1730008816413.PAZXh0bgNhZW0CMTEAAaYfKB0dlgKbYZHGZoq-MuFuiJ6LW9ZlUu7V909MYYBTyp1Qt1lefLOOsco_aem_K-MS_qAdzQ242sPRdVKyIg',
        '_gcl_gs': '2.1.k1$i1730389170$u260663631',
        '_gcl_aw': 'GCL.1730389173.Cj0KCQjw1Yy5BhD-ARIsAI0RbXZYbRfoEH-xN6C4O-QxOLYHk8puzGy0mTGb2B4yTULs7nLB0IN3jjYaAg8pEALw_wcB',
        '_gac_UA-61914164-6': '1.1730389174.Cj0KCQjw1Yy5BhD-ARIsAI0RbXZYbRfoEH-xN6C4O-QxOLYHk8puzGy0mTGb2B4yTULs7nLB0IN3jjYaAg8pEALw_wcB',
        'SPC_EC': '.WGdvYzBuOVcxdzVwekxqbDAgAOwyhdSUOdkAn87ZnnLXLP88BeqiZO4m06vExjhsbEk4969diBzUt0xiwr/F88g4BexAZyIxcg4p1C+ZPlXpT6ai3c77Uh4JzZM4RmBJD+agfNn0k2HGoKf8nlBy+RK7QWljHqI6CAQExSVoMoP+xCDaZf+4byz3ZWleFfcor0HohLMiCTn7wHVrOkCS2ltIPt7sEWm2TH+zuPnFGdNZTdBc3Tp7O+pdesNlw5Q5',
        'SPC_ST': '.WGdvYzBuOVcxdzVwekxqbDAgAOwyhdSUOdkAn87ZnnLXLP88BeqiZO4m06vExjhsbEk4969diBzUt0xiwr/F88g4BexAZyIxcg4p1C+ZPlXpT6ai3c77Uh4JzZM4RmBJD+agfNn0k2HGoKf8nlBy+RK7QWljHqI6CAQExSVoMoP+xCDaZf+4byz3ZWleFfcor0HohLMiCTn7wHVrOkCS2ltIPt7sEWm2TH+zuPnFGdNZTdBc3Tp7O+pdesNlw5Q5',
        'SPC_U': '1011065965',
        'SPC_R_T_ID': 'n6godyiA7ffjcoQXAG5WG3Rt2M6UpaAeaT9aUFXHAM8/y0W2RLMxNGYv08y8JuSSVl1MlIZTATG0uprUem6KS9oaaxxmbWAdcKWyGNvlCZ8Gfj/GgONBS5y9Dl+QBk0RKbv9FmAzV5K2O+N4kvgywO/DHBeaXntRFF1M2aWEugs=',
        'SPC_R_T_IV': 'THhJRGt4cEV3UkhWM2d3Uw==',
        'SPC_T_ID': 'n6godyiA7ffjcoQXAG5WG3Rt2M6UpaAeaT9aUFXHAM8/y0W2RLMxNGYv08y8JuSSVl1MlIZTATG0uprUem6KS9oaaxxmbWAdcKWyGNvlCZ8Gfj/GgONBS5y9Dl+QBk0RKbv9FmAzV5K2O+N4kvgywO/DHBeaXntRFF1M2aWEugs=',
        'SPC_T_IV': 'THhJRGt4cEV3UkhWM2d3Uw==',
        '__LOCALE__null': 'VN',
        'SPC_SEC_SI': 'v1-NHc0cnJQb3BwTW5POERnSwD/runhQXzXnskh4TLCrH/MlZD0dGD3fR4pvXFWTJkpoJkGPuwb8Cuu26VySWV5yE/txi4uezwM+LO4yOG0NaM=',
        'SPC_SI': 'u8I1ZwAAAAA5N0FVTkg1ZBeRKgAAAAAAOVJOQW1wRnY=',
        'csrftoken': 'giuznsmTNxKcI8xJEW3m6l0Ew3h4qnOz',
        '_sapid': '219f78693e20360fcdbf486a2f34ba8831843163849c7484e73d06ce',
        'SPC_IA': '1',
        '_gid': 'GA1.2.1389408610.1732036185',
        'SPC_CDS_CHAT': 'ce8edd5d-96d9-4fbc-a422-96f1a3dde780',
        '_med': 'refer',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_ga': 'GA1.1.265873742.1726200588',
        '_dc_gtm_UA-61914164-6': '1',
        '_hjSession_868286': 'eyJpZCI6IjdiMWVhNDU1LTY3NTUtNDg3MC04MWE1LTFhZTVlNmZhZmFiYSIsImMiOjE3MzIxMTgyMjU2MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        '_ga_4GPP1ZXG63': 'GS1.1.1732118225.69.1.1732118248.37.0.0',
        'shopee_webUnique_ccd': 'nuMVs3ZtjTfDQMg7mlLTpA%3D%3D%7CxdxDuSXsInRzp1f0KWLZ%2FvhH0tmf8nI3Va8Ft3QUZtFs2%2B4qyQ4lqbkk05cqKBASPqobnNlEydom3CNR4L8%3D%7CQJfdHUyolWcfqihE%7C08%7C3',
        'ds': '6b8b3721b5f373d64a87db084b35d47f'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://shopee.vn/S%C3%A1ch-Combo-2-cu%E1%BB%91n-T%C6%B0-Duy-Ng%C6%B0%E1%BB%A3c-T%C6%B0-Duy-M%E1%BB%9F-Nguy%E1%BB%85n-Anh-D%C5%A9ng-SBOOKS-i.182607782.22374558225?sp_atk=4f30bb44-c035-4537-a3c1-e197d6847313&xptdk=4f30bb44-c035-4537-a3c1-e197d6847313',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'x-api-source': 'pc',
        'x-csrftoken': 'giuznsmTNxKcI8xJEW3m6l0Ew3h4qnOz',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '6d193e676318733f1dfc7b36050159b9d3792d7a1808b8105255',
        'x-sap-sec': '6LhePgGQ3aOuMCmuBaIrBlJujaJGBZLuL7I5BwcugaIOBb8u7aJABzmu5aIHBbUuSSIjBzcu+15jBaUuR7JUBzeuk7IpByFuLS5CBwJu6aIRBZJuRaJ5Bb3uR1IuBxJuPa5wBGhuLaJrBbcufaIWBYmuBaI6BCFuBaJuBzHSBbHCE5cuBaJuBZ2Mc0KoE1J96JwqJOaLYaeuBj09SKjbBSJuzahuBiEIE/tuBaI6saeuByJtBaIwB7Ju0OL591JuciLNBSJudbPd30mtBaI1WkBeoahuBGctBa5Ap+c9BaJuBtFqBaJuBaJp1dJ3l1JuBgFNB7JuGrIfLkJtBaICqkfsdVe5RKEZvJCzB1Ju1aeuBg+73mWuB1Juvw4Gz4HEXvKrkwNYGvpWFuv34o6PMAK1STTP1+WzH/iimcVdOJmzJg7Kq9JTCkWHKVtljPihlPyGHwLAozidHmdzRzZYEPQ/Rukg1pOePQuUUoal4nBJFfXEYNHwN7su4lU81hL87Ms+z5Do0rTBkcU8+Ir6Jwy10MFtHNumzfvM11JXIDWCM/gxZ3QS/Ce6KrqnzUKnxJlZZgVq6+U5iKTLMzwshXjtci8HxZZePdrRjlyz99B6U+jC0kqcq7bKZ8bQI6PhvSpT7FR9N1OKnH2qxvj2Gw9D91XIbnkdOD+3pQSQpZAyyAO1k7+Wdlm6OhMdYxpbSXyqT1+hHJOZXe9XlrzhSozyhR7ON2UGaaMnDt6AEyZh7eeNTXjrn26GMa8dPGzMoKdr3sRjYQ5eL6OdF4Ny7cVdTaBDOSroEPUXBaJulQSMmw3NKnViBaJuQ19vCsLkRCLoZNKJzKbMx2sK+IYR98DbRoIWyVSjnHg9cqSKjx8ETtiwpXz/Ue/K9029LsUABOUccUN0XgT3613DOiTK/g8rJ5e1QTvILqoiL1kFBBq4vpt7/Ylj039Er58fC6UsbLnB7l13mYXA7uIiczCTAu59NSD/OA48bJywyPSyTrOSc1YZajcLvtspVWtKtmawkMW/BaJuMaJuBZY5/QmVBaJug0rJA1ZuBaJaSwfikheOIHsROY/TH1JuB7JuBGevBaJVBaJukxJjQ7JuBaJvBaJuEEJuQHMKo1IhBaJuh1Lk7eCH/3sLBxUc7sFM/heu03ZBhwgjs/3zcbCHkxWRoufvrhcM0qfkK638/GMTMaZcK2v507MbSuxvkGOfr1fk06ZXKt89cSflP2ULoveYc2xx+3K1kGn+O2LcepxAcnJuBaJuBaJuBaJu7aJuBb/NJHOTHxlVcElzPoWL06nv21mYrLm5Rb3I5qhjLvE1chDZOoW72YZzHuLbrtJhkqOc5Vs8EL8jBaJuBaFuBa56dMgdqqMgHvcuBaJb2aGadt/QraWN503jovxVcxDnc0C60uJb07tCdtEBrHh5NoJuBaJuB7JuBwG6BaJuBaJu+aJuBxQ9pLKMPbvd',
        'x-shopee-language': 'vi',
        'x-sz-sdk-version': '1.12.8'
    }

    params = {
        'item_id': item_id,
        'shop_id': shop_id,
        'tz_offset_minutes': '420',
        'detail_level': '0',
    }
    
    # Gửi yêu cầu GET đến API với cookie, headers và params
    response = requests.get(api_url, cookies=cookies, headers=headers, params=params)
    
    # In ra toàn bộ phản hồi JSON
    if response.status_code == 200:
        print(response.json())
        product_info = parser_product(response.json())
        print(product_info)
    else:
        print(f"Yêu cầu thất bại với mã lỗi: {response.status_code}")
else:
    print("Không tìm thấy kết quả")

url = "https://shopee.vn/S%C3%A1ch-C%C3%A2y-Cam-Ng%E1%BB%8Dt-C%E1%BB%A7a-T%C3%B4i-(Nh%C3%A3-Nam-HCM)-i.404602141.9338588760?sp_atk=bb05aab0-83ef-45f0-98e2-3fa581c0568a&xptdk=bb05aab0-83ef-45f0-98e2-3fa581c0568a"

# Biểu thức chính quy để trích xuất shop_id và item_id
match = re.search(r'i\.(\d+)\.(\d+)', url)
if match:
    shop_id = match.group(1)
    item_id = match.group(2)
    print(f"shop_id: {shop_id}")
    print(f"item_id: {item_id}")

    # Tạo URL API
    api_url = f"https://shopee.vn/api/v4/pdp/get_pc"
    
    # Định dạng cookie thành JSON
    cookies = {
        'SPC_F': '2S3KdUqD98a12Fd6801BC52Ukx5HrNG3',
        'REC_T_ID': '450d9347-6f33-11ef-b5da-a24986d58f89',
        '_QPWSDCXHZQA': 'ebce5646-6bf2-4a8c-a17d-6a531d25a7d9',
        'REC7iLP4Q': 'cf764513-b639-4c6b-a608-6572fc8d39fc',
        '_gcl_au': '1.1.24672565.1725945147',
        '_fbp': 'fb.1.1726031734168.371161192420180184',
        '_hjSessionUser_868286': 'eyJpZCI6ImM2YzM3YzUwLTY0ZGYtNTcwMC05Y2I5LTFiMDYxOTc2MjEyZCIsImNyZWF0ZWQiOjE3MjYzODQwODI2MjUsImV4aXN0aW5nIjp0cnVlfQ==',
        'SPC_CLIENTID': 'MlMzS2RVcUQ5OGExtbatucezehrhbixl',
        'SC_DFP': 'gZVXyFkUCNzakraqYPaoDSOroVIRUjSu',
        '_ga_3XVGTY3603': 'GS1.1.1727058732.1.0.1727058740.52.0.0',
        '_fbc': 'fb.1.1730008816413.PAZXh0bgNhZW0CMTEAAaYfKB0dlgKbYZHGZoq-MuFuiJ6LW9ZlUu7V909MYYBTyp1Qt1lefLOOsco_aem_K-MS_qAdzQ242sPRdVKyIg',
        '_gcl_gs': '2.1.k1$i1730389170$u260663631',
        '_gcl_aw': 'GCL.1730389173.Cj0KCQjw1Yy5BhD-ARIsAI0RbXZYbRfoEH-xN6C4O-QxOLYHk8puzGy0mTGb2B4yTULs7nLB0IN3jjYaAg8pEALw_wcB',
        '_gac_UA-61914164-6': '1.1730389174.Cj0KCQjw1Yy5BhD-ARIsAI0RbXZYbRfoEH-xN6C4O-QxOLYHk8puzGy0mTGb2B4yTULs7nLB0IN3jjYaAg8pEALw_wcB',
        'SPC_EC': '.WGdvYzBuOVcxdzVwekxqbDAgAOwyhdSUOdkAn87ZnnLXLP88BeqiZO4m06vExjhsbEk4969diBzUt0xiwr/F88g4BexAZyIxcg4p1C+ZPlXpT6ai3c77Uh4JzZM4RmBJD+agfNn0k2HGoKf8nlBy+RK7QWljHqI6CAQExSVoMoP+xCDaZf+4byz3ZWleFfcor0HohLMiCTn7wHVrOkCS2ltIPt7sEWm2TH+zuPnFGdNZTdBc3Tp7O+pdesNlw5Q5',
        'SPC_ST': '.WGdvYzBuOVcxdzVwekxqbDAgAOwyhdSUOdkAn87ZnnLXLP88BeqiZO4m06vExjhsbEk4969diBzUt0xiwr/F88g4BexAZyIxcg4p1C+ZPlXpT6ai3c77Uh4JzZM4RmBJD+agfNn0k2HGoKf8nlBy+RK7QWljHqI6CAQExSVoMoP+xCDaZf+4byz3ZWleFfcor0HohLMiCTn7wHVrOkCS2ltIPt7sEWm2TH+zuPnFGdNZTdBc3Tp7O+pdesNlw5Q5',
        'SPC_U': '1011065965',
        'SPC_R_T_ID': 'n6godyiA7ffjcoQXAG5WG3Rt2M6UpaAeaT9aUFXHAM8/y0W2RLMxNGYv08y8JuSSVl1MlIZTATG0uprUem6KS9oaaxxmbWAdcKWyGNvlCZ8Gfj/GgONBS5y9Dl+QBk0RKbv9FmAzV5K2O+N4kvgywO/DHBeaXntRFF1M2aWEugs=',
        'SPC_R_T_IV': 'THhJRGt4cEV3UkhWM2d3Uw==',
        'SPC_T_ID': 'n6godyiA7ffjcoQXAG5WG3Rt2M6UpaAeaT9aUFXHAM8/y0W2RLMxNGYv08y8JuSSVl1MlIZTATG0uprUem6KS9oaaxxmbWAdcKWyGNvlCZ8Gfj/GgONBS5y9Dl+QBk0RKbv9FmAzV5K2O+N4kvgywO/DHBeaXntRFF1M2aWEugs=',
        'SPC_T_IV': 'THhJRGt4cEV3UkhWM2d3Uw==',
        '__LOCALE__null': 'VN',
        'SPC_SEC_SI': 'v1-NHc0cnJQb3BwTW5POERnSwD/runhQXzXnskh4TLCrH/MlZD0dGD3fR4pvXFWTJkpoJkGPuwb8Cuu26VySWV5yE/txi4uezwM+LO4yOG0NaM=',
        'SPC_SI': 'u8I1ZwAAAAA5N0FVTkg1ZBeRKgAAAAAAOVJOQW1wRnY=',
        'csrftoken': 'giuznsmTNxKcI8xJEW3m6l0Ew3h4qnOz',
        '_sapid': '219f78693e20360fcdbf486a2f34ba8831843163849c7484e73d06ce',
        'SPC_IA': '1',
        '_gid': 'GA1.2.1389408610.1732036185',
        'SPC_CDS_CHAT': 'ce8edd5d-96d9-4fbc-a422-96f1a3dde780',
        '_med': 'refer',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_ga': 'GA1.1.265873742.1726200588',
        '_dc_gtm_UA-61914164-6': '1',
        '_hjSession_868286': 'eyJpZCI6IjdiMWVhNDU1LTY3NTUtNDg3MC04MWE1LTFhZTVlNmZhZmFiYSIsImMiOjE3MzIxMTgyMjU2MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        '_ga_4GPP1ZXG63': 'GS1.1.1732118225.69.1.1732118248.37.0.0',
        'shopee_webUnique_ccd': 'nuMVs3ZtjTfDQMg7mlLTpA%3D%3D%7CxdxDuSXsInRzp1f0KWLZ%2FvhH0tmf8nI3Va8Ft3QUZtFs2%2B4qyQ4lqbkk05cqKBASPqobnNlEydom3CNR4L8%3D%7CQJfdHUyolWcfqihE%7C08%7C3',
        'ds': '6b8b3721b5f373d64a87db084b35d47f'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://shopee.vn/S%C3%A1ch-Combo-2-cu%E1%BB%91n-T%C6%B0-Duy-Ng%C6%B0%E1%BB%A3c-T%C6%B0-Duy-M%E1%BB%9F-Nguy%E1%BB%85n-Anh-D%C5%A9ng-SBOOKS-i.182607782.22374558225?sp_atk=4f30bb44-c035-4537-a3c1-e197d6847313&xptdk=4f30bb44-c035-4537-a3c1-e197d6847313',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'x-api-source': 'pc',
        'x-csrftoken': 'giuznsmTNxKcI8xJEW3m6l0Ew3h4qnOz',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '6d193e676318733f1dfc7b36050159b9d3792d7a1808b8105255',
        'x-sap-sec': '6LhePgGQ3aOuMCmuBaIrBlJujaJGBZLuL7I5BwcugaIOBb8u7aJABzmu5aIHBbUuSSIjBzcu+15jBaUuR7JUBzeuk7IpByFuLS5CBwJu6aIRBZJuRaJ5Bb3uR1IuBxJuPa5wBGhuLaJrBbcufaIWBYmuBaI6BCFuBaJuBzHSBbHCE5cuBaJuBZ2Mc0KoE1J96JwqJOaLYaeuBj09SKjbBSJuzahuBiEIE/tuBaI6saeuByJtBaIwB7Ju0OL591JuciLNBSJudbPd30mtBaI1WkBeoahuBGctBa5Ap+c9BaJuBtFqBaJuBaJp1dJ3l1JuBgFNB7JuGrIfLkJtBaICqkfsdVe5RKEZvJCzB1Ju1aeuBg+73mWuB1Juvw4Gz4HEXvKrkwNYGvpWFuv34o6PMAK1STTP1+WzH/iimcVdOJmzJg7Kq9JTCkWHKVtljPihlPyGHwLAozidHmdzRzZYEPQ/Rukg1pOePQuUUoal4nBJFfXEYNHwN7su4lU81hL87Ms+z5Do0rTBkcU8+Ir6Jwy10MFtHNumzfvM11JXIDWCM/gxZ3QS/Ce6KrqnzUKnxJlZZgVq6+U5iKTLMzwshXjtci8HxZZePdrRjlyz99B6U+jC0kqcq7bKZ8bQI6PhvSpT7FR9N1OKnH2qxvj2Gw9D91XIbnkdOD+3pQSQpZAyyAO1k7+Wdlm6OhMdYxpbSXyqT1+hHJOZXe9XlrzhSozyhR7ON2UGaaMnDt6AEyZh7eeNTXjrn26GMa8dPGzMoKdr3sRjYQ5eL6OdF4Ny7cVdTaBDOSroEPUXBaJulQSMmw3NKnViBaJuQ19vCsLkRCLoZNKJzKbMx2sK+IYR98DbRoIWyVSjnHg9cqSKjx8ETtiwpXz/Ue/K9029LsUABOUccUN0XgT3613DOiTK/g8rJ5e1QTvILqoiL1kFBBq4vpt7/Ylj039Er58fC6UsbLnB7l13mYXA7uIiczCTAu59NSD/OA48bJywyPSyTrOSc1YZajcLvtspVWtKtmawkMW/BaJuMaJuBZY5/QmVBaJug0rJA1ZuBaJaSwfikheOIHsROY/TH1JuB7JuBGevBaJVBaJukxJjQ7JuBaJvBaJuEEJuQHMKo1IhBaJuh1Lk7eCH/3sLBxUc7sFM/heu03ZBhwgjs/3zcbCHkxWRoufvrhcM0qfkK638/GMTMaZcK2v507MbSuxvkGOfr1fk06ZXKt89cSflP2ULoveYc2xx+3K1kGn+O2LcepxAcnJuBaJuBaJuBaJu7aJuBb/NJHOTHxlVcElzPoWL06nv21mYrLm5Rb3I5qhjLvE1chDZOoW72YZzHuLbrtJhkqOc5Vs8EL8jBaJuBaFuBa56dMgdqqMgHvcuBaJb2aGadt/QraWN503jovxVcxDnc0C60uJb07tCdtEBrHh5NoJuBaJuB7JuBwG6BaJuBaJu+aJuBxQ9pLKMPbvd',
        'x-shopee-language': 'vi',
        'x-sz-sdk-version': '1.12.8'
    }

    params = {
        'item_id': item_id,
        'shop_id': shop_id,
        'tz_offset_minutes': '420',
        'detail_level': '0',
    }
    
    # Gửi yêu cầu GET đến API với cookie, headers và params
    response = requests.get(api_url, cookies=cookies, headers=headers, params=params)
    
    # In ra toàn bộ phản hồi JSON
    if response.status_code == 200:
        print(response.json())
        product_info = parser_product(response.json())
        print(product_info)
    else:
        print(f"Yêu cầu thất bại với mã lỗi: {response.status_code}")
else:
    print("Không tìm thấy kết quả")