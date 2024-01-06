from selenium.webdriver.common.by import By

def find_state_webpages(list_of_states):
    list_of_state_webpages = []
    for state in list_of_states:
        state_webpage = state.get_attribute('href')
        list_of_state_webpages.append(state_webpage)
    return list_of_state_webpages

def find_city_webpages(list_of_cities):
    list_of_city_webpages = []
    for city in list_of_cities:
        city_webpage = city.get_attribute('href')
        list_of_city_webpages.append(city_webpage)
    return list_of_city_webpages

def find_provider_webpages(list_of_providers):
    list_of_provider_webpages = []
    for provider in list_of_providers:
        provider_webpage_element = provider.find_element(By.XPATH, ".//a[@class = 'name']")
        provider_webpage = provider_webpage_element.get_attribute('href')
        list_of_provider_webpages.append(provider_webpage)
    return list_of_provider_webpages

def find_provider_information(list_of_provider_webpages):
    name = ''
    website = ''
    address = ''
    insurance_care_providers = []
    care_settings = []
    