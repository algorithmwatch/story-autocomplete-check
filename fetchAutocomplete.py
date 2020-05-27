from suggestion import Suggestion, db
from concepts import concepts
import time

class AutocompleteFetcher:
    def __init__(self, driver, country_IP):
        self.driver = driver
        self.db = db
        self.country_IP = country_IP
        self.onlyEnglish = False

    def getSearchBox(self):
        pass
    def getSuggestions(self):
        pass
    def doBeforeQuery(self):
        pass
    def doAfterPageLoad(self):
        pass

    def fetch(self):
        self.driver.get(self.url)

        self.doAfterPageLoad()

        for concept in concepts:
            for query in concept["queries"]:
                phrase = query["query"].format(concept = concept["name"])
                language = query["lang"]

                if not (self.onlyEnglish and language != "en"):
                
	                self.doBeforeQuery()

	                q = self.getSearchBox()

	                q.clear()

	                time.sleep(self.waitBeforeQuery)

	                # Type in the query
	                for letter in phrase:
	                    q.send_keys(letter)
	                    time.sleep(.05)
	                # Extract the suggestions
	                time.sleep(self.waitAfterQuery)
	                suggestions = self.getSuggestions()

	                # Stores the suggestions in the DB 
	                for suggestion in suggestions.text.split("\n") :
	                    Suggestion(concept=concept["name"]
	                             , phrase=phrase
	                             , suggestion=suggestion
	                             , language=language
	                             , country_IP=self.country_IP
	                             , service=self.service).save()


class getGoogleTranslate(AutocompleteFetcher):
    def __init__(self, driver, country_IP):
        AutocompleteFetcher.__init__(self, driver, country_IP)
        self.url = "https://translate.google.com/#view=home&op=translate&sl=en&tl=en"
        self.service = "Google Translate"
        self.waitBeforeQuery = 1
        self.waitAfterQuery = 3
        self.onlyEnglish = True

    def getSearchBox(self):
        return self.driver.find_element_by_id("source")
    
    def getSuggestions(self):
        return self.driver.find_element_by_id("gt-src-is")

class getGoogleSearch(AutocompleteFetcher):
    def __init__(self, driver, country_IP):
        AutocompleteFetcher.__init__(self, driver, country_IP)
        self.url = "https://google.com"
        self.service = "Google Search"
        self.waitBeforeQuery = .5
        self.waitAfterQuery = 1.5

    def getSearchBox(self):
        return self.driver.find_element_by_name("q")
    
    def getSuggestions(self):
        return self.driver.find_element_by_xpath("//ul[@role = 'listbox']")

class getYandex(AutocompleteFetcher):
    def __init__(self, driver, country_IP):
        AutocompleteFetcher.__init__(self, driver, country_IP)
        self.url = "https://yandex.ru/"
        self.service = "Yandex"
        self.waitBeforeQuery = 1
        self.waitAfterQuery = 2

    def getSearchBox(self):
        return self.driver.find_element_by_class_name("input__control")
    
    def getSuggestions(self):
        return self.driver.find_element_by_class_name("mini-suggest__popup")

class getBing(AutocompleteFetcher):
    def __init__(self, driver, country_IP):
        AutocompleteFetcher.__init__(self, driver, country_IP)
        self.url = "https://www.bing.com"
        self.service = "Bing Search"
        self.waitBeforeQuery = 2
        self.waitAfterQuery = 3

    def getSearchBox(self):
        return self.driver.find_element_by_id("sb_form_q")
    
    def getSuggestions(self):
        return self.driver.find_element_by_id("sw_as")

    def doBeforeQuery(self):
        self.driver.find_element_by_id("b_logo").click()

class getYahoo(AutocompleteFetcher):
    def __init__(self, driver, country_IP):
        AutocompleteFetcher.__init__(self, driver, country_IP)
        self.url = "https://search.yahoo.com/"
        self.service = "Yahoo Search"
        self.waitBeforeQuery = 1
        self.waitAfterQuery = 2

    def getSearchBox(self):
        return self.driver.find_element_by_id("yschsp")
    
    def getSuggestions(self):
        return self.driver.find_element_by_class_name("sa-sbx-container")

    def doAfterPageLoad(self):
        try:
            q = self.driver.find_element_by_id("yschsp")
        except Exception:
            self.driver.find_element_by_name("agree").click()
            self.driver.get("https://search.yahoo.com/")