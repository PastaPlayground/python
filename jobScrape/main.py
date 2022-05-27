# web scrape script for LinkedIn jobs
# python jobs

# 26/05/2022
# change output format from csv to json for clearer view of data
# create a list of dictionaries to store key values of jobs

import requests
from bs4 import BeautifulSoup
import csv
import datetime
import json


# user can key input for dynamic search
# print("Job title your are looking for: ")


def scrape():

    url = f"https://www.linkedin.com/jobs/search?keywords={user_job}&location=Singapore&geoId=102454443&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=3087806252&position=2&pageNum=0"

    html = requests.get(url).text

    # init Beautiful soup instance
    soup = BeautifulSoup(html, "lxml")

    jobs = soup.find_all(
        "div",
        class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
    )

    # get individual data without for loop
    # running for loop to get all data from the page
    for job in jobs:
        published_date = job.find("time").text.strip()
        matches = ["minutes", "hour", "hours", "day", "days"]

        if any(x in published_date for x in matches):
            company_name = job.find("h4").text.strip()
            job_title = job.find("h3").text.strip()
            job_link = job.a["href"]

            # empty list
            output = []

            # dictionary of key pair value
            data = {
                "Posted": f"{published_date}",
                "Company name": f"{company_name}",
                "Job Title": f"{job_title}",
                "Link": f"{job_link}",
            }
            # print(data)
            # for i in range

            output.append(data)
            # print(output)
            print(json.dumps(output, indent=4))

            try:
                # export CSV format
                # with open(f"{user_job}.csv", "a") as fopen:
                #     csv_writer = csv.writer(fopen)
                #     data = [
                #         f"{published_date} \n {company_name} \n {job_title} \n {job_link}"
                #     ]

                #     csv_writer.writerow(data)

                # export JSON format
                # data in dictionary form

                # 1 company data

                json_data = json.dumps(data, indent=2)
                # with open(f"{user_job}.json", "a") as fopen:

                #     fopen.write(json_data)

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
    user_job = input("Job title your are looking for: ").replace(" ", "").lower()
    now = datetime.datetime.now()
    formatDate = now.strftime("%x")

    print(f"Starting job scrape for {user_job} on {formatDate}. . .")
    scrape()
    print(f"Jobs scrape done for {user_job} on LinkedIn")
