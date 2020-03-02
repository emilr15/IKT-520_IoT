# IKT-520_IoT
Repository for our assignments in IoT.

## Contributing

Note: local means on your own machine, remote means the "github cloud"/online repository/branch.

#### 1. Clone repository

Open command with git integrated or Git Bash, navigate to the directory you would like to ceate project and clone from this repository.
Or, use PyCharm to make a new project from GitHub.
**NB! The commands underneath are meant for git bash (using '/' instead of '\' path)**

```
cd <path to directory you want the repository>
git clone https://github.com/emilr15/IKT-520_IoT.git
```

#### 2. Checkout branch
Keep your changes in a new branch.
If it's a fix start its name with "fix/..." or if it's a feature, start its name with "feature/..."

Create a new branch:
```
git checkout -b <branch name>
```

Switch between existing branches:
```
git checkout <name of another existing branch>
```

#### 3. Get latest changes

Get latest changes from repo (for example if someone else has committed and pushed something):
The git fetch command downloads commits, files, and refs from a remote repository into your local repo. Fetching is what you do when you want to see what everybody else has been working on without merging it into your own local branch.
```
git fetch
``` 
Git pull is to merge the fetched content into your own branch, if no branch is specified you will merge the remote changes from your own branch. 
```
git pull <branch name>
```

#### 4. Push your latest changes to the library (to your remote branch)

**Add files to commit:**
```
git add <path/to/file 1> <path/to/file 2> <path/to/file 3>
```
Add all new changed files to commit:
```
git add -A
```
Alternative:
```
git add .
```

**Commit your changes**

This means that you will save your changes on your local branch, the remote branch will still have the same content:
```
git commit -m "message: should be what a short summary of the changes you made in this commit"
```

**Push the changes to the remote repository:**
```
git push origin <branch name>
```

`git push -u origin <branch name>` will make an upstream which means you just have to write "git push" next time when working on the same branch. 

### In PyCharm
Make your changes. Hit Ctrl(cmd) + K to commit (& push) your changes to GitHub.

#### 3. Make a PR (Pull Request)

Create a PR to merge your changes to master, this is done from the repository at Github.
