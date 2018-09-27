import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

import asyncio

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_REPO = os.getenv("GITHUB_REPO")


CLOSING_COMMENT = """Hi, I'm closebot! I'm closing this issue (automatically) to keep things tidy.

If you feel like this is in error, please @mention one of the maintainers.
"""


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, GITHUB_USER, oauth_token=os.getenv("GH_AUTH"))
        print(gh)
        # Make closing comment.
        # Close the issue.
        # https://api.github.com/repos/octocat/Hello-World/issues/comments/1


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
