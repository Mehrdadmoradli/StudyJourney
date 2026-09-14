from pathlib import Path

from studyjourney_data_engine.downloader.pdf_downloader import download_pdf


url = "https://www.fh-dortmund.de/medien/po/fb4/infBA_ab_2013/StgPO_BA_Informatik_2026_final.pdf"


destination = Path(f"tests/results/pdf_downloader_result.pdf")


result = download_pdf(url, destination)

print(f"Downloaded to: {result}")
print(f"Exists: {result.exists()}")
print(f"Size: {result.stat().st_size} bytes")
