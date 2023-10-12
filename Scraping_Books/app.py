import requests
import logging
import aiohttp
import asyncio
import async_timeout
import time
from pages.all_books_page import AllBooksPage

logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG,
                    filename = 'logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get(f'https://books.toscrape.com/').content
page = AllBooksPage(page_content)

loop = asyncio.get_event_loop() 

books = page.books

async def fetch_page(session, url):
    page_start = time.time()
    # async with aiohttp.ClientSession() as session:
        #Methods with an async keyword may have a yield method in __enter__, __exit__, or both methods.
        #New methods are __aenter__ and __aexit__.
        
    #async with async_timeout.timeout(10): #Raises a Timeouterror after the given time in seconds.
    async with session.get(url) as response:
        print(f'Page took {time.time() - page_start} seconds to complete.')
        return await response.text()
        
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop = loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = [f'https://books.toscrape.com/catalogue/page-{page_num + 1}.html' 
        for page_num in range(1,page.page_count)]

start =time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All page requests took {time.time() - start} seconds to complete.')

for page_content in pages:
    logger.debug("Creating AllBooksPage from page content.")
    page = AllBooksPage(page_content)
    books.extend(page.books)

# for page_num in range(1,page.page_count):
#     url = f'https://books.toscrape.com/catalogue/page-{page_num + 1}.html'
#     page_content = requests.get(url).content
#     logger.debug("Creating AllBooksPage from page content.")
#     page = AllBooksPage(page_content)
#     books.extend(page.books)
