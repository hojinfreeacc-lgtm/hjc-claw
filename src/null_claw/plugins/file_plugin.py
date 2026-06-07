import os
import shutil
from pathlib import Path
from .base import BasePlugin
from ..core.registry import PluginMetadata, registry

@registry.register
class FilePlugin(BasePlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="file_system",
            description="파일 및 디렉토리 관리 도구",
            intents=[
                {
                    "intent": "file_list",
                    "keywords": ["목록", "리스트", "보여줘", "ls", "파일 확인"],
                    "action": "list_files"
                },
                {
                    "intent": "file_delete",
                    "keywords": ["삭제", "지워", "remove", "delete"],
                    "action": "delete_file",
                    "dangerous": True
                }
            ]
        )

    def list_files(self, paths=None, **kwargs):
        target = paths[0] if paths else os.getcwd()
        try:
            items = os.listdir(target)
            if not items: return f"'{target}' 폴더가 비어 있습니다."
            return f"📁 {target} 목록:\n" + "\n".join([f"  - {i}" for i in items])
        except Exception as e:
            return f"오류: {str(e)}"

    def delete_file(self, paths=None, **kwargs):
        if not paths: return "삭제할 파일 경로가 없습니다."
        target = paths[0]
        try:
            if os.path.isfile(target):
                os.remove(target)
                return f"파일 '{target}'을(를) 삭제했습니다."
            elif os.path.isdir(target):
                shutil.rmtree(target)
                return f"디렉토리 '{target}'을(를) 삭제했습니다."
            return f"'{target}'을(를) 찾을 수 없습니다."
        except Exception as e:
            return f"삭제 실패: {str(e)}"
