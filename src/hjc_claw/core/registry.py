"""
core/registry.py — 플러그인 레지스트리 시스템
==========================================
모든 도구(Plugin)를 중앙에서 관리하고 의도(Intent)에 따라 라우팅합니다.
"""

from typing import Dict, List, Any, Callable, Optional
from dataclasses import dataclass, field

@dataclass
class PluginMetadata:
    name: str
    description: str
    intents: List[Dict[str, Any]]  # {intent, keywords, action, dangerous}
    instance: Any = None

class PluginRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PluginRegistry, cls).__new__(cls)
            cls._instance.plugins = {}
            cls._instance.intent_map = {}
        return cls._instance

    def register(self, plugin_class: Any):
        """플러그인 클래스를 등록합니다."""
        instance = plugin_class()
        meta = instance.get_metadata()
        
        self.plugins[meta.name] = meta
        meta.instance = instance

        for intent_info in meta.intents:
            intent_name = intent_info["intent"]
            self.intent_map[intent_name] = {
                "plugin": meta.name,
                "action": intent_info["action"],
                "keywords": intent_info.get("keywords", []),
                "dangerous": intent_info.get("dangerous", False)
            }
        return plugin_class

    def get_plugin(self, name: str) -> Optional[Any]:
        meta = self.plugins.get(name)
        return meta.instance if meta else None

    def get_all_intents(self) -> Dict[str, Any]:
        return self.intent_map

registry = PluginRegistry()
