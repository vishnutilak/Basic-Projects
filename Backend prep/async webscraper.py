import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url, timeout=10) as resp:
        return await resp.text()

async def scrape(urls):
    async with aiohttp.ClientSession() as sess:
        tasks = [asyncio.create_task(fetch(sess,u)) for u in urls]
        return await asyncio.gather(*tasks)

# usage:
# urls = ["https://example.com","https://python.org"]
# asyncio.run(scrape(urls))
