# python-learning
The repository consists of Python snippets created during my journey to learn Python
# Initialize the repository
git init
# branch creation and changed to develop
git branch -m develop
# add the remote branch on local for the github folder
git remote add origin https://github.com/tusartak20-dotcom/python-learning.git
# add the tracker on local for the github folder
git branch --set-upstream-to=origin/<branch> develop
# add the files
git add .
# commit the changes
git commit -m "Initial commit"
# Push the changes to github
git push -u origin develop
# pull the changes
git pull
# pull the changes and rebase
git pull --rebase
