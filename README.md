## Courses

# Product List

(endpoint)
```
/api/products/
```

# Lessons List 

(endpoint)
```
/api/lessons/?product_id=<id>
```

# Register User

```
/auth/register/
```

# Sign In User

```
/auth/login/
```


- [x] 1. Создать сущность продукта. У продукта должен быть создатель этого продукта(автор/преподаватель). Название продукта, дата и время старта, стоимость **(1 балл)**

- [x] 2. Определить, каким образом мы будем понимать, что у пользователя(клиент/студент) есть доступ к продукту. (2 балл)

- [x] 3. Создать сущность урока. Урок может принадлежать только одному продукту.. В уроке должна быть базовая информация: название, ссылка на видео. (1 балл)

- [x] 4. Создать сущность группы. По каждому продукту есть несколько групп пользователей, которые занимаются в этом продукте. Минимальное и максимальное количество юзеров в группе задается внутри продукта. Группа содержит следующую информацию: ученики, которые состоят в группе, название группы, принадлежность группы к продукту (2 балла)

- [x] 1. При получении доступа к продукту, распределять пользователя в группу. Если продукт ещё не начался, то можно пересобрать группы так, чтобы везде было примерно одинаковое количество участников.
    
    По-умолчанию алгоритм распределения должен работать заполняя до максимального значения
- [x] +3 балла дается за реализацию алгоритма распределения по группам так, чтобы в каждой группе количество участников не отличалось больше, чем на 1. При этом, минимальные и максимальные значения участников в группе должны быть учтены.

- [x] 2. Реализовать API на список продуктов, доступных для покупки, которое бы включало в себя основную информацию о продукте и количество уроков, которые принадлежат продукту. (2 балла)

- [x] 3. Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ. (1 балл).