from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

from fetchAutocomplete import *

# Connects over Tor
PROXY = "127.0.0.1:8118"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://google.com")

countries = ["United States","日本","中国","Deutschland","France","United Kingdom","Italia","Россия","España","Brasil","Canada","Canada","India","भारत","México","Australia","대한민국","Nederland","Türkiye","Polska","Indonesia","België","Belgique","Belgien","Suisse","Schweiz","Svizzera","Sverige","العربية السعودية","Norge","Österreich","臺灣","Ελλάδα","Danmark","ایران","Argentina","Venezuela","South Africa","ประเทศไทย","Suomi","Ireland","Éire","الامارات","Portugal","Colombia","Malaysia","Česká republika","香港","Nigeria","ישראל","إِسْرَائِيلُ‎","România","新加坡","Украина","Україна","Chile","Philippines","Pilipinas","Pakistan","پاکِستان","مَصْر","الجزائر","دولة الكويت","Magyarország","Қазақстан","Қазақия,","Қазақ Елі","قازاقستان","Казахстан","New Zealand","Perú","قطر","Slovensko","العراق","ليبيا","Việt Nam","المغرب‎","Angola","বাংলাদেশ","Hrvatska","Беларусь","Беларусь","عمان‎","السودان","Sudan","سورية‎","Luxembourg","Luxemburg","Lëtzebuerg","Ecuador","Slovenija","Србија","Srbija","България","Lietuva","Azərbaycan","Азәрбајҹан","آذربايجان","República Dominicana","تونس‎","Tunisie","ශ්රී ලංකා","இலங்கை","Guatemala","Latvija","Uruguay","Costa Rica","Kenya","Kenya","لُبْنَان‎","Liban","Ўзбекистон","Узбекистан","اليَمَن","ኢትዮጵያ","Κύπρος","Kıbrıs","Trinidad and Tobago","Cameroon","Cameroun","Eesti","Côte d’Ivoire","Panamá","El Salvador","مملكة البحرين","الأردن‎","Jordan","Tanzania","Tanzania","Guinée Équatoriale","Guiné Equatorial","Guinea Ecuatorial"]

lower_bar = driver.find_element_by_class_name("fbar").text

for country in countries:
	if country in lower_bar:
		country_IP = country

print(country_IP)

getGoogleTranslate(driver, country_IP).fetch()
getGoogleSearch(driver, country_IP).fetch()
getYandex(driver, country_IP).fetch()
getBing(driver, country_IP).fetch()
getYahoo(driver, country_IP).fetch()

driver.close()
