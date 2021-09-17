# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from colorama import Fore, Style
from config.banner import bn

os.system('cls')

if os.path.isdir("output"):
    pass
else:
    os.system('mkdir output')

print(bn)
keyword_search = input(f"{Fore.CYAN}[{Style.RESET_ALL}:{Fore.CYAN}]{Style.RESET_ALL} Enter something to {Fore.CYAN}search{Style.RESET_ALL} for: ")
total_keywords = int(input(f"\n{Fore.CYAN}[{Style.RESET_ALL}:{Fore.CYAN}]{Style.RESET_ALL} Enter {Fore.CYAN}maximum {Style.RESET_ALL}number of keywords to fetch: "))
output_file = input(f"\n{Fore.CYAN}[{Style.RESET_ALL}?{Fore.CYAN}]{Style.RESET_ALL} Enter the {Fore.CYAN}name{Style.RESET_ALL} of the output file? ")
print_keywords = input(f"\n{Fore.CYAN}[{Style.RESET_ALL}?{Fore.CYAN}]{Style.RESET_ALL} Print the {Fore.CYAN}output{Style.RESET_ALL} keywords? ")
# Main System:

opts = webdriver.FirefoxOptions()
opts.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options = opts)
driver.get('https://keywordshitter.com/')
text_area = driver.find_element_by_id('input')
text_area.send_keys(keyword_search)
start_job = driver.find_element_by_id('startjob')
start_job.click()
keyword_div = driver.find_element_by_id('numofkeywords')
shouldLoop = True
keywords_list = list
while(shouldLoop):
    keyword_count_text = keyword_div.text.split(':')
    keyword_count_1 = int(keyword_count_text[0])
    keyword_count_2 = int(keyword_count_text[1])
    if(keyword_count_1 >= total_keywords or keyword_count_2 >= total_keywords):
        start_job.click()
        stop_alert = driver.switch_to.alert
        stop_alert.dismiss()
        shouldLoop = False
        data = text_area.get_attribute('value')
        keywords_list = data.split('\n')
        keywords_list = [i for i in keywords_list if(len(i.strip())!=0)]
        driver.close()


yes_response = ["y", "Y", "yes", "YES", "ye", "YE", "yea", "YEA", "yup", "YUP"]
if print_keywords in yes_response:
    x = 0
    for k in keywords_list:
        print(f"{Fore.CYAN}[{Style.RESET_ALL}{x}{Fore.CYAN}]{Style.RESET_ALL} {k}")
        x += 1
        with open(f"output//{output_file} - {total_keywords}.txt", "a", encoding="utf-8") as kwfile:
            kwfile.write(f"{k}\n")
            kwfile.close()

else:
    for k in keywords_list:
        with open(f"output//{output_file} - {total_keywords}.txt", "a", encoding="utf-8") as kwfile:
            kwfile.write(f"{k}\n")
            kwfile.close()