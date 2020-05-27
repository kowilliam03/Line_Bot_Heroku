# Line Bot Heroku
## 大綱
* [1. 註冊Heroku](#1.-註冊Heroku)
* [2. 註冊GitHub](#2.-註冊GitHub)
* [3. 上傳之前](#3.-上傳之前)
* [4. 部署專案](#4.-部署專案)


## 1. 註冊Heroku
前往[Heroku](https://id.heroku.com/login)註冊一組帳號。接著創建一個app。

> app名字必須是不重複的，因此可能要多試幾組，像linebot這樣的名字就已經被使用了。

## 2. 註冊GitHub
前往[GitHub](https://github.com)註冊一組帳號，之後我們會將完成的專案上傳到GitHub，然後透過Heroku提供的功能，將專案部署到Heroku上。

## 3. 上傳之前
在我們的專案上傳之前，我們需要新增幾個檔案。

**Procfile**

這個檔案是告訴Heroku，當我們將檔案上傳後，要怎麼啟動它。
> 因為需要用gunicorn，所以需要安裝這個套件

```procfile
web gunicorn app:app --preload
```

**runtime.txt**

這個文件是告訴Heroku，我們的專案指定要用哪個版本的Python。下方的案例為指定Python 3.7.7 版本。
```txt
python-3.7.7
```

**requirements.txt**
這個文件告訴Heroku，我們的專案要安裝哪些套件。由於之前說過了，所以不另外說明。

## 4. 部署專案
完成以上步驟後，就可以將專案上傳到GitHub，之後再藉由GitHub將專案部署到Heroku上了。