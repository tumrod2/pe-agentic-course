from github import Github
import os

def create_github_issue(title: str, body: str):
    github_token = os.environ.get("GITHUB_TOKEN")
    github_repo = os.environ.get("GITHUB_REPO")
    user_name =os.environ.get("GITHUB_USER_NAME")
    g = Github(github_token)

    repo = g.get_repo(github_repo)
    issue = repo.create_issue(
        title=title,
        body=body,
        assignees=[user_name],
        labels=["bug", "high-priority"]
    )

    print(f"Issue created successfully: {issue.html_url}")
