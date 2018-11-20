1. Перед тем, как начать изменять что-то:  
   1. Перейдите из своей ветки в мастер:
   ```sh
   git checkout master
   ```
   2. Выгрузите из мастера все изменения:
   ```sh
   git pull --rebase
   ```
   (можно без rebase - погуглите, в чем разница, ибо мне просто говорили, что лучше с ним)
   3. Перейдите обратно в свою ветку:
   ```sh
   git checkout <your_branch>
   ```
   (Если вы забыли, как называется ваша ветка - `git branch` ; создать новую ветку - `git branch <branch_name>`)
   4. Замержите мастер к себе в ветку:
   ```sh
   git merge master
   ```
2. Сделали какие-то изменения в своей ветке
3. Чтобы закинуть все это в репозиторий:
   1. git status - посмотреть, что изменилось (красное - изменилось и нет в коммитах, зеленое - добавлено для коммита). На самом деле, малоинформативно, ибо после запуска игры изменяется куча всего
   2. `git add *` - если все надо закинуть, `git add <file1> <file2>` etc - если только определенные файлы (файлы можно прям из вывода status копировать)
   3. `git commit -m "<commit_message>"` - если не хотите головной боли с добавлением мессаджа через вим, не забывайте про -m. Мессадж обязателен
   4. `git push`
4. Дальше переходим непосредственно на гитхаб в репозиторий
5. Обновите страницу или откройте репозиторий
6. Там будет что-то типа "Compare & create merge request"
7. Нажать
8. Создать запрос на мердж в мастер, опционально и желательно (особенно для крупных и финальных изменений) - добавить в репортеры всех остальных девелоперов
9. Если в запросе стоит, что конфликтов нет и можно мерджить, и назначенные девелоперы все посмотрели, мержить через кнопку
10. Если есть конфликты: (из своей ветки)
  	 1. `git fetch`
    2. `git merge origin/master`
    3. It will complain about conflicts. Edit the files to resolve them. You'll need to take the changes made to the conflicting file upstream (you can use `git diff HEAD...MERGE_HEAD` to see what they are) and migrate them onto your version.
    4. Use `git add` to mark files with changes that should be committed (probably just readme.txt) and `git rm` to mark files that should be removed 
    5. `git commit`
    6. `git push`
