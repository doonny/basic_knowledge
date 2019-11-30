# 20个最常用的 Git 命令用法说明及示例

    git config
    git init
    git clone
    git add
    git commit
    git diff
    git reset
    git status
    git rm
    git log
    git show
    git tag
    git branch
    git checkout
    git merge
    git remote
    git push
    git pull
    git stash

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
    用法：git reset –hard [commit]
    该命令将丢弃所有的历史记录，并回滚到指定的提交。
    ```bash
    dee@dee-Latitude:~/Documents/basic_knowledge$ git reset --hard 425fb563154d91c9e4d5eae57c2529cbd26919ee
    HEAD is now at 425fb56 git_note.md edited
    ```
9. git rm
    用法：git rm [file]
    该命令将删除工作目录中的文件，并将删除动作添加到stage。


