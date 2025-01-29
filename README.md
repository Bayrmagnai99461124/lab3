Admin@219-13 MINGW64 /c/Users/admin
$ cd lab2

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ ls
jishee-1.py

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git status
On branch master
nothing to commit, working tree clean

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   jishee-1.py

no changes added to commit (use "git add" and/or "git commit -a")

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git add .

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   jishee-1.py


Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git config --global user.nmae "Bayrmagnai99461124"

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git config --global user.email "bayrmagnai.1124@gmail.com"

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git config --global user.name "Bayrmagnai99461124"

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git config --global user.email "bayrmagnai.1124@gmail.com"

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git commit -m "magnai"
[master 720f7cc] magnai
 1 file changed, 5 insertions(+)

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git remote add origin ^C

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git remote add origin https://github.com/Bayrmagnai99461124/lab3.git
error: remote origin already exists.

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git remote -v
origin  https://github.com/Bayrmagnai99461124/lab3.git (fetch)
origin  https://github.com/Bayrmagnai99461124/lab3.git (push)

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 318 bytes | 318.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Bayrmagnai99461124/lab3.git
   ccf0b3a..720f7cc  master -> master

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ code ..

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ touch jishee-2.py

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ ls
jishee-1.py  jishee-2.py

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ code .

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        jishee-2.py

nothing added to commit but untracked files present (use "git add" to track)

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        jishee-2.py

nothing added to commit but untracked files present (use "git add" to track)

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git add .

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   jishee-2.py


Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git config --global user.name "Bayrmagnai99461124"

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git config --global user.email "bayrmagnai.1124@gmail.com"

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git commit -m "magnai"
[master c1e4bd7] magnai
 1 file changed, 13 insertions(+)
 create mode 100644 jishee-2.py

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git remote add origin ^C

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git remote add origin https://github.com/Bayrmagnai99461124/lab3.git
error: remote origin already exists.

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git remote -v
origin  https://github.com/Bayrmagnai99461124/lab3.git (fetch)
origin  https://github.com/Bayrmagnai99461124/lab3.git (push)

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 490 bytes | 25.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Bayrmagnai99461124/lab3.git
   720f7cc..c1e4bd7  master -> master

Admin@219-13 MINGW64 /c/Users/admin/lab2 (master)
$
