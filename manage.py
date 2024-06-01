#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# ========================================================include====================================
# in include the header and footer are kept in separate html file and are included in each html file using {% include 'header.html'%}

# ===========================================================extends===================================
# in extends the header and footer remain static in one base.html file and the page content between them goes on changing 

# ================================================database=====================================
# we use sqlite3 database
# SQLite is a self-contained, serverless, zero-configuration, transactional SQL database engine. It doesn't require a separate server process to operate. Instead, the entire database is stored in a single disk file, making it easy to set up and use.

# MySQL follows a traditional client-server model where the database server process handles database operations, and clients connect to it over a network. This allows multiple clients to access the same database concurrently.
# create default table in db.sqlite3:python manage.py migrate
#create superuser:python manage.py createsuperuser
# to open admin pannel create superuser
# ==============================================================end end end =================================
# views take the data and render to the html page
# views and url is to be connected\

# =======================================git git git============================================

# when we add and commit the 'M' symbol before file disappear as the modified changes is reflected to local repository
# and U for untracted which is not added to the repository
# When you run git add ., you are staging changes for the next commit. 
# This command tells Git to add all changes in the current directory and its subdirectories to the staging area. 
# The staging area, also known as the index, is an intermediate place where changes are prepared before being committed to the repository(local).

# Operations: Commands like git add, git commit, git log, git status, and git diff operate within this local repository.
# When you run git commit, Git creates a new commit object in the local repository. This commit object represents a snapshot of the changes that have been staged in the index (staging area) and includes metadata about the commit.

# to link this local repository to remote repository:# Add a remote repository named "origin"
        #   git remote add origin https://github.com/username/repository.git
         # to verify:git remote -v
# to add and commit changes to local repository
        # git add .
        # git commit -m "Initial commit"
# to push the changes to remote repository
        # # Push to the "main" branch (or "master", depending on your default branch)
        #  git push -u origin main
        # When you use the -u option, you are telling Git to remember the remote branch (origin/main in this case) that your local branch (main) is tracking.
        # after doing this you can use Instead of git push origin main, you can simply use git push.next time
        # if you made any changes to the remote repository before pushing the files from local repo,you can first pull using (git pull origin main --allow-unrelated-histories) and again push
# The error message "remote origin already exists" indicates that a remote repository named origin has already been set for your local repository.
# if you want to set that origin for next repo do:
    #  git remote set-url origin https://github.com/anujtheboss/djangocontinues.git
# ==================================================end end end===============================================