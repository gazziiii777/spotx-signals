import aiohttp
import asyncio


class BybitListingFetcher:
    def __init__(self):
        self.url = "https://api2.bybit.com/spot/api/v1/business/listing/list"

        self.headers = {
            "authority": "api2.bybit.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en",
            "origin": "https://www.bybit.com",
            "referer": "https://www.bybit.com/",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "cookie": '_abck=9DA6ABD12DB060416E730D3DBAE12204~0~YAAQj2pkX5ExnouWAQAAgSHCyg1gEzJ421fYip0gqY3NXu6zfyVCW8eJ/ArRCapYGlKBlffnySkNKEAYhBfHSCwb2GGlS0nM2yTGGuB2anDP3rfzu0oHlyMgb/CN9f4jmgtHDpyhSxx6fRd7af0irG6fuljplqwuR1HpkmjaMhRuADvzS2TCKyMEzm2uSCEiP3574x9be0WWPnFET++LRYHu3OGWbOu7v/Ep4SP65iWWh1BJeEfYG2d/iQBgE/YllfL8Gtyw78cxBWdxo5SHyCy6FsjuhrDxEstOgMMcKjFW4UCREt+UXuc0RQ8QoSGOvJ6fIXBzNOHT48a5qjkb/BXBnftc2hVjoR+AMO17rCAxjk0pQN/yJHfL6YfZFV8rv7P2KWPLwxsq7e61F1/KUqAhBZinXmuMEIojhmBxRapwXyqPr60ik/Gpc2+6M6XUzqoKqCd0vqlj70s/la/9icC…ZhbHNlLCJzaWQiOiJCWUJJVCJ9.ELWGsQPg-cYiiq2zMIhLPFWRgJ9RBWsvFKfzM5DTLEYKbtQGgZi_s7d9OKrqyal3Dqt9Vwd6sHBUTTB2VrFLaA; bm_mi=5E8F74DA9040DC0AE6DD3F74D5D53969~YAAQj2pkX1ornouWAQAA2OLByhvzzbhvL8kN5ZeA5NJaBjtkJz0y/VPsstqJ/QYP1vf7i+NvM1WzcWlWHOGpFQeFzVP36Gu9E3FYAI0wmvwY6dRT71p0jWArlI42lUvoIv4YX7mcE+gBkq66O/v95w7BYyhRzjkDNpbxhjF9H1IGn9gIBOF749QGNXwPsikfuoOrkNsGzNHYXBFiw7t7EdDjNRFIB59PLEEQTYrtRI5UYWLoU+spKvNenfx+zmEn8CsGWh9HIyYTc2vtz0pg70w3ilW1z1KYx+SX3PZzfZvurahQFft5FvQ0jDzpLcI30hvJAP5i+L9iVKOrAxZ40wwdxVJd80dfDA==~1'
        }

    async def fetch_json(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.url) as response:
                response.raise_for_status()
                answer = await response.json()
                return answer.get("result").get("ongoing").get("tokenSplash")

    async def get_listings(self):
        data = await self.fetch_json()
        return data


async def main():
    fetcher = BybitListingFetcher()
    data = await fetcher.get_listings()
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
