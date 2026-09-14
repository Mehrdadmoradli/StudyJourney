from pathlib import Path

import httpx


def download_pdf(url: str, destination: Path) -> Path:
    response = httpx.get(
        url,
        follow_redirects=True,
        timeout=30.0,
    )

    response.raise_for_status()

    content_type = response.headers.get("content-type", "")

    if "application/pdf" not in content_type:
        raise ValueError(
            f"Expected PDF but received: {content_type}"
        )

    if not response.content:
        raise ValueError("Downloaded PDF is empty")

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    destination.write_bytes(response.content)

    return destination
