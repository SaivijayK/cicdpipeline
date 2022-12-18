from github import Github
import time
import os
import pytz
from datetime import datetime,timezone

# token = os.environ.get("token")
# print(token)
g = Github("")

repositary = g.get_repo("SaivijayK/Flask-application-One")

developmentBranch = repositary.get_branch("dev")

latest_sha = developmentBranch.commit.sha

commit = repositary.get_commit(sha = latest_sha)

commitDate = commit.commit.author.date
# print(commitDate)
commitDate = commitDate.replace(tzinfo=timezone.utc)

present = datetime.now(pytz.timezone('UTC'))
# print(present.time())

minutes = (present-commitDate).total_seconds()/60

if(minutes<5):
    print("new commit found")
    os.system(".\script.bat")