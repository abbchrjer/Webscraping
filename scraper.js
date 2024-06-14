// importing neccessary modules
const puppeteer = require('puppeteer');
var fs = require('fs');

// async function
(async () => {

    // declaring url to scrape and path to cookieblocking chrome extension
    const EXT = 'C:\\Users\\21chrjer\\Puppeteer\\web-scraping-med-puppeteer-abbchrjer\\EXT';

    // launching browser with extension enabled to bypass cookies
    const browser = await puppeteer.launch({
        headless: true,
        args: [
        `--disable-extensions-except=${EXT}`,
        `--load-extension=${EXT}`,
        `--enable-automation`,
        ],
    });
    const page = await browser.newPage();

    // get amount of pages on site
    const url = 'https://www.hemnet.se/till-salu/vasteras-kommun/vasteras?page=1';
    await page.goto(url); 
    let element = await page.waitForXPath('//*[@id="result"]/div[1]/div/div/div[5]/a');
    let pages = await page.evaluate(element => element.textContent, element);

    // loop through all pages of real estate for sale and store attributes in data list
    data = []
    for (k=1; k<=pages; k++){
        // goto right url
        const url = 'https://www.hemnet.se/till-salu/vasteras-kommun/vasteras?page='+k;
        await page.goto(url); 

        // loop through right amount of li tags
        let liCount = await page.$eval('ul.qa-organic-results', el => el.childElementCount)
        for (i=1; i<=liCount; i++){
            console.log(i)

            // if ads or other irrelevant list objects continue
            let element = await page.waitForXPath('/html/body/div[4]/div/div[6]/div[1]/div[2]/ul/li['+i+']/@class');
            let content = await page.evaluate(element => element.textContent, element);

            if (content.replace(/^\s+|\s+$/gm,'') != 'normal-results__hit js-normal-list-item') continue
            
            // scrape real estate address, description, property type, attributes and link using xpath and evaluate
            element = await page.waitForXPath('//*[@id="result"]/ul/li['+i+']/a/div[2]/div/div[1]/div/h2');
            let address = await page.evaluate(element => element.textContent, element);
            address = address.replace(/^\s+|\s+$/gm,'')
            
            element = await page.waitForXPath('//*[@id="result"]/ul/li['+i+']/a/div[2]/div/div[3]/p');
            let desc = await page.evaluate(element => element.textContent, element);
            
            element = await page.waitForXPath('//*[@id="result"]/ul/li['+i+']/a/div[2]/div/div[1]/div/div/span[1]');                      
            let type = await page.evaluate(element => element.textContent, element); 
            type = type.replace(/^\s+|\s+$/gm,'')
            type = type.substring(0, type.length/2)
            
            let attributes = []
            for (j=1; j<4; j++){
                let element = await page.waitForXPath('//*[@id="result"]/ul/li['+i+']/a/div[2]/div/div[2]/div[1]/div['+j+']');
                let content = await page.evaluate(element => element.textContent, element);
                content = content.replace(/^\s+|\s+$/gm,'')
                attributes.push(content)
            }
    
            element = await page.waitForXPath('//*[@id="result"]/ul/li['+i+']/a/@href');
            let link = await page.evaluate(element => element.textContent, element);
            
            // element = await page.waitForXPath('/html/body/div[4]/div/div[6]/div[1]/div[2]/ul/li[67]/a/div[1]/div/img/@src');
            // let img = await page.evaluate(element => element.textContent, element);
            // console.log(img)
            
            // convert data and attributes to a json object and push to datalist
            var property = {
                type: type,
                desc: desc,
                price: attributes[0],
                size: attributes[1],
                rooms: attributes[2],
                location: address,
                link: link,
            }
            data.push(property)
        }}

    // writing the collected json-data to json file
    fs.writeFile ("data.json", JSON.stringify(data), function(err) {
        if (err) throw err;
        console.log('complete');
        }
);
    // closing browser
    browser.close();
})()