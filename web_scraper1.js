const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch()
  const pages = await browser.pages()
  const currentPage = pages[0]
  const url = currentPage.url()
  console.log(url)
  await browser.close()
})()
