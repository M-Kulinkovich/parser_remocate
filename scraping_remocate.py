import re
import time
from datetime import timedelta
from datetime import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data_pattern_engl import params


def convert_date_to_timestamp(date_string):
    keywords = {
        'today': timedelta(days=0),
        'yesterday': timedelta(days=1),
        'ago': None
    }

    days_match = re.search(r'(\d+)\s+days', date_string)
    if days_match:
        days_ago = int(days_match.group(1))
        timedelta_obj = timedelta(days=days_ago)
    else:
        timedelta_obj = timedelta()

    for keyword, delta in keywords.items():
        if keyword in date_string.lower():
            if delta is not None:
                timedelta_obj += delta
            break

    timestamp = int((datetime.now() - timedelta_obj).timestamp())
    return timestamp


class RemocateGetInformation:
    def __init__(self):
        self.url = "https://www.remocate.app/"
        self.categories = ['Support', 'UX/UI', 'HR', 'QA', 'Analytics', 'Design', 'Development', 'Marketing']

    def get_data(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(self.url)

        while True:
            while True:
                driver.execute_script("window.scrollBy(0, 2500);")
                time.sleep(0.5)
                current_height = driver.execute_script("return window.pageYOffset;")
                full_height = driver.execute_script("return document.documentElement.scrollHeight;")
                window_height = driver.execute_script("return window.innerHeight;")
                if current_height + window_height >= full_height:
                    break

            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card")))
            vacancies = driver.find_elements(By.CLASS_NAME, "job-card")

            for vacancy in vacancies:
                try:
                    category_element = vacancy.find_element(
                        By.CSS_SELECTOR,
                        "div.job-card-bubble[fs-cmsfilter-field='category']"
                    )

                    # deleting emoji ------------------------------------------
                    category_emoj = category_element.text.strip()
                    category = re.sub(r'[^a-zA-Z]', '', category_emoj)
                    if category not in self.categories:
                        continue

                    vacancy_link = vacancy.get_attribute("href")

                    driver.execute_script("window.open(arguments[0])", vacancy_link)
                    driver.switch_to.window(driver.window_handles[-1])

                    # get title -------------------------------
                    title = driver.find_element(By.CSS_SELECTOR, ".job-top-title").text.strip()

                    # get vacancy URL -------------------------------
                    vacancy_url = vacancy_link

                    # get body -------------------------------
                    try:
                        body_elements = driver.find_elements(By.CSS_SELECTOR, "div.job-description.w-richtext")
                        body = ' '.join(element.text.strip() for element in body_elements)
                    except NoSuchElementException:
                        body = ""

                    # get company -------------------------------
                    company = driver.find_element(By.CLASS_NAME, "job-top-company").text.strip()

                    # get job_type and relocation -------------------------------
                    job_info = driver.find_element(By.CLASS_NAME, "job-top-tags").text.strip()
                    job_info = re.sub(r'[^a-zA-Z]', ' ', job_info).split()
                    relocation = ""
                    for tags in job_info:
                        if tags == "Remote":
                            job_type = "Remote"
                        elif tags == "Relocation":
                            relocation = "Relocation"
                        else:
                            job_type = ""

                    # get date -------------------------------
                    date = driver.find_element(By.CLASS_NAME, "job-top-right").text.strip()
                    date = convert_date_to_timestamp(date)

                    # get english -------------------------------
                    english = ''
                    if re.findall(r'[Аа]нглийский', body, re.IGNORECASE) or re.findall(r'[Ee]nglish', body):
                        english_additional = ''
                        for item in params['english_level']:
                            matches = re.findall(rf"{item}", body, re.IGNORECASE)
                            for match in matches:
                                english_additional += f"{match}"

                        if re.search(r'\b(intermediate|upper|b1|b2|pre)\b', english_additional, re.IGNORECASE):
                            english = english_additional.strip()

                    if not english and (
                            re.findall(r'[Аа]нглийский', body, re.IGNORECASE) or re.findall(r'[Ee]nglish', body)):
                        english = 'English'

                    # get city -------------------------------
                    city_info = driver.find_element(By.CLASS_NAME, "job-top-tags").text.strip().split()
                    city = ''
                    for tag in city_info:
                        if tag in params['country_list']:
                            city = tag
                            break

                    # get salary --------------------------
                    salary = ''
                    for line in body.split('\n'):
                        if re.search(r'\b[sS]alary\b', line):
                            salary = line

                    # get experience --------------------------
                    experience = ''
                    for line in body.split('\n'):
                        if re.search(r'\b[Ee]xperience&[Yy]ear|[Yy]ears\b', line):
                            experience = line
                        elif re.search(r'\b[Ee]xperience\b', line):
                            experience = line

                    results_dict = {
                        'chat_name': self.url,
                        'title': title,
                        'body': body,
                        'vacancy': title,
                        'vacancy_url': vacancy_url,
                        'company': company,
                        'english': english,
                        'relocation': relocation,
                        'job_type': job_type,
                        'city': city,
                        'salary': salary,
                        'experience': experience,
                        'time_of_public': date,
                    }

                    for key, value in results_dict.items():
                        print(f"{key}: {value if value else ''}")
                    print()

                except NoSuchElementException:
                    continue

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            driver.quit()


if __name__ == "__main__":
    parser = RemocateGetInformation()
    parser.get_data()
