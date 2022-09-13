import requests
import re

FLAG = False


def url_to_domain(url):
    return re.findall(r"://([^/]+)/?", url)[0]


def global_rank(num):
    to_num = float(num)
    if to_num > 0 and to_num < 100000:
        return 1
    else:
        return -1


def page_rank(num):
    to_num = float(num)
    if (to_num <= 0.35):
        return -1
    else:
        return 1


def alexa_rank_page_rank(url):

    domain = url_to_domain(url)

    api = "https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D="

    response = requests.get(api + domain, headers={'API-OPR': '8goss84kwsgc4scg4gwksw8004ggkcsk808os80c'})
    response = response.json()

    data = response["response"][0]
    page_rank = data["page_rank_decimal"]
    alexa_rank = data["rank"]

    return alexa_rank, page_rank


def web_traffic(url):

    domain = url_to_domain(url)
    url_web_archive = "https://web.archive.org/__wb/calendarcaptures/2?url="

    url_to_search = domain + "&date=2020&groupby=day"
    url = url_web_archive + url_to_search

    response = requests.get(url)
    json_data = response.json()

    try:
        if (len(json_data["items"]) > 0):
            return 1
    except:
        return -1


def print_debug(*argv):
    if(FLAG):
        print(argv)


def prediction_result(value):
    prediction = value[0]

    if prediction == 1:
        return '{"message": "URL is safe"}'
    elif prediction == -9:
        return '{"message": "The following website doesnt allow to run the program or its down"}'
    else:
        return '{"message": "URL is not safe, traces of Phishing detected"}'
