"""
Rate limiting service to prevent abuse
"""
from typing import Dict
from datetime import datetime, timedelta
from collections import defaultdict


class RateLimiter:
    """Simple in-memory rate limiter"""

    def __init__(self, requests_per_window: int = 10, window_minutes: int = 60):
        self.requests_per_window = requests_per_window
        self.window_minutes = window_minutes
        self.requests: Dict[str, list] = defaultdict(list)

    def is_allowed(self, identifier: str) -> tuple[bool, int]:
        """
        Check if request is allowed for given identifier (IP, user ID, etc.)
        Returns: (is_allowed, remaining_requests)
        """
        now = datetime.now()
        window_start = now - timedelta(minutes=self.window_minutes)

        # Clean old requests
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if req_time > window_start
        ]

        # Check if under limit
        current_count = len(self.requests[identifier])

        if current_count >= self.requests_per_window:
            return False, 0

        # Record new request
        self.requests[identifier].append(now)
        remaining = self.requests_per_window - current_count - 1

        return True, remaining

    def reset(self, identifier: str):
        """Reset rate limit for identifier"""
        if identifier in self.requests:
            del self.requests[identifier]

    def get_stats(self, identifier: str) -> Dict[str, int]:
        """Get rate limit stats for identifier"""
        now = datetime.now()
        window_start = now - timedelta(minutes=self.window_minutes)

        # Clean old requests
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if req_time > window_start
        ]

        current_count = len(self.requests[identifier])
        remaining = max(0, self.requests_per_window - current_count)

        return {
            'limit': self.requests_per_window,
            'used': current_count,
            'remaining': remaining,
            'window_minutes': self.window_minutes
        }


# Singleton instance - 10 requests per hour for free tier
rate_limiter = RateLimiter(requests_per_window=10, window_minutes=60)
