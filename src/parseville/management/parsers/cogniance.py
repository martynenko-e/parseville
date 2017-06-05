# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Office, Event


def parse_vacancy(save):
    soup = get_soup_from_url('http://cogniance.com/careers/', save)
    if soup:
        vacancy_elements = soup.find('div', class_='careers-list'). \
            find('ul', class_='locations-position').findAll('li', class_='careers-item col')
        if vacancy_elements:
            for vacancy in vacancy_elements:
                vacancy_url = vacancy.a['href']
                vacancy_title = vacancy.strong.text
                soup = get_soup_from_url(vacancy_url, False)
                if soup:
                    desc = soup.find('div', class_='col-profile-left col')
                    card = soup.find('h1', class_='modal-title')
                    if card:
                        title = card.find('strong', id='job-position').text
                        city = card.find('div', id='job-location').text
                        lang = ''
                        print title, city, lang
                        comp = Company.objects.get(alias='cogniance')

                        vacancy_obj, created = Vacancy.objects.get_or_create(name=title, company=comp)
                        vacancy_obj.alias = re.sub(' ', '-', title.lower())
                        vacancy_obj.description = desc.encode('utf-8')
                        vacancy_obj.url = vacancy_url
                        vacancy_obj.extra = city + ' languages ' + lang
                        vacancy_obj.save()


def parse_offices(save):
    company = Company.objects.get(alias='cogniance')
    soup = get_soup_from_url('http://cogniance.com/get-in-touch/', save)
    if soup:
        office_list_kyiv = soup.find('div', class_='popover_list').find('div', id='kyiv')
        if office_list_kyiv:
            office = office_list_kyiv.find('address')
            office_name = office.find('h3').text
            office_city = office.find('h3').text
            office_address = office.findAll('h4')[0].text
            office_email = office.findAll('h4')[3].find('a', class_='external').text
            Office.objects.get_or_create(name=office_name,
                                         city=office_city,
                                         company=company,
                                         latitude=02,
                                         longtitude=03,
                                         address=office_address,
                                         phone=03,
                                         email=office_email
                                         )


def parse_events(save):
    company = Company.objects.get(alias='cogniance')
    soup = get_soup_from_url('http://cogniance.com/insights/', save)
    if soup:
        events_list = soup.find('div', class_='all_events').findAll('div', class_='event')
        if events_list:
            for event in events_list:
                event_date = event.findAll('div')[0].find('span', class_='event-month') + ' of ' + event.findAll('div')[
                    0].find('span', class_='event-day')
                event_name = event.find('strong').find('a').text
                event_description = 'wo nada'
                event_short_text = 'taki nada'
                event_url = event.find('strong').a['href']
                Event.objects.get_or_create(company=company,
                                            name=event_name,
                                            date=event_date,
                                            description=event_description,
                                            short_text=event_short_text,
                                            url=event_url)
# news fly over like shifaner under the Paris