# Статический сайт

Простой статический сайт (HTML + CSS + JavaScript) для практической работы №7.

## Локальный просмотр

Откройте `index.html` в браузере или запустите:

```powershell
cd static-site
python -m http.server 8000
```

Затем откройте http://localhost:8000.

## Публикация на GitHub Pages

1. В репозитории `homework IIT` откройте **Settings → Pages**.
2. В разделе **Build and deployment** выберите Source: **Deploy from a branch**.
3. Выберите ветку `gh-pages` и папку `/ (root)` (сайт лежит в корне этой ветки).
4. Сохраните. Ссылка на сайт появится в разделе Pages: `https://<логин>.github.io/homework%20IIT/` (либо `https://<логин>.github.io/homework-IIT/` в зависимости от имени репозитория).

Альтернатива: разместить содержимое папки `static-site/` в отдельной ветке `gh-pages` как её корень ( subtree).
