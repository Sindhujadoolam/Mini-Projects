**1. Project Title & Description**
**webscraping_beautifulsoup.py (TimesJobs Web Scraper).**

This project is a web scraper built using BeautifulSoup and Requests to extract job listings from TimesJobs. 
It fetches and displays key job details, making it easier to explore job opportunities based on your skills,job count and experience.
To know more about the job details we can have a link available to us we can check and fill the application.

**2. Feature:**
Extracts job details, filters based on skills,experience,location

**3. Installation & Setup**
Steps to set up the project : Installing dependencies(requests,Beautifulsoup,running the script)

**4. How to Use**
Example commands or scripts to run the project.
# Importing required libraries
from bs4 import BeautifulSoup # BeautifulSoup for parsing HTML
import requests # importing requests to request the website 
html_content = requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=").text  # parsing html code inside the html_content variable
soup = BeautifulSoup(html_content,'lxml') # creating instance of beautiful soup and parsing it in the lxml format
jobs = soup.find_all("div",class_="srp-job-bx") # find_all is listing all the jobs
  # iterating over the jobs and counting the jobs using enumerate function
for index,job in enumerate(jobs, start = 1): 
     # Extracting company_name
    company_name = job.find("span",class_="srp-comp-name").text
     # Extracting job link
    job_link = job.a['href']
     # Extracting skills
    skills = [a.text.strip() for a in job.find('div',class_ = "srp-keyskills").find_all("a")]
     # Extracting location
    location = job.find('div',class_ = "srp-loc").text
     # Extracting required experience
    experience = job.find('div',class_ = "srp-exp").text
     # Extracting ctc
    salary_or_ctc= job.find('div',class_ = "srp-sal").text
    # Printing job details in a structured format
    print(f'''job_count:{index}\n''')
    print(f'''company_name : {company_name}\n''')
    print(f'''key_skills : {skills}\n''')
    print(f'''Location:{location}\n''')
    print(f'''experience:{experience}\n''')
    print(f'''salary_or_ctc:{salary_or_ctc}\n''')
    print(f'''company_link : {job_link}\n''')
    print("\n")
    print("\n")

**Sample output:**
     C:\Users\sindh>python webscraping.py
job_count:1

company_name : east india securities ltd.

key_skills : ['python', 'hadoop', 'machine learning']

Location:Kolkata

experience:2 - 5  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-engineer-east-india-securities-ltd-kolkata-2-to-5-yrs-jobid-AoNKFWTxLYxzpSvf__PLUS__uAgZw==&bc=+&sequence=1





job_count:2

company_name : CONNECTING 2 WORK

key_skills : ['rest', 'python', 'django', 'mongodb']

Location:Calicut/ Kozhikode

experience:0 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-trainer-connecting-2-work-calicut-kozhikode-0-to-3-yrs-jobid-Z__PLUS__uCQzJQBSxzpSvf__PLUS__uAgZw==&bc=+&sequence=2      





job_count:3

company_name : SEVEN CONSULTANCY

key_skills : ['python', 'mvc', 'sql']

Location:Navi Mumbai,  Mumbai

experience:4 - 7  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-seven-consultancy-navi-mumbai-mumbai-4-to-7-yrs-jobid-VJ3GBkmUwLVzpSvf__PLUS__uAgZw==&bc=+&sequence=3





job_count:4

company_name : DREAMAJAX TECHNOLOGIES

key_skills : ['python', 'django', 'api', 'sql', 'nosql']

Location:Bengaluru / Bangalore

experience:4 - 7  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-dreamajax-technologies-bengaluru-bangalore-4-to-7-yrs-jobid-QP62Nb779jFzpSvf__PLUS__uAgZw==&bc=+&sequence=4    





job_count:5

company_name : Datagrid Solutions

key_skills : ['python', 'database', 'django', 'mysql', 'api']

Location:Mumbai

experience:2 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-datagrid-solutions-mumbai-2-to-3-yrs-jobid-WOb3ZI4H4nVzpSvf__PLUS__uAgZw==&bc=+&sequence=5





job_count:6

company_name : InnOvator Web Solutions Pvt.Ltd.

key_skills : ['rest', 'python', 'django', 'web developer', 'mysql', 'api']

Location:Mumbai

experience:5 - 8  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-innovator-web-solutions-pvt-ltd-mumbai-5-to-8-yrs-jobid-xW9AZzv9Ek5zpSvf__PLUS__uAgZw==&bc=+&sequence=6        





