##### Install Scoop

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

##### Install pipx

scoop install pipx
pipx ensurepath

##### Install poetry
pipx install poetry
pipx ensurepath



https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit
https://medium.com/thelorry-product-tech-data/unit-testing-and-continues-integration-ci-in-github-action-for-python-programming-c8ad57fae3a1

:/