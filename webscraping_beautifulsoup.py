from bs4 import BeautifulSoup
import requests
html_content = requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=").text
soup = BeautifulSoup(html_content,'lxml')
jobs = soup.find_all("div",class_="srp-job-bx")
for index,job in enumerate(jobs, start = 1):
    company_name = job.find("span",class_="srp-comp-name").text
    job_link = job.a['href']
    skills = [a.text.strip() for a in job.find('div',class_ = "srp-keyskills").find_all("a")]
    location = job.find('div',class_ = "srp-loc").text
    experience = job.find('div',class_ = "srp-exp").text
    salary_or_ctc= job.find('div',class_ = "srp-sal").text
    print(f'''job_count:{index}\n''')
    print(f'''company_name : {company_name}\n''')
    print(f'''key_skills : {skills}\n''')
    print(f'''Location:{location}\n''')
    print(f'''experience:{experience}\n''')
    print(f'''salary_or_ctc:{salary_or_ctc}\n''')
    print(f'''company_link : {job_link}\n''')
    print("\n")
    print("\n")
    print("\n")
