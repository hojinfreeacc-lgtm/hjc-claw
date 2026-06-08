import requests
from bs4 import BeautifulSoup
from .base import BasePlugin
from ..core.registry import PluginMetadata, registry
from ..core.ai_brain import AIBrain

@registry.register
class AIWebPlugin(BasePlugin):
    def __init__(self):
        self.ai = AIBrain()

    def get_metadata(self):
        return PluginMetadata(
            name="ai_web",
            description="AI-powered web search and summarization",
            intents=[
                {
                    "intent": "ai_search",
                    "keywords": ["검색해줘", "찾아봐", "search ai", "ask web"],
                    "action": "search_and_summarize"
                }
            ]
        )

    def search_and_summarize(self, query=None, **kwargs):
        if not query:
            # params에서 추출 시도
            query = kwargs.get("params", {}).get("query", "latest news")
            
        search_url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        try:
            # 1. 검색 결과 가져오기 (간소화된 크롤링)
            res = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            snippets = [s.get_text() for s in soup.find_all("div")[:10]]
            context = "\n".join(snippets)
            
            # 2. AI에게 요약 요청
            prompt = f"Based on these search results for '{query}', provide a concise summary:\n\n{context}"
            summary = self.ai.ask(prompt, "You are a helpful AI that summarizes web search results.")
            return f"🌐 AI Search Results for '{query}':\n\n{summary}"
        except Exception as e:
            return f"Search Error: {str(e)}"
