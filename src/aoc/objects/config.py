from typing import Optional


class AdventOfCodeConfig:
    debug = False
    testing = False

    auto_fetch_input = False
    cache_input = False

    session: Optional[str] = None

    cache_directory: Optional[str] = None
