import random
import time
import pandas as pd
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
]

cookie_string = "SPC_F=2S3KdUqD98a12Fd6801BC52Ukx5HrNG3; REC_T_ID=450d9347-6f33-11ef-b5da-a24986d58f89; _QPWSDCXHZQA=ebce5646-6bf2-4a8c-a17d-6a531d25a7d9; REC7iLP4Q=cf764513-b639-4c6b-a608-6572fc8d39fc; _gcl_au=1.1.24672565.1725945147; _fbp=fb.1.1726031734168.371161192420180184; _hjSessionUser_868286=eyJpZCI6ImM2YzM3YzUwLTY0ZGYtNTcwMC05Y2I5LTFiMDYxOTc2MjEyZCIsImNyZWF0ZWQiOjE3MjYzODQwODI2MjUsImV4aXN0aW5nIjp0cnVlfQ==; SPC_CLIENTID=MlMzS2RVcUQ5OGExtbatucezehrhbixl; SC_DFP=gZVXyFkUCNzakraqYPaoDSOroVIRUjSu; _ga_3XVGTY3603=GS1.1.1727058732.1.0.1727058740.52.0.0; _fbc=fb.1.1730008816413.PAZXh0bgNhZW0CMTEAAaYfKB0dlgKbYZHGZoq-MuFuiJ6LW9ZlUu7V909MYYBTyp1Qt1lefLOOsco_aem_K-MS_qAdzQ242sPRdVKyIg; _gcl_gs=2.1.k1$i1730389170$u260663631; _gcl_aw=GCL.1730389173.Cj0KCQjw1Yy5BhD-ARIsAI0RbXZYbRfoEH-xN6C4O-QxOLYHk8puzGy0mTGb2B4yTULs7nLB0IN3jjYaAg8pEALw_wcB; _gac_UA-61914164-6=1.1730389174.Cj0KCQjw1Yy5BhD-ARIsAI0RbXZYbRfoEH-xN6C4O-QxOLYHk8puzGy0mTGb2B4yTULs7nLB0IN3jjYaAg8pEALw_wcB; __LOCALE__null=VN; SPC_SI=u8I1ZwAAAAA5N0FVTkg1ZBeRKgAAAAAAOVJOQW1wRnY=; csrftoken=giuznsmTNxKcI8xJEW3m6l0Ew3h4qnOz; _sapid=219f78693e20360fcdbf486a2f34ba8831843163849c7484e73d06ce; SPC_IA=1; _gid=GA1.2.1389408610.1732036185; SPC_CDS_CHAT=ce8edd5d-96d9-4fbc-a422-96f1a3dde780; _med=refer; SPC_SEC_SI=v1-Rm1hbnUzWU55ZUFLNmppVLsEziaZ79KmmBbmhNH1mbEwV4zo3ZvSFAbHGFs5slWwLOQaWg0ZFb0iC3wziR8wl5JqnFVZVdnSuLdA3ygw6QE=; AMP_TOKEN=%24NOT_FOUND; SPC_EC=.RTNtSGhHNG1ydHFjb09kYUigkb3SCYdlk7msdIo9UWLzdbicaoUCnubxmH9DrE2oHqDZDcbK1ynjjfuSKWVw9xT2L097rY8XfUR+IPL8qxAd6pnGUGNAbvgzjTw6kUeN/9by7QVtMtRRAgp6puJdR3DETiTZpTbUPURj0p0O4TT1u78kZSyo5RQLZewi3Zd87fHhuYNJoBq5Gk9CNQb5wpEHufK0gCPMEy1kyOAYJCsAk9WbOiSeyr4faFGrd97H; SPC_ST=.RTNtSGhHNG1ydHFjb09kYUigkb3SCYdlk7msdIo9UWLzdbicaoUCnubxmH9DrE2oHqDZDcbK1ynjjfuSKWVw9xT2L097rY8XfUR+IPL8qxAd6pnGUGNAbvgzjTw6kUeN/9by7QVtMtRRAgp6puJdR3DETiTZpTbUPURj0p0O4TT1u78kZSyo5RQLZewi3Zd87fHhuYNJoBq5Gk9CNQb5wpEHufK0gCPMEy1kyOAYJCsAk9WbOiSeyr4faFGrd97H; SPC_U=1011065965; SPC_R_T_ID=K1FZMsPKaam2YEo9OGOozO8Zz9CeaQ4VTQc5+4RFaARphDjihReUCz8OZOR6OVV5XDa+iUtYsfRD/Y/2o3twpCeWbK+mOli81JlzU6+OHvtqUDreQDQokfI9Y75vfDgEyhYdGAzsidIvZzm0f1zFqWlyhT7pqxHQu2MtlUGucpw=; SPC_R_T_IV=cmhibzV1dlU0Z2hBMXhnNA==; SPC_T_ID=K1FZMsPKaam2YEo9OGOozO8Zz9CeaQ4VTQc5+4RFaARphDjihReUCz8OZOR6OVV5XDa+iUtYsfRD/Y/2o3twpCeWbK+mOli81JlzU6+OHvtqUDreQDQokfI9Y75vfDgEyhYdGAzsidIvZzm0f1zFqWlyhT7pqxHQu2MtlUGucpw=; SPC_T_IV=cmhibzV1dlU0Z2hBMXhnNA==; _dc_gtm_UA-61914164-6=1; _ga=GA1.1.265873742.1726200588; _hjSession_868286=eyJpZCI6ImZhNGNhZjJiLWU5ZmItNDdkMS1hNjZlLTFjMzM5Yjc3MGEyZSIsImMiOjE3MzIyMDQwMjU4OTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; AC_CERT_D=U2FsdGVkX1/lIHnX0C8BpQaDJb6QarNn2kAudx/6e2o004QWeJdtBqs0C8kvdYLt7LhBb6ZGLfg+dZSopUq1BUp+YCoPd6sptVZUhYSvtnC5cYslUAQ5pZlVwi0O69nlrZQYCMn3OZOHrsnPVU2dqCT/QGelyCZp/2Y/kq2nvg/HazYRjSrc4tXZFYn0MgUPx8hIgCV88pUHbNR673ISNgf4ZRUFFggik+5ILg0SbFChdeXGEtzwBrCMu+gfhGfQqx7fEXdnWgQm9NUnKsu1LRZrybOGY6Wp7ZRaVCy85GZKcsTmfiw+8WhHl81AJtVndSfWdavIpdOEf/6Eun+kM20VoVY610vjzDEWQ9mELH9Dqi3wBy7g0xNBfooPeYc4zpeVDOThFYio3KUX2AftmO/NjTXPY4D5oXmjRgpOpdgYu0ityGvDx0hV9cP2Dkm+mcJGYTO58TRNAYEQoI+g9c/haAEz7vFiA0JMjBhU9YmkOJokK5gW1ugPf3SKKMh3wNPBrc9JEcXThGb0508OD6JlYeJXzUGmEna0W59CcYa0F5wqkRkcU5KQytBnVUOIcorYDguWmJuymwVWQgQHf9fw+SyJAd9cPqTiKDwp7Jvr7u4ak3lURWwRHipe1G7w2DuW5ul26ybMPXljutBkPdXRsUGG+CrvFWwvUq8CnmG2vwwt+o9/WnLIgKRzWq1vQnITNIqM6iWQpiqz+PpQoNPs2bNIQPjR3xlRfh+lUP/56D9EYtwNaQLGccV+PfAcAHtjhqwEJMgzr2nm0EnbSXmI4hrkCyy2BU3RJBbp4kgdBW9cIpBqDqwjQK4PGC7/hHCaQNeAtuttDVW+9UjXB09cIkjU/zJ7RegUsRD3kS9d6rpOex6INF2sLGz7r5L/bI7YxaYygLkx0+P6FezhZ39+8YwkhIAPL0kBJyz1bGflRDUKzAsJo2Og8cw/TV7KgT8V0ouA+MWhDF83n/JaqV44y6XYWIkUVQghBJAeoxiSZyauDRNvaq44R3eCqC6+aK9o0C3D0epH/JOba0PRsKDEiBH6Ro1Oz7quolawV89fBewpc6j0ZU/v7Xh5C8cQMVguYAHsxFtjp37XKp6ETtrbzJcOyZFilCDrMx45XH4="

