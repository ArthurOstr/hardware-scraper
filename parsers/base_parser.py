from abc import ABC, abstractclassmethod
from typing import List, Optional
from models.hardware import Component


class BaseParser(ABC):
    def __init__(self, html_source: str):
        self.html = html_source

    @abstractclassmethod
    def extract_items(self) -> List[Component]:
        """Parses the HTML and returns a list of strict Component models"""
        pass

    @abstractclassmethod
    def get_next_page_url(self) -> Optional[str]:
        """Extract the pagination 'Next' link, or returns None if at the end."""
        pass
