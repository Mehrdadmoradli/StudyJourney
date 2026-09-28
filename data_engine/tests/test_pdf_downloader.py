from pathlib import Path

from studyjourney_data_engine.downloader.pdf_downloader import download_pdf


url = "https://www.hs-fulda.de/fileadmin/user_upload/Hochschulkommunikation/ZSUE/AI/MSc_GSD_2020_en_DeepL-UEbersetzung_SPO.pdf"


destination = Path(f"tests/results/pdf_downloader_result2.pdf")


result = download_pdf(url, destination)

print(f"Downloaded to: {result}")
print(f"Exists: {result.exists()}")
print(f"Size: {result.stat().st_size} bytes")
