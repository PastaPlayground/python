# web scrape script for LinkedIn jobs
# python jobs

# 26/05/2022
# change output format from csv to json for clearer view of data
# create a list of dictionaries to store key values of jobs

# 27/05/22
# create empty list outside of for loop to prevent looping empty list
# append the dictionaries into list using a loop
# create folder to contain all json files

import os
import requests
from bs4 import BeautifulSoup
import datetime
import csv
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

    # empty list
    output = []
    for job in jobs:
        published_date = job.find("time").text.strip()
        matches = ["minutes", "hour", "hours", "day", "days"]

        if any(x in published_date for x in matches):
            company_name = job.find("h4").text.strip()
            job_title = job.find("h3").text.strip()
            job_link = job.a["href"]

            # 1 company data
            # dictionary of key pair value
            data = {
                "Posted": f"{published_date}",
                "Company name": f"{company_name}",
                "Job Title": f"{job_title}",
                "Link": f"{job_link}",
            }

            # append all company data into list with for loop
            output.append(data)
            # convert list into json object
            json_output = json.dumps(output, indent=2)

            # open jobs folder and add new json file inside
            with open(f"{folderName}/{user_job}.json", "w") as fopen:
                fopen.write(json_output)

            # try:
            # #     # export CSV format
            # #     with open(f"{user_job}.csv", "a") as fopen:
            # #         csv_writer = csv.writer(fopen)
            # #         data = [
            # #             f"Posted: {published_date} \n Company: {company_name} \n Title: {job_title} \n Link: {job_link}"
            # #         ]

            # #         csv_writer.writerow(data)

            # except:
            #     return False


if __name__ == "__main__":
    user_job = input("Job title your are looking for: ").replace(" ", "").lower()
    now = datetime.datetime.now()
    formatDate = now.strftime("%x")

    # jobScrape absolute path
    fileDir = os.path.dirname(os.path.realpath("__file__"))

    # folder in same path as jobScrape
    folderName = os.path.join(fileDir, "jobs")

    print(f"Starting job scrape for {user_job} on {formatDate}. . .")
    scrape()
    print(f"Jobs scrape done for {user_job} on LinkedIn")
else:
    print("Unsuccessful")