cookies = []
for cookie in cookie_string.split('; '):
    name, value = cookie.split('=', 1)
    cookies.append({
        'name': name,
        'value': value,
        'domain': 'shopee.vn',
        'path': '/',
        'expires': -1,
        'httpOnly': False,
        'secure': False,
        'sameSite': 'Lax'
    })

def main():
    with sync_playwright() as p:
        user_agent = random.choice(user_agents)
        print(user_agent)

        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            timezone_id="Asia/Ho_Chi_Minh",
            locale='vi-VN',
            user_agent=user_agent,
            java_script_enabled=True
        )

        #stealth_sync(context)  # Apply stealth techniques

        context.add_cookies(cookies)

        # context.set_extra_http_headers({
        #     "DNT": "1",
        #     "Connection": "keep-alive",
        #     "Accept-Language": "vi-VN,vi;q=0.9",
        #     "Upgrade-Insecure-Requests": "1",
        #     "Cache-Control": "max-age=0",
        #     "Sec-Fetch-Dest": "document",
        #     "Sec-Fetch-Mode": "navigate",
        #     "Sec-Fetch-Site": "same-origin",
        #     "Sec-Fetch-User": "?1"
        # })

        

        # Save cookies to file
        context.storage_state(path="cookies.json")

        page = context.new_page()

        page.set_viewport_size({"width": 1366, "height": 768})
        
        page.goto('https://shopee.vn/S%C3%A1ch-C%C3%A2y-Cam-Ng%E1%BB%8Dt-C%E1%BB%A7a-T%C3%B4i-(Nh%C3%A3-Nam-HCM)-i.404602141.9338588760?sp_atk=07612dab-fd71-44b0-a457-6b7d314d935e&xptdk=07612dab-fd71-44b0-a457-6b7d314d935e')

        time.sleep(10000)

        if "captcha" in page.url:
            print("Captcha page detected. Please solve the captcha manually.")
            input("Press Enter after solving the CAPTCHA...")
        else:
            page_number = 1
            all_comments = []

            while True:
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(random.uniform(5, 10))

                comments = page.query_selector_all('div[style*="word-break: break-word"]')
                for comment in comments:
                    all_comments.append({'comment': comment.inner_text()})

                authors = page.query_selector_all('a.shopee-product-rating__author-name')
                for author in authors:
                    href = author.get_attribute('href')
                    author_id = href.split('/')[-1] if href else 'None'
                    author_name = author.inner_text()
                    all_comments.append({'id': author_id, 'name': author_name})

                next_button = page.query_selector(f'button.shopee-button-no-outline:has-text("{page_number + 1}")')
                if next_button:
                    next_button.click()
                    page_number += 1
                    time.sleep(random.uniform(5, 10))
                else:
                    break

            df = pd.DataFrame(all_comments)
            df.to_csv('comments.csv', index=False, encoding='utf-8')

        browser.close()

if __name__ == "__main__":
    main()