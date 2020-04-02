from bs4 import BeautifulSoup
from requests import get

from data.models import StateData

MOHFW_URL = 'https://www.mohfw.gov.in/'

def get_state_data():
    try:
        response = get(url=MOHFW_URL)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        table = html_soup.find_all('table')
        trs = table[0].find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            try:
                if tds:
                    obj, created = StateData.objects.get_or_create(
                                                state=tds[1].text, 
                                                defaults={
                                                    'total_confirmed_cases': int(tds[2].text),
                                                    'total_recovered': int(tds[3].text),
                                                    'total_death': int(tds[4].text)
                                                })
                    if created:
                        obj.total_confirmed_cases = int(tds[2].text)
                        obj.total_recovered = int(tds[3].text)
                        obj.total_death = int(tds[4].text)
                        obj.save()

            except IndexError:
                continue
        return True        
    except Exception as e:
        print(e)
        return False
