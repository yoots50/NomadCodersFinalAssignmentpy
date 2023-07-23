from bs4 import BeautifulSoup
import requests
from extractors.rmt import extract_rmt_jobs
from extractors.wwr import extract_wwr_jobs

results = extract_rmt_jobs("rust")
print(results)
