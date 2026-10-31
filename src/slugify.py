"""Slugify utility for the STARK sandbox (target of one supervised cloud-agent test)."""


def slugify(text: str) -> str:
    """Return a URL slug for ``text``.

    Rules: lowercase; every run of characters that are not ASCII letters or digits becomes a single "-";
    no leading or trailing "-"; an empty or symbol-only input returns "".
    """
    raise NotImplementedError
