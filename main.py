import requests
from requests.exceptions import ProxyError, ConnectTimeout, ConnectionError
import random
import csv
import os
import time

def getHeaders():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.aliexpress.com',
        'priority': 'u=1, i',
        'referer': 'https://www.aliexpress.com/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
    }
    return headers


def getParams(productId, pageNum, pageSize):
    params = {
        'productId': productId,
        'lang': 'en_US',
        'country': 'DZ',
        'page': str(pageNum),
        'pageSize': str(pageSize),
        'filter': 'all',
        'sort': 'complex_default',
    }
    return params

def getProxy():
    proxies = []
    # Ensure all operations are within the "with" block
    with open("http_proxies.txt", 'r') as f:  # Open the file
        reader = csv.DictReader(f)  # Create the CSV reader
        for row in reader: 
            if row['protocol'] == 'http':
                proxy_ip = row['ip']
                proxy_port = row['port']

                http_proxy = f"http://{proxy_ip}:{proxy_port}"
                https_proxy = f"https://{proxy_ip}:{proxy_port}"

                proxies.append({
                    'http': http_proxy,
                    'https': https_proxy
                })
    # The file is closed here
    return proxies  # Return the list of proxies

def rotateProxy(proxyList):
    while True:
        proxy = random.choice(proxyList)
        if not isProxyWorking(proxy):
            print("Proxy is not working, rotating to antother")
            continue
        print("Proxy is working")
        break
    return proxy

def isProxyWorking(proxy):
    test_url = "https://www.amazon.com/"

    try:
        response = requests.get(test_url, proxies=proxy, timeout=5)

        if 200 <= response.status_code < 300:
            return True  
        else:
            return False 
    except (ProxyError, ConnectTimeout, ConnectionError):
        return False

def requestData(productId, pageNumber, pageSize, numOfPages):
    for page in range(1, numOfPages):
        print("Page"+ str(page))
        while True:
            try:
                response = requests.get('https://feedback.aliexpress.com/pc/searchEvaluation.do', params=getParams(productId, pageNumber, pageSize), headers=getHeaders())
                print("Request Succeed: " + str(response.status_code))
            except (ProxyError, ConnectTimeout, ConnectionError):
                print("Request failed")
                continue
            break
        data = response.json()

        # Extracting features:
        for reveiw in data['data']['evaViewList']:
            try:
                buyerName = reveiw["buyerName"].strip()
            except:
                buyerName = None
            try:
                buyerCountry = reveiw["buyerCountry"].strip()
            except:
                buyerCountry = None
            try:
                Evaluation = reveiw["buyerEval"]
            except:
                Evaluation = None
            try:
                buyerFeedback = reveiw["buyerFeedback"].strip()
            except:
                buyerFeedback = None
            try:
                buyerProductFeedBack = reveiw["buyerProductFeedBack"].strip()
            except:
                buyerProductFeedBack = None
            try:
                buyerTranslationFeedback = reveiw["buyerTranslationFeedback"].strip()
            except:
                buyerTranslationFeedback = None
            try:
                downVoteCount = reveiw["downVoteCount"]
            except:
                downVoteCount = None
            try:
                upVoteCount = reveiw["upVoteCount"]
            except:
                upVoteCount = None
            try:
                evalDate = reveiw["evalDate"].strip()
            except:
                evalDate = None
            try:
                evaluationId = reveiw["evaluationId"]
            except:
                evaluationId = None
            try:
                responsiveness = reveiw["reviewLabelValue1"]
            except:
                responsiveness = None
            try:
                warrantyService = reveiw["reviewLabelValue2"]
            except:
                warrantyService = None
            try:
                functionality = reveiw["reviewLabelValue3"]
            except:
                functionality = None
            try:
                status = reveiw["status"]
            except:
                status = None
            print(buyerName)
            saveToCsv(buyerName, buyerCountry, Evaluation, buyerFeedback, buyerProductFeedBack, buyerTranslationFeedback, downVoteCount, upVoteCount, evalDate, evaluationId, responsiveness, warrantyService, functionality, status)
            print("Data Saved Successfuly")
        time.sleep(3)
          
def saveToCsv(buyerName, buyerCountry, Evaluation, buyerFeedback, buyerProductFeedBack, buyerTranslationFeedback, downVoteCount, upVoteCount, evalData, evaluationId, responsiveness, warrantyService, functionality, status):
    
    if not os.path.exists("Reviews.csv"):
        # Open the file in append mode
        with open("Reviews.csv", 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile,delimiter="|")  
            csv_writer.writerow(['buyerName', 'buyerCountry', 'Evaluation', 'buyerFeedback', 'buyerProductFeedBack', 'buyerTranslationFeedback', 'downVoteCount', 'upVoteCount', 'evalData', 'evaluationId', 'responsiveness', 'warrantyService', 'functionality', 'status'])
    with open("Reviews.csv", 'a', newline='', encoding='utf-8') as csvfile:
        # Write the data to the CSV file
        csv_writer = csv.writer(csvfile, delimiter="|")
        csv_writer.writerow([buyerName, buyerCountry, Evaluation, buyerFeedback, buyerProductFeedBack, buyerTranslationFeedback, downVoteCount, upVoteCount, evalData, evaluationId, responsiveness, warrantyService, functionality, status])


def main():
    # productId = input("Inter the product Id: ")
    # pageNumber = int(input("Inter the page number: "))
    # pageSize = int(input("Inter the page size: "))
    # numOfPages = int(input("Inter the number of pages: "))
    productId = "1005006074818290"
    pageNumber = 1
    pageSize = 50
    numOfPages = 30

    requestData(productId, pageNumber, pageSize, numOfPages)


if __name__ == "__main__":
    main()