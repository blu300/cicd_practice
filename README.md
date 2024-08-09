Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

scoop install pipx
pipx ensurepath

pipx install poetry

pipx ensurepath


https://medium.com/thelorry-product-tech-data/unit-testing-and-continues-integration-ci-in-github-action-for-python-programming-c8ad57fae3a1