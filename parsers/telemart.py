from bs4 import BeautifulSoup
from typing import List, Optional
from parsers.base_parser import BaseParser
from models.hardware import Component


class TelemartParser(BaseParser):
    def __init__(self, html_source: str):
        super().__init__(html_source)
        self.soup = BeautifulSoup(self.html, "lxml")
        self.base_url = "https://telemart.ua"

    def extract_items(self) -> List[Component]:
        components = []

        product_cards = self.soup.select(".product-item__inner")

        print(f"[*] Found {len(product_cards)} potential products on this page.")

        for card in product_cards:
            try:
                name = card.get("data-prod-name")
                price_str = card.get("data-prod-price")

                if not name or not price_str:
                    continue
                link_node = card.find("a")
                if link_node and link_node.get("href"):
                    url = self.base_url + link_node.get("href")
                else:
                    url = "https://telemart.ua/missing-link"

                brand = card.get("data-prod-brand")
                articul = card.get("data-prod-articul")

                component = Component(
                    name=name,
                    category="CPU",
                    url=url,
                    price_uah=float(price_str),
                    specs={"brand": brand, "articul": articul},
                )
                components.append(component)

            except Exception as e:
                print(f"[-] Failed to parse a card: {e}")
                continue

        return components

    def get_next_page_url(self) -> Optional[str]:
        return None
