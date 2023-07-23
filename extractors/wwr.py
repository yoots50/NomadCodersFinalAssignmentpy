from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(term):
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  request = requests.get(url)
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all("li")
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor["href"]
        company, kind, region = anchor.find_all("span", class_="company")
        title = anchor.find("span", class_="title")
        job = {
            'link': link,
            'company': company.string,
            'position': title.string,
            'location': region.string
        }
        results.append(job)

  else:
    print("Can't get jobs.")

  return results
