import os
import pickle
from typing import Any

CACHE_DIR = "cache"  # folder to store cache files
os.makedirs(CACHE_DIR, exist_ok=True)

class CacheService:
    def __init__(self, cache_dir: str = CACHE_DIR):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)
        self._memory_cache = {}  # in-memory cache during runtime

    def _get_cache_path(self, key: str) -> str:
        """Generate file path for a cache key"""
        filename = f"{key}.pkl"
        return os.path.join(self.cache_dir, filename)

    def get(self, key: str) -> Any | None:
        """Return cached data if available (memory first, then disk)"""
        if key in self._memory_cache:
            return self._memory_cache[key]

        path = self._get_cache_path(key)
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = pickle.load(f)
            self._memory_cache[key] = data  # store in memory for fast access
            return data

        return None

    def set(self, key: str, data: Any) -> None:
        """Store data in memory and persist to disk"""
        self._memory_cache[key] = data
        path = self._get_cache_path(key)
        with open(path, "wb") as f:
            pickle.dump(data, f)

    def clear(self, key: str | None = None) -> None:
        """Clear a specific cache key or all cache"""
        if key:
            self._memory_cache.pop(key, None)
            path = self._get_cache_path(key)
            if os.path.exists(path):
                os.remove(path)
        else:
            self._memory_cache.clear()
            for file in os.listdir(self.cache_dir):
                if file.endswith(".pkl"):
                    os.remove(os.path.join(self.cache_dir, file))
