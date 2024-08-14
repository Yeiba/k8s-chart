git config
Usage: git config –global user.name “[name]”  

Usage: git config –global user.email “[email address]”

git init
Usage: git init [repository name]

git clone
Usage: git clone [url]  

git add
Usage: git add [file] 
Usage: git add * 

git commit
Usage: git commit -m “[ Type in the commit message]”  
Usage: git commit -a 

git diff
Usage: git diff  
Usage: git diff –staged
Usage: git diff [first branch] [second branch] 

git reset
Usage: git reset [file] 
Usage: git reset [commit] 
Usage: git reset –hard [commit]

git status
Usage: git status  

git rm
Usage: git rm [file] 

git log
Usage: git log  
Usage: git log –follow[file]  

git show
Usage: git show [commit]

git tag
Usage: git tag [commitID] 

git branch
Usage: git branch
Usage: git branch [branch name]  
Usage: git branch -d [branch name]

git checkout
Usage: git checkout [branch name]  
Usage: git checkout -b [branch name]  

git merge
Usage: git merge [branch name] 

git remote
Usage: git remote add [variable name] [Remote Server Link] 
git remote remove origin


git push
Usage: git push [variable name] master
Usage: git push [variable name] [branch]
Usage: git push –all [variable name]
Usage: git push [variable name] :[branch name]  

git pull
Usage: git pull [Repository Link]

git stash
Usage: git stash save
Usage: git stash pop
Usage: git stash list
Usage: git stash drop

echo "# Terraform" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Yeiba/Terraform.git
git push -u origin main

git remote add origin https://github.com/Yeiba/Terraform.git
git branch -M main
git push -u origin main