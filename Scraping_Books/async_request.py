import aiohttp
import asyncio  
import time

async def fetch_page(session, url):
    page_start = time.time()
    # async with aiohttp.ClientSession() as session:
        #Methods with an async keyword may have a yield method in __enter__, __exit__, or both methods.
        #New methods are __aenter__ and __aexit__.
    async with session.get(url) as response:
        print(f'Page took {time.time() - page_start} seconds to complete.')
        return response.status
        
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop = loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks
        # await grouped_tasks
        # return grouped_tasks

loop = asyncio.get_event_loop()
urls = ['https://www.google.com/' for i in range(50)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'All took {time.time() - start} seconds to complete.')