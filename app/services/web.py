from fastapi import HTTPException
import requests
from bs4 import BeautifulSoup


class Web:
    def __init__(self, url: str):
        self.url = url
        self.content = None

    def fetch(self) -> str:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.content = response.content
            return self.content
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def extract_text(self) -> str:
        if not self.content:
            raise ValueError("No content fetched. Call fetch() first.")
        soup = BeautifulSoup(self.content, "html.parser")
        return soup.get_text()
