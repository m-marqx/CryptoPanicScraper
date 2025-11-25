import asyncio
from api_news_scraper import CryptoPanicScraper

async def main():
    scraper = CryptoPanicScraper(
        filter='all',
        limit=10000,
        # topic='BTC',
        save_path='news_data',
        # jina_api_key='jina_4d7479b1a43542138c177e3e3a76f7c7RgVhcuusmPIdTaGzSVumpW_Zf3Gi',
        max_retries=5,
    )

    await scraper.run()

if __name__ == "__main__":
    asyncio.run(main())