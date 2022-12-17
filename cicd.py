from github import Github
import time
import os
import pytz
from datetime import datetime
g = Github("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")

repositary = g.get_repo("SaivijayK/Flask-application-One")

developmentBranch = repositary.get_branch("dev")

latest_sha = developmentBranch.commit.sha

commit = repositary.get_commit(sha = latest_sha)

commitDate = commit.commit.author.date

present = datetime.now(pytz.timezone('GMT'))

if(present.timestamp()-commitDate.timestamp()<5*60*60):
    print("new commit found")
    os.system(".\pushandpull.bat")