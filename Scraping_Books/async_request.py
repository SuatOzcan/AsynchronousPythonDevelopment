import aiohttp
import asyncio  
import time

async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        #Methods with an async keyword may have a yield method in __enter__, __exit__, or both methods.
        #New methods are __aenter__ and __aexit__.
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start} seconds to complete.')
            return response.status

loop = asyncio.get_event_loop()
tasks = [fetch_page('http://www.google.com') for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All took {time.time() - start} seconds to complete.')