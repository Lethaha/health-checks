# health-checks
script that checks the health of computers

This will be populated with lots of fancy  checks.


*git config --global credential.helper cache*

Allow us to configure the credential helper to allow automated login to Github we can also use create SSH Key-pair.


*git clone URL*

Git clone is used to clone a remote repository into a local workspace

*git push*

Git push is used to push commits from your local repo to a remote repo

*git pull*

Git pull is used to fetch the newest updates from a remote repository 

*git remote show origin OR git remote -v*

get information about the remote/ see remote and local branches too


*git branch -r*

remote branches that our repo is currently tracking


*git remote* 

Lists remote repos

*git remote -v*

List remote repos verbosely

*git remote show <name>*

Describes a single remote repo

*git remote update*

Fetches the most up-to-date objects

*git fetch*

Downloads specific objects

*git branch -r*

Lists remote branches; can be combined with other branch arguments to manage remote branches


  
  
## pull merge and push cycle
  try git push
  
  if fail: to the following
  *git pull*
  pull changes in remote
  
  if conflict
  resolve conflict by editting file and then doing a git add followed by a git commit which will merge changes. the git push successfully.
  
  
  *git log --graph --oneline --all*
  show the graph of logs with remote and local
  
*git log -p origin/main*
 show all logs in remote repository
  
  ## pushing remote branches
  *git checkout -b refactor*
  create and check out new branch on local repo
  
  *git commit -a -m 'creat wrappter function for check_disk_full'*
  commit changes
  
  *git push -u origin refactor*
  push branch to remote repository to allow collaborators to check code before merge with main. the -u is for upstream   
  
  ## Rebasing Your Changes
  
  This makes debugging easier and prevents three-way merges by transferring the completed work from one branch to another.


