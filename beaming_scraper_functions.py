from selenium.webdriver.common.by import By
import time

def find_state_webpages(driver):
    states_list_element = driver.find_element(By.XPATH, "//div[contains(@class, 'find-service-block state')]")
    list_of_states = states_list_element.find_elements(By.XPATH, ".//a[@class = 'b-item_link']")
    list_of_state_webpages = []
    for state in list_of_states:
        state_webpage = state.get_attribute('href')
        list_of_state_webpages.append(state_webpage)
    return list_of_state_webpages

def find_city_webpages(driver):
    city_list_element = driver.find_element(By.XPATH, "//div[contains(@class, 'find-service-block city')]")
    list_of_cities = city_list_element.find_elements(By.XPATH, ".//a[@class = 'b-item_link']")
    list_of_city_webpages = []
    for city in list_of_cities:
        city_webpage = city.get_attribute('href')
        list_of_city_webpages.append(city_webpage)
    return list_of_city_webpages

def find_provider_webpages(driver):
    list_of_providers = driver.find_elements(By.XPATH, "//div[@class = 'doctors-card']")
    list_of_provider_webpages = []
    for provider in list_of_providers:
        provider_webpage_element = provider.find_element(By.XPATH, ".//a[@class = 'name']")
        provider_webpage = provider_webpage_element.get_attribute('href')
        list_of_provider_webpages.append(provider_webpage)
    return list_of_provider_webpages

def find_provider_information(driver):
    try:
        driver.find_element(By.XPATH, "//div[@class = 'is-closed-block']")
        information_panel_element = driver.find_element(By.XPATH, "//div[@class = 'personal-info-block']")
        provider_name_element = information_panel_element.find_element(By.XPATH, ".//h1[@class = 'b-title']")
        provider_name = provider_name_element.get_attribute('textContent')
        print(provider_name, 'is closed')

    except:
        information_panel_element = driver.find_element(By.XPATH, "//div[@class = 'personal-info-block']")

        #find name of provider
        provider_name_element = information_panel_element.find_element(By.XPATH, ".//h1[@class = 'b-title']")
        provider_name = provider_name_element.get_attribute('textContent')
        print(provider_name)

        #find website of provider
        try:
            provider_website_element = driver.find_element(By.XPATH, "//a[contains(@class, 'social-button v-btn v-btn--fab v-btn--outlined v-btn--round theme--light v-size--x-small')]")
            provider_website = provider_website_element.get_attribute('href')
            print(provider_website)
        except:
            print('There is no website listed')

        #find address of provider
        try:
            provider_address_element_shell = information_panel_element.find_element(By.XPATH, ".//ul[@class = 'list-under-title']")
            provider_address_element = provider_address_element_shell.find_element(By.TAG_NAME, 'li')
            provider_address_long = provider_address_element.get_attribute('textContent')
            if 'Address: ' not in provider_address_long:
                provider_address = 'There is no address listed'
            else:
                provider_address_shortened = provider_address_long.replace('Address: ', '')
                provider_address_shortened = provider_address_shortened.replace('\n', ' ')
                provider_address = provider_address_shortened.replace('           ', ' ')
            print(provider_address)
        except:
            print('There is no address listed')

        #find care settings
        try:
            care_settings = []
            care_settings_list_element = driver.find_element(By.XPATH, "//div[contains(@class, 'doctor-other-information-row info-row settings')]")
            list_of_care_settings = care_settings_list_element.find_elements(By.XPATH, ".//li[@class = 'b-other-info-list_item']")
            for care_setting_element in list_of_care_settings:
                care_setting_long = care_setting_element.get_attribute('textContent')
                care_setting_shortened = care_setting_long.replace('\n', '')
                care_setting = care_setting_shortened.replace(' ', '')
                care_settings.append(care_setting)
            print(care_settings)
        except:
            print('There are no care settings listed')

        #find accepted insurance
        try:
            insurance_care_providers = []
            care_providers_list_element = driver.find_element(By.XPATH, "//ul[@class = 'insurance-list']")
            list_of_care_providers = care_providers_list_element.find_elements(By.XPATH, ".//li[@class = 'insurance-list__item']")
            for care_provider_element in list_of_care_providers:
                care_provider = care_provider_element.get_attribute('textContent')
                insurance_care_providers.append(care_provider)
            for index, care_provider in enumerate(insurance_care_providers):
                if 'See More' in care_provider:
                    insurance_care_providers.pop(index)
                    #send click to see more element and gather that list
                    see_more_button_element = care_providers_list_element.find_element(By.XPATH, ".//span[@class = 'see-more-button']")
                    see_more_button_element.click()
                    list_of_extra_providers = driver.find_elements(By.XPATH, "//li[@class = 'insurance-name']")
                    for extra_provider_element in list_of_extra_providers:
                        extra_provider_long = extra_provider_element.get_attribute('textContent')
                        if '\n' in extra_provider_long:
                            extra_provider_long = extra_provider_long.replace('\n', '')
                        if '        ' in extra_provider_long:
                            extra_provider_long = extra_provider_long.replace('        ', '')
                        if '      ' in extra_provider_long:
                            extra_provider = extra_provider_long.replace('      ', '')
                        insurance_care_providers.append(extra_provider)
            print(insurance_care_providers)
        except:
            print('There are no insurance providers listed')



        print('\n')
    
