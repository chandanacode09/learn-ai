"""
Caching service for API responses
Reduces costs by caching common explanations
"""
import json
import hashlib
from typing import Optional, Dict, Any
from datetime import datetime, timedelta


class CacheService:
    """In-memory cache service with TTL"""

    def __init__(self, ttl_hours: int = 24):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl_hours = ttl_hours

    def _generate_key(self, content: str, level: str, mode: str) -> str:
        """Generate cache key from content and parameters"""
        # Hash the content to create a unique key
        content_hash = hashlib.md5(content.encode()).hexdigest()
        return f"{level}:{mode}:{content_hash}"

    def get(self, content: str, level: str, mode: str) -> Optional[Dict[str, Any]]:
        """Get cached explanation if exists and not expired"""
        key = self._generate_key(content, level, mode)

        if key not in self.cache:
            return None

        cached_item = self.cache[key]
        expiry = cached_item['expiry']

        # Check if expired
        if datetime.now() > expiry:
            del self.cache[key]
            return None

        return cached_item['data']

    def set(self, content: str, level: str, mode: str, data: Dict[str, Any]):
        """Cache explanation with TTL"""
        key = self._generate_key(content, level, mode)
        expiry = datetime.now() + timedelta(hours=self.ttl_hours)

        self.cache[key] = {
            'data': data,
            'expiry': expiry,
            'created_at': datetime.now()
        }

    def clear(self):
        """Clear all cache"""
        self.cache = {}

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        total = len(self.cache)
        expired = sum(
            1 for item in self.cache.values()
            if datetime.now() > item['expiry']
        )

        return {
            'total_entries': total,
            'active_entries': total - expired,
            'expired_entries': expired
        }


# Singleton instance
cache_service = CacheService(ttl_hours=24)
