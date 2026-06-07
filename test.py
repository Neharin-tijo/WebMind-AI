from crawler import crawl_website

pages = crawl_website("https://example.com")

print(len(pages))

for url, text in pages.items():
    print(url)
    print(text[:200])
    