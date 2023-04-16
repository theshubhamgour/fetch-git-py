#This is to find the card from the specifed project  - for single card
from github import Github

# Access the repository using a Personal Access Token
ACCESS_TOKEN = "Here_Goes_the_TOKEN"
#Target the repository
REPO_NAME = "theshubhamgour/hotelbee"

#Specify the branch name
BRANCH_NAME = "release-4.4.4"

#Commit or Card you want to search
CARD_NAME = "EA-10080.txt"

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_NAME)
branch = repo.get_branch(BRANCH_NAME)

# Search for the file in the branch
contents = repo.get_contents("", ref=branch.commit.sha)
found = False
while contents and not found:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path, ref=branch.commit.sha))
    elif file_content.type == "file" and file_content.name == CARD_NAME:
        found = True
        print("Found file {} in branch {} of repository {}".format(CARD_NAME, BRANCH_NAME, REPO_NAME))

if not found:
    print("Could not find file {} in branch {} of repository {}".format(CARD_NAME, BRANCH_NAME, REPO_NAME))