job_count:7

company_name : CONNECTING 2 WORK

key_skills : ['python', 'storage', 'django', 'testing tools', 'debugging']

Location:Thiruvananthapuram

experience:5 - 10  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-connecting-2-work-thiruvananthapuram-5-to-10-yrs-jobid-rWXOEDNUju5zpSvf__PLUS__uAgZw==&bc=+&sequence=7





job_count:8

company_name : CONNECTING 2 WORK

key_skills : ['database', 'python', 'css', 'rest api', 'html', 'javascript']

Location:Cochin/ Kochi/ Ernakulam

experience:2 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-connecting-2-work-cochin-kochi-ernakulam-2-to-3-yrs-jobid-p__SLASH__ne4OsY9tNzpSvf__PLUS__uAgZw==&bc=+&sequence=8





job_count:9

company_name : SEVEN CONSULTANCY

key_skills : ['Python programming', 'programming language', 'front-end developer']

Location:Surat

experience:9 - 12  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-seven-consultancy-surat-9-to-12-yrs-jobid-Kdex__PLUS__SlZxqJzpSvf__PLUS__uAgZw==&bc=+&sequence=9





job_count:10

company_name : 3RI Technologies Pvt Ltd

key_skills : ['python', 'database', 'security', 'django', 'git', 'mobile']

Location:Pune

experience:0 - 1  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-3ri-technologies-pvt-ltd-pune-0-to-1-yrs-jobid-W8__SLASH__axd9w6ixzpSvf__PLUS__uAgZw==&bc=+&sequence=10        





job_count:11

company_name : Wing Global IT Services

key_skills : ['spring boot', 'python', 'java', 'django', 'jpa', 'hibernate']

Location:Panchkula

experience:2 - 5  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-wing-global-it-services-panchkula-2-to-5-yrs-jobid-ZNzjSAvv9uJzpSvf__PLUS__uAgZw==&bc=+&sequence=11





job_count:12

company_name : DealsCorner

key_skills : ['python', 'css', 'oops', 'linux', 'debugging', 'html', 'javascript']

Location:Ahmedabad

experience:1 - 4  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-dealscorner-ahmedabad-1-to-4-yrs-jobid-hTihN4iwnitzpSvf__PLUS__uAgZw==&bc=+&sequence=12





job_count:13

company_name : AxisTechnolabs

key_skills : ['python', 'django', 'html5', 'api', 'jquery']

Location:Ahmedabad

experience:0 - 1  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-odoo-axistechnolabs-ahmedabad-0-to-1-yrs-jobid-sQ9JqHz7dglzpSvf__PLUS__uAgZw==&bc=+&sequence=13





job_count:14

company_name : 3RI Technologies Pvt Ltd

key_skills : ['python', 'Pandas', 'PyQt5', 'Matplotlib', 'Openpyxl']

Location:Pune

experience:0 - 1  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-programmer-3ri-technologies-pvt-ltd-pune-0-to-1-yrs-jobid-RisAg8NKGbBzpSvf__PLUS__uAgZw==&bc=+&sequence=14





job_count:15

company_name : SKYWALK VISA IMMIGRATION SERVICES LLP

key_skills : ['Python Scripting', 'Data Analysis', 'Matlab', 'c ++', 'Sql', 'Data Visualization', 'Mysql']

Location:Australia,  Canada,  New Zealand,  Singapore,  null

experience:2 - 7  Years

salary_or_ctc:53.30 - 87.25 Lakhs

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-skywalk-visa-immigration-australia-canada-new-zealand-singapore-null-2-to-7-yrs-jobid-3uaoRfVE__PLUS__jRzpSvf__PLUS__uAgZw==&bc=+&sequence=15





job_count:16

company_name : CONNECTING 2 WORK

key_skills : ['security compliance', 'python', 'html5', 'mobile', 'javascript', 'database', 'django', 'debugging']

Location:Thiruvananthapuram

experience:0 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-connecting-2-work-thiruvananthapuram-0-to-3-yrs-jobid-8rfk7VC5R71zpSvf__PLUS__uAgZw==&bc=+&sequence=16





job_count:17

company_name : CONNECTING 2 WORK

key_skills : ['security compliance', 'python', 'html5', 'mobile', 'javascript', 'database', 'django', 'debugging']

