# -*- coding: utf-8 -*-
import re
import urllib, json
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Event, Office, News


def parse_vacancy(save):
    company = Company.objects.get(alias='lohika')
    url = 'https://cube.lohika.com/0/ServiceModel/JobPosting.svc/vacancies?page=1&locations=&categories='
    response = urllib.urlopen(url)
    file = json.loads(response.read())
    vacancies = file['vacancies']
    for vacancy in vacancies:
        print vacancy['title']
        name = vacancy['title']
        description = vacancy['jobPurpose'].encode('utf-8') + '\n' \
                      + 'Optional knowledge: %s ' % vacancy['optionalKnowledge'] + '\n' \
                      + 'Required knowledge: %s' % vacancy['requiredKnowledge']
        short_text = 'if vacancy is hot ==> %s' % vacancy['isHot']
        # short_text1 = 'if vacancy is hot ==> {vacancy}'.format(vacancy=vacancy['isHot'])
        url = vacancy['recruiters']
        date = vacancy['publishedDate']
        programming_language = vacancy['tags']
        vacancy_obj, created = Vacancy.objects.get_or_create(name=name, company=company)
        vacancy_obj.alias = re.sub(" ", "-", name.lower())
        vacancy_obj.description = description
        vacancy_obj.url = url
        vacancy_obj.extra = short_text
        vacancy_obj.date = date
        vacancy_obj.save()


# parse.html is empty. nothing to parse
def parse_offices(save):
    company = Company.objects.get(alias='lohika')
    Office.objects.get_or_create(name='Kiev office',
                                 city='Kiev',
                                 company=company,
                                 latitude=50.434043,
                                 longiitude=30.509147,
                                 address='35 Zhylianska Street,5 floor',
                                 phone='0445938080',
                                 email='job_kyiv@lohika.com')
