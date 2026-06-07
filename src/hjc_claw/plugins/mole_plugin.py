import os
import shutil
from pathlib import Path
from .base import BasePlugin
from ..core.registry import PluginMetadata, registry

@registry.register
class MolePlugin(BasePlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="mole_cleaner",
            description="Automatic dummy file and cache cleaner (Mole-style)",
            intents=[
                {
                    "intent": "clean_dummy",
                    "keywords": ["mole", "clean dummy", "remove cache", "cleanup", "tidy up", "더미 정리"],
                    "action": "cleanup_project",
                    "dangerous": True
                },
                {
                    "intent": "analyze_waste",
                    "keywords": ["analyze space", "check dummy", "show waste", "용량 분석"],
                    "action": "analyze_space"
                }
            ]
        )

    def cleanup_project(self, paths=None, **kwargs):
        target_root = paths[0] if paths else os.getcwd()
        patterns = [
            "**/__pycache__", 
            "**/*.pyc", 
            "**/*.pyo", 
            "**/*.pyd",
            "**/.DS_Store", 
            "**/Thumbs.db",
            "**/*.log",
            "**/temp_*",
            "**/.pytest_cache",
            "**/.ipynb_checkpoints"
        ]
        
        cleaned_count = 0
        freed_space = 0
        
        results = []
        for pattern in patterns:
            for path in Path(target_root).glob(pattern):
                try:
                    size = self._get_size(path)
                    if path.is_file():
                        path.unlink()
                    elif path.is_dir():
                        shutil.rmtree(path)
                    
                    cleaned_count += 1
                    freed_space += size
                    results.append(f"  - Removed: {path.relative_to(target_root)}")
                except Exception as e:
                    results.append(f"  - Failed to remove {path}: {str(e)}")

        if cleaned_count == 0:
            return f"✨ No dummy files found in '{target_root}'. Everything is clean!"
        
        summary = (
            f"🧹 Mole Cleanup Finished!\n"
            f"  - Total items removed: {cleaned_count}\n"
            f"  - Space recovered: {freed_space / 1024:.2f} KB\n"
            + "\n".join(results[:10])
        )
        if len(results) > 10:
            summary += f"\n  ... and {len(results)-10} more items."
        return summary

    def analyze_space(self, paths=None, **kwargs):
        target_root = paths[0] if paths else os.getcwd()
        total_size = 0
        dummy_size = 0
        
        dummy_patterns = ["**/__pycache__", "**/*.pyc", "**/*.log", "**/.DS_Store"]
        
        for path in Path(target_root).rglob("*"):
            if path.is_file():
                total_size += path.stat().st_size
        
        for pattern in dummy_patterns:
            for path in Path(target_root).glob(pattern):
                dummy_size += self._get_size(path)

        return (
            f"📊 Space Analysis for '{target_root}':\n"
            f"  - Total project size: {total_size / 1024 / 1024:.2f} MB\n"
            f"  - Potential dummy waste: {dummy_size / 1024:.2f} KB\n"
            f"  - Tip: Use 'mole' command to clean up waste."
        )

    def _get_size(self, path):
        if path.is_file():
            return path.stat().st_size
        elif path.is_dir():
            return sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
        return 0