Location:Cochin/ Kochi/ Ernakulam

experience:0 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-connecting-2-work-cochin-kochi-ernakulam-0-to-3-yrs-jobid-H6kmUA8Jl55zpSvf__PLUS__uAgZw==&bc=+&sequence=17     





job_count:18

company_name : tataatsu idealabs pvt. ltd.

key_skills : ['oop', 'python', 'linux', 'team player', 'mongodb', 'sql']

Location:Bengaluru / Bangalore

experience:1 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-tataatsu-idealabs-pvt-ltd-bengaluru-bangalore-1-to-3-yrs-jobid-S5XtOGDDD0RzpSvf__PLUS__uAgZw==&bc=+&sequence=18





job_count:19

company_name : Parahit Technologies Limited

key_skills : ['python', 'django', 'json', 'html', 'ajax', 'javascript']

Location:Delhi

experience:0 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-parahit-technologies-limited-delhi-0-to-3-yrs-jobid-j6NKVNIrw0hzpSvf__PLUS__uAgZw==&bc=+&sequence=19





job_count:20

company_name : Techasoft Pvt Ltd

key_skills : ['python', 'javascript', 'docker', 'django', 'postgresql', 'oops', 'mysql', 'mongodb', 'opencv']

Location:Bengaluru / Bangalore

experience:0 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-techasoft-pvt-ltd-bengaluru-bangalore-0-to-3-yrs-jobid-a7yPAxSxElFzpSvf__PLUS__uAgZw==&bc=+&sequence=20        





job_count:21

company_name : innefu labs pvt. ltd.

key_skills : ['python', 'database', 'django', 'neo4j', 'mining', 'web crawling']

Location:Delhi,  Delhi/NCR

experience:4 - 5  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-innefu-labs-pvt-ltd-delhi-delhi-ncr-4-to-5-yrs-jobid-3__SLASH__KteZt0ABFzpSvf__PLUS__uAgZw==&bc=+&sequence=21  





job_count:22

company_name : pegasus knowledge solutions india pvt ltd.

key_skills : ['python', 'css', 'django', 'java', 'html', 'bootstrap', 'api', 'jquery', 'sql']

Location:Bengaluru / Bangalore

experience:0 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-pegasus-knowledge-solutions-india-pvt-ltd-bengaluru-bangalore-0-to-3-yrs-jobid-__SLASH__TcxSk101ZVzpSvf__PLUS__uAgZw==&bc=+&sequence=22





job_count:23

company_name : AxisTechnolabs

key_skills : ['python', 'django', 'html5', 'team player', 'angularjs', 'javascript']

Location:Ahmedabad

experience:1 - 4  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-axistechnolabs-ahmedabad-1-to-4-yrs-jobid-u0tOEanhg39zpSvf__PLUS__uAgZw==&bc=+&sequence=23





job_count:24

company_name : AxisTechnolabs

key_skills : ['python', 'css', 'user interaction', 'bootstrap', 'openerp', 'database', 'xml', 'oops', 'html']

Location:Ahmedabad

experience:0 - 1  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-axistechnolabs-ahmedabad-0-to-1-yrs-jobid-oQxb__SLASH__TVWjxlzpSvf__PLUS__uAgZw==&bc=+&sequence=24





job_count:25

company_name : LAKSH HUMAN RESOURCE

key_skills : ['rest', 'python', 'django', 'git']

Location:Mumbai

experience:1 - 3  Years

salary_or_ctc:As per Industry Standards

company_link : https://m.timesjobs.com/mobile/job-detail/python-developer-laksh-human-resource-mumbai-1-to-3-yrs-jobid-ak3vdW639qBzpSvf__PLUS__uAgZw==&bc=+&sequence=25



**5. Project Structure**
Explanation of the files and directories.(not complex)

**6. Future Enhancements (Optional)**
Planned improvements or additional features : "Planning to filter the jobs based on the job title"

**7. Disclaimer** 
**web scraping policies:**
. Check the Website’s Terms of Service (ToS)

. Use Robots.txt for Guidance

. Avoid Overloading the Server

. Do Not Scrape Personal or Sensitive Data

. Use APIs Where Available

. Attribution and Ethical Use

**Disclaimer**
This project is for educational purposes only.
By using this scraper, you acknowledge responsibility for ensuring compliance with all applicable laws and website policies.
I am not liable for any misuse or legal issues arising from scraping activities.
