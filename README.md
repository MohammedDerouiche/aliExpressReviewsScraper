<div style="display: flex; justify-content: center;">
    <img src="https://logos-world.net/wp-content/uploads/2022/12/AliExpress-Logo.png" alt="AliExpress Logo" width="900">
</div>

# AliExpress Product Reviews Scraper

This project is a Python-based web scraper designed to extract reviews and feedback from AliExpress. It uses proxy rotation to avoid rate-limiting and provides functionalities for handling CSV files, among other features.
The .csv dataset resulted by this webscraper have several potential use cases like `EDA` and `Sentement Analysis` to Determine the overall sentiment from customer reviews. This can help gauge customer satisfaction, identify common issues, and understand product performance.

## Project Overview

The code contains functions to:

- Retrieve HTTP headers for web scraping.
- Generate dynamic parameters for request URLs.
- Rotate through a list of HTTP proxies.
- Check if proxies work with external websites (e.g., Amazon).
- Save extracted data to CSV files, with conditional creation of the CSV file and headers.

## Skills, Languages, and Libraries

This project employs the following skills, languages, and libraries:

- **Programming Language**: Python 3.x
- **Libraries**: 
  - `requests`: HTTP requests, including error handling with `ProxyError`, `ConnectTimeout`, and `ConnectionError`.
  - `csv`: Handling CSV file operations.
  - `random`: For proxy rotation.
  - `os`: To interact with the operating system for file checks.
  - `time`: For time-related operations.

- **Skills**: Web scraping, proxy rotation, error handling, CSV file manipulation, conditional logic, and exception handling.

## Extracted Features

The web scraper collects a variety of features from AliExpress reviews, providing a comprehensive dataset for analysis. The extracted features include:

- **buyerName**: The name or username of the buyer who submitted the review.
- **buyerCountry**: The country where the buyer is located.
- **Evaluation**: The overall evaluation or rating given by the buyer.
- **buyerFeedback**: The general feedback or comments from the buyer.
- **buyerProductFeedBack**: Specific feedback about the product.
- **buyerTranslationFeedback**: Feedback related to translation (if applicable).
- **downVoteCount**: The number of downvotes the review received.
- **upVoteCount**: The number of upvotes the review received.
- **evalData**: Additional data related to the evaluation.
- **evaluationId**: The unique identifier for the evaluation.
- **responsiveness**: The responsiveness rating for the product.
- **warrantyService**: The warranty or service rating.
- **functionality**: The functionality rating.
- **status**: The status of the review.


## Prerequisites

To run this project, you need:

- Python 3.x
- The libraries listed above
- A CSV file containing HTTP proxies (like `http_proxies.txt`), can be downloaded from [ProxyScrape](https://proxyscrape.com/free-proxy-list). Make sure to use proxies that is near to your location
- Note: The proxy rotator is disabled, which means that runing the code will send requests using your ip address. To prevent this, you can add the parameter `proxies`=`rotateProxy()` as an argument to the request function in line 86.

## Setup

1. Clone or download the repository.
2. Ensure Python and the required libraries are installed.
3. Place your `http_proxies.txt` file in the working directory. Ensure it has the correct format (with headers).

## Configuration

In the main script, you can customize the following variables based on your requirements:

- **productId**: The identifier for the AliExpress product you're scraping. Default: `"1005006074818290"` (can be found at the beggining URL of the product main page).
- **pageNumber**: The starting page for scraping. Default: `1`.
- **pageSize**: The number of reviews to fetch per page. Default: `50` (Don't increase the pageSize over then 50, it can lead to IP bans.
- **numOfPages**: The total number of pages to scrape. Default: `30`.

Adjust these values as needed for your specific use case.

## Running the Code

To run the scraper:

```bash
python main.py
