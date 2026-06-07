import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import os


def get_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        domain = urlparse(url).netloc

        for tag in soup.find_all("a", href=True):
            link = urljoin(url, tag["href"])

            # Only crawl links from the same domain
            if urlparse(link).netloc == domain:
                links.append(link)

        return list(set(links))

    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return []


def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts and styles
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""


def save_pages(pages):
    os.makedirs("data", exist_ok=True)

    with open("data/pages.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(pages)} pages to data/pages.json")


def crawl_website(start_url, max_pages=10):
    visited = set()
    pages = {}

    queue = [start_url]

    while queue and len(visited) < max_pages:

        url = queue.pop(0)

        if url in visited:
            continue

        print(f"Crawling: {url}")

        visited.add(url)

        text = scrape_page(url)

        if text:
            pages[url] = text

        links = get_links(url)

        for link in links:
            if link not in visited:
                queue.append(link)

    save_pages(pages)

    return pages
    