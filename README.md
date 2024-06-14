# Web Scraping Project using Puppeteer: Real Estate in Västerås

This project aims to scrape real estate data from hemnet (https://www.hemnet.se/) using Puppeteer, a Node.js library for automating web browsers. The scraped data will then be processed and plotted on a map for visual representation.

## Project Screenshot

![Project Screenshot](/project-screenshot.PNG)

## Requirements

To run this project, you need to have the following installed:

- Node.js
- Python

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/abbindustrigymnasium/web-scraping-med-puppeteer-abbchrjer.git

2. Install dependencies:

   ```bash
   cd <project-directory>
   npm i
   npm i puppeteer
   pip install folium geopy

3. Run the scraper:

    ```bash
    node scraper.js

4. Run the visualization:

    ```bash
    python map.py

## Additional Notes

- Ignore the Django-project.

- Please be aware that scraping large amounts of data and finding the location of the data for mapping can be time-consuming processes.

  - Estimated scraping time: approximately 1 minute and 30 seconds for 500 properties, depending on the amount of data being scraped.

  - Estimated mapping time: around 4 minutes for approximately 500 locations, depending on the amount of data being processed.

  Please note that these time estimates are approximate and can vary based on the size and complexity of the data being scraped and mapped.

- Ensure that you comply with the website's terms of service and do not overload the server with too many requests in a short period. Consider using delays or rate limiting to prevent excessive scraping.

- Remember to handle errors and exceptions gracefully. Puppeteer offers various error handling mechanisms, such as try-catch blocks or using `page.on('error')` and `page.on('pageerror')` events.                                                                                                                                      

- If the website requires user authentication or has additional security measures, you may need to modify the scraper accordingly.

## Contributing

Contributions are welcome! If you have any ideas or improvements for this project, please submit a pull request. Ensure that your changes align with the project's coding style and best practices.

<!-- ## License

This project is licensed under the [MIT License](LICENSE). -->

## Disclaimer

**Note:** Please be aware that web scraping may be subject to legal restrictions or terms of service imposed by the website being scraped. Ensure that you comply with all applicable laws and the website's terms of service when using this project. The authors of this project do not take any responsibility for the misuse or illegal use of the code.