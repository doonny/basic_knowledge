# 20个最常用的 Git 命令用法说明及示例

## 设置SSH
1. 生成公钥
    ```bash
    ssh-keygen -t rsa -C "youremail@example.com"
    ```
2. 将公钥添加到github等等托管平台上

## Git 命令
1. git config
    用法：git config –global user.name “[name]”  
    用法：git config –global user.email “[email address]”
    该命令将分别设置提交代码的用户名和电子邮件地址。
    ```bash
    dee@dee-Latitude:~$ git config --global user.name "dezengzang"
    dee@dee-Latitude:~$ git config --global user.email "dezengzang@outlook.com"
    ```

2. git init
    用法：git init [repository name]
    该命令可用于创建一个新的代码库。
    ```bash
    dee@dee-Latitude:~$ git init ~/Documents/DEMO
    Initialized empty Git repository in /home/dee/Documents/DEMO/.git/
    ```

3. git clone
    用法：git clone [url]
    该命令可用于通过指定的URL获取一个代码库。
    ```bash
    dee@dee-Latitude:~/Documents$ git clone https://github.com/doonny/basic_knowledge
    Cloning into 'basic_knowledge'...
    remote: Enumerating objects: 79, done.
    remote: Counting objects: 100% (79/79), done.
    remote: Compressing objects: 100% (57/57), done.
    remote: Total 79 (delta 23), reused 68 (delta 15), pack-reused 0
    Unpacking objects: 100% (79/79), done.
    ```

4. git status
    用法：git status
    该命令将显示所有需要提交的文件
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git status 
    On branch master
    Your branch is up to date with 'origin/master'.

    Untracked files:
    (use "git add <file>..." to include in what will be committed)

        git_note.md

    nothing added to commit but untracked files present (use "git add" to track)
    ```

5. git add
    用法：git add [file]
    该命令可以将一个文件添加至stage(暂存区)。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git add git_note.md
    ```
    用法：git add *
    该命令可以将多个文件添加至stage(暂存区)。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git add *
    ```

6. git commit
    用法：git commit -m “[ Type in the commit message]”  
    该命令可以在版本历史记录中永久记录文件。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git commit -m "git_note.md added"
    [master e1226c5] git_note.md added
    1 file changed, 80 insertions(+)
    create mode 100755 git_note.md
    ```
    用法：git commit -a
    该命令将提交git add命令添加的所有文件，并提交git add命令之后更改的所有文件。 
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git commit -a -m "git_note.md edited"
    [master 12b077e] git_note.md edited
    1 file changed, 16 insertions(+)
    ```

7. git diff
    用法：git diff
    该命令可以显示尚未添加到stage的文件的变更。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git diff
    diff --git a/git_note.md b/git_note.md
    index 37354bd..aa46d56 100755
    --- a/git_note.md
    +++ b/git_note.md
    @@ -97,5 +97,8 @@
        1 file changed, 16 insertions(+)
        ```
    
    +7. git diff
    +    用法：git diff
    +    该命令可以显示尚未添加到stage的文件的变更。
    ```
    用法：git diff --staged
    该命令可以显示添加到stage的文件与当前最新版本之间的差异。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git diff --staged
    diff --git a/git_note.md b/git_note.md
    index 685f456..0afb41b 100755
    --- a/git_note.md
    +++ b/git_note.md
    @@ -117,7 +117,6 @@
    -
    +        这里添加一句话
    ```
    用法：git diff [first branch] [second branch]
    该命令可以显示两个分支之间的差异。

8. git reset
    用法：git reset [file]
    该命令将从stage中撤出指定的文件，但可以保留文件的内容。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git reset git_note.md
    Unstaged changes after reset:
    M	git_note.md
    ```
    用法：git reset [commit]
    该命令可以撤销指定提交之后的所有提交，并在本地保留变更。([commit]可以使用git log查到)
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git reset 425fb563154d91c9e4d5eae57c2529cbd26919ee
    Unstaged changes after reset:
    M	git_note.md
    ```

    用法：git reset --hard [commit]
    该命令将丢弃所有的历史记录，并回滚到指定的提交。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git reset --hard 425fb563154d91c9e4d5eae57c2529cbd26919ee
    HEAD is now at 425fb56 git_note.md edited
    ```
9. git rm
    用法：git rm [file]
    该命令将删除工作目录中的文件，并将删除动作添加到stage。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git rm example.txt 
    rm 'example.txt'
    ```
10. git log
    用法：git log
    该命令可用于显示当前分支的版本历史记录。 
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git log
    commit 9db87d7e15506fad3e3c5333116090b7f4478bd5 (HEAD -> master)
    Author: dezengzang <dezengzang@outlook.com>
    Date:   Sat Nov 30 15:18:08 2019 +0800

        example.txt deleted

    commit 56b20dd9b39ddf65da4ab0465dd8a06b845d33c6
    Author: dezengzang <dezengzang@outlook.com>
    Date:   Sat Nov 30 15:17:23 2019 +0800

        add example.txt
    ```
    用法：git log --follow[file]
    该命令可用于显示某个文件的版本历史记录，包括文件的重命名。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git log --follow git_note.md
    commit a5ea2257c7fd8f1dc504d3bdd76f2e0916809315
    Author: dezengzang <dezengzang@outlook.com>
    Date:   Sat Nov 30 15:16:49 2019 +0800

        add example.txt
    ```
11. git show
    用法：git show [commit]
    该命令经显示指定提交的元数据以及内容变更。
    ```
    dee@dee-Latitude:~/Documents/basic_knowledge$ git show 9db87d7e15506fad3e3c5333116090b7f4478bd5
    commit 9db87d7e15506fad3e3c5333116090b7f4478bd5 (HEAD -> master)
    Author: dezengzang <dezengzang@outlook.com>
    Date:   Sat Nov 30 15:18:08 2019 +0800

        example.txt deleted

    diff --git a/example.txt b/example.txt
    deleted file mode 100644
    index ce01362..0000000
    --- a/example.txt
    +++ /dev/null
    @@ -1 +0,0 @@
    -hello
    ```
12. git tag
    用法：git tag [commitID]
    该命令可以给指定的提交添加标签。
13. git branch
    用法：git branch
    该命令将显示当前代码库中所有的本地分支。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git branch
    * master
    ```
    用法：git branch [branch name]
    该命令将创建一个分支。
    ```
    dee@dee-Latitude:~/Documents/basic_knowledge$ git branch branch1
    ```
    用法：git branch -d [branch name]
    该命令将删除指定的分支。
    ```bashrc
    dee@dee-Latitude:~/Documents/basic_knowledge$ git branch -d branch1 
    Deleted branch branch1 (was 9db87d7).
    ```
14. git checkout
    用法：git checkout [branch name]
    你可以通过该命令切换分支。
    ```
    dee@dee-Latitude:~/Documents/basic_knowledge$ git checkout branch2 
    M	git_note.md
    Switched to branch 'branch2'
    ```
    用法：git checkout -b [branch name] 
    你可以通过该命令创建一个分支，并切换到新分支上。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git checkout -b branch3
    M	git_note.md
    Switched to a new branch 'branch3'
    ```
15. git merge
    用法：git merge [branch name]
    该命令可以将指定分支的历史记录合并到当前分支。
    ```
    dee@dee-Latitude:~/Documents/basic_knowledge$ git merge branch3
    Already up to date.
    ```
16. git remote
    用法：git remote add [variable name] [Remote Server Link]
    你可以通过该命令将本地的代码库连接到远程服务器。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git remote add origin1 git@github.com:doonny/basic_knowledge.git
    ```
17. git push
    用法：git push [variable name] master
    该命令可以将主分支上提交的变更发送到远程代码库。
    ```
    dee@dee-Latitude:~/Documents/basic_knowledge$ git push origin master 
    Enumerating objects: 20, done.
    Counting objects: 100% (20/20), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (18/18), done.
    Writing objects: 100% (19/19), 3.31 KiB | 1.66 MiB/s, done.
    Total 19 (delta 11), reused 0 (delta 0)
    remote: Resolving deltas: 100% (11/11), completed with 1 local object.
    To https://github.com/doonny/basic_knowledge
    2b2a690..9db87d7  master -> master
    ```
    用法：git push [variable name] [branch]
    该命令可以将指定分支上的提交发送到远程代码库。
    ```bash
    git push origin branch1
    ```
    用法：git push --all [variable name]
    该命令可以将所有分支发送到远程代码库。
    ```bash
    git push --all origin
    ```
    用法：git push [variable name] :[branch name]
    该命令可以删除远程代码库上的一个分支。
    ```bash
    git push origin :branch1
    ```
18. git pull
    用法：git pull [Repository Link]
    该命令将获取远程服务器上的变更，并合并到你的工作目录。
    ```bash
    (base) dee@dee-Latitude:~/Documents/basic_knowledge$ git pull
    Already up to date.
    ```
19. git stash
    用法：git stash save
    该命令将临时保存所有修改的文件。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git stash save 
    Saved working directory and index state WIP on master: 9db87d7 example.txt deleted
    ```
    用法：git stash pop
    该命令将恢复最近一次stash（储藏）的文件。
    ```bash
    git stash pop
    ```
    用法：git stash list
    该命令将显示stash的所有变更。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git stash list 
    stash@{0}: WIP on master: 9db87d7 example.txt deleted
    ```
    用法：git stash drop
    该命令将丢弃最近一次stash的变更。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git stash drop 
    Dropped refs/stash@{0} (72aec8b06c040b7f233f87734df587ef2e472af0)
    ```

 整理自[公众号CSDN](https://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650733891&idx=3&sn=ff358e64ec52838c7b030739579c567a&chksm=bea68c9089d10586178224580949fe432e3f033cba7bd748113baad89ff031d6cc901ccf34b7&mpshare=1&scene=23&srcid=&sharer_sharetime=1575079281233&sharer_shareid=ca4a235412dbd4ab62a02058c2d4d001#rd)（其实只有19个指令）

