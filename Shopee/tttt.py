import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'f20c502c-ef0a-43f7-bdfe-1d4cb930e667',
      'url': 'https://shopee.vn/%C3%81o-Thun-Tr%C6%A1n-Cotton-250gsm-GODMOTHER-Premium-Full-Color-C%E1%BB%95-Tr%C3%B2n-Nam-N%E1%BB%AF-i.703090265.19787998337?sp_atk=dbf9d37b-1b9a-4354-bb23-777478a1e934&xptdk=dbf9d37b-1b9a-4354-bb23-777478a1e934', 
  },
)

print('Response Body: ', response.content)
      