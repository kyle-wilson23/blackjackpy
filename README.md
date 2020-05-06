# blackjackpy

Using the repo:
On your computer, find a nice folder to put your projects. I like to have a folder called 'sandbox' where all my git repos live locally

1. On the top right of this page, click the green clone button. Copy the URL to the clipboard
2. In your terminal, 'cd' into the parent folder where you want the project to live
3. Execute 'git clone <pasted_url>'. This should download a blackjackpy folder to the parent folder containing the files in this repository
4. Open the blackjackpy folder in VS code

Branching:
For smaller projects, this probably isn't very necessary but it's a really good practice to prevent multiple developers sharing one repository from stepping on each other's toes too much.

1. From the blackjackpy folder, run 'git branch <branch_name>'. For my work on this project I will choose a branch name of "kyle-blackjackpy". By default, the main branch will be called master when you clone this repository. What we've done is create a child branch off of master. This is yours and yours only at this point. Nobody can see or use this branch. It is a local branch.
2. If someone else has made changes and pushed them up to master (there will be notes on pushing and merging below), you can get the latest changes/updates to master by:
    - git checkout master
    - get pull (fetches latest changes)
    - git checkout <your_branch_name>
    - git merge master

Making changes:
1. 'cd' into the blackjackpy folder in your terminal and checkout your branch
2. Code away
3. In your terminal, run a 'git status'. This should show your changed files in red
4. Run 'git add <file_path>' to stage individual files, or 'git add .' to stage all changed files for commit
5. Running a 'git status' now should show your staged files in green
6. Run 'git commit -m "<informative_commit_message"'. Using the -m flag here allows us to add a message to our commit. This is useful when tracking the change history of files. A good example is something simple like "added logic to sort hand"
7. Now run 'git push'. After this command finishes, you have pushed your changes and branch to the server. Via this repository, I could find your branch name and check it out and see what you've done if I wanted.

I wanna jump back for a second and try to explain why we're branching a little better. There are these little things called merge conflicts that we will inevitably come across. They happen when two different developers make changes to the same lines in the same file, and then they both try to push their changes. Whoever loses this race will have to deal with the conflict - git just doesn't know whats going on when multiple changes occur to the same line from different sources. Luckily VS code has a great visual way of dealing with merge conflicts.

Here's the thing, though, we want to deal with merge conflicts on our local branch - they can be kinda hairy and cause bugs... it's easy to make a mistake when fixing them. If you can consider the parent master branch as our shared, production, working copy... we don't want to be fixing conflicts there. Its better to do everything from simple changes to resolving conflicts on our local branches, test, and then push to master when you're confident things are correct and working. Less of a problem for a simple python program, but imagine fixing a merge conflict in a large codebase for a full-scale application in the master branch where things are user facing - and something goes wrong - you don't want to be responsible for catastrophe.

Moving on...

Another useful command is 'git stash'. Use this if you have anything in progress that you want to 'save' before making a commit. its useful when you're not ready to submit your work, but need to switch branches. When you're ready to return, git stash apply will bring these changes back. Not a great idea to rely on too much though.

TL;DR of reccomended git flow:
git branch, git checkout your branch, do your work, git add, git commit, git checkout master, git pull (to get latest), git checkout your branch, git merge master (to merge latest with your recent work and ensure no conflicts or bugs), git checkout master, git merge your branch, git push

I know this all seems overwhelming, but git can be a life-saver. I don't think these practices need to be used much for this project, but if we start making larger-scale fun things this can be very useful. You'll be happy to know there is a side menu in VS code that provides a UI for managing all of this too and makes things easier :)
