# web scrape script for LinkedIn jobs
# python jobs
import requests
from bs4 import BeautifulSoup
import csv


def scrape():
    html = requests.get(
        "https://www.linkedin.com/jobs/search?keywords=python&location=Singapore&geoId=102454443&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=3087806252&position=2&pageNum=0"
    ).text
    soup = BeautifulSoup(html, "lxml")

    # job = soup.find("li", class_="jobs-search-results__list-item occludable-update")
    jobs = soup.find_all(
        "div",
        class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
    )

    for job in jobs:
        published_date = job.find("time").text.replace(" ", "")
        if "hours" or "days" in published_date:
            company_name = job.find("h4").text.strip()
            job_title = job.find("h3").text.strip()
            job_link = job.a["href"]

            # data = [company_name, job_title, job_link]

            # print(f"Posted {published_date.strip()}")
            # print(f"Company: {company_name.strip()}")
            # print(f"Looking for: {job_title.strip()}")
            # print(f"Job link: {job_link}")

            # print(" ")
            try:
                with open("Jobs.csv", "a") as fopen:
                    csv_writer = csv.writer(fopen)
                    data = [f"""{company_name} \n {job_title} \n {job_link}"""]

                    csv_writer.writerow(data)
            except:
                return False


# def write_to_csv(list):
#     try:
#         with open("Jobs.csv", "a") as fopen:
#             csv_writer = csv.writer(fopen)
#             csv_writer.writerow(list)
#     except:
#         return False


if __name__ == "__main__":
    print("Starting job scrape . .")
    scrape()
