"""
plugins/base.py — 플러그인 베이스 클래스
======================================
모든 도구는 이 클래스를 상속받아 구현됩니다.
"""

from abc import ABC, abstractmethod
from ..core.registry import PluginMetadata

class BasePlugin(ABC):
    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        """플러그인의 메타데이터와 의도 맵을 반환합니다."""
        pass
