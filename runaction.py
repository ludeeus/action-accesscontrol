"""
https://github.com/ludeeus/actions/
"""
import os
import sys
from github import Github

ACL = {
    "admin": ["admin", "write", "read"],
    "write": ["write", "read"],
    "read": ["read"],
}

ACTION_LEVEL = os.environ.get("ACTION_LEVEL")
GITHUB_ACTOR = os.environ.get("GITHUB_ACTOR")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

if ACTION_LEVEL is None:
    print("ACTION_LEVEL is missing")
    sys.exit(1)

if ACTION_LEVEL not in ACL:
    print(ACTION_LEVEL, "is not one of", ACL.keys())

if ACTION_LEVEL is None:
    print("GITHUB_TOKEN is missing")
    sys.exit(1)

try:
    GH = Github(GITHUB_TOKEN)
    REPO = GH.get_repo(os.environ.get("GITHUB_REPOSITORY"))
    ACTOR_ACCESS = REPO.get_collaborator_permission(GITHUB_ACTOR)
    if ACTOR_ACCESS in ACL[ACTION_LEVEL]:
        ACCESSGRANTED = True
except:
    ACCESSGRANTED = False

if ACCESSGRANTED:
    sys.exit(0)
else:
    print(GITHUB_ACTOR, "does not have", ACTION_LEVEL, "access")
    sys.exit(78)
