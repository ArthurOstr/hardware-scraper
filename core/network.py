import httpx
from httpx import HTTPStatusError, RequestError


class NetworkFetcher:
    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5,uk;q=0.3",
        }
        self.client = httpx.Client(
            headers=self.headers, timeout=15.0, follow_redirects=True
        )

    def fetch_page(self, url: str) -> str:
        """Attempts to fetch the raw HTML or JSON from a target URL."""
        try:
            print(f"[*] Firing request at: {url}")
            response = self.client.get(url)

            response.raise_for_status()

            print(f"[+] Success! Status Code: {response.status_code}")
            return response.text

        except HTTPStatusError as e:
            status = e.response.status_code
            print(f"[-] HTTP Error: The server returned {status}")
            return ""
        except RequestError as e:
            print(f"[-] Network Error: Failed to connect to {url}")
            return ""

    def close(self):
        """Clean up the connection pool when we are done."""
        self.client.close()
