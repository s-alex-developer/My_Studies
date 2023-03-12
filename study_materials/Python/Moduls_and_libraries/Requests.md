*Последние изменения внесены: `12.03.2023`*

# Requests в Python – Примеры выполнения HTTP запросов

* `Библиотека requests` является стандартным инструментом для составления **HTTP-запросов** в **Python**. 
* Простой и аккуратный **API** значительно облегчает трудоемкий процесс создания запросов.

Стоит взять на заметку сайт **httpbin.org**. 
   * Это чрезвычайно полезный ресурс, созданный человеком, который внедрил использование `requests` – *Кеннетом Рейтцом*.
   * Данный сервис предназначен для тестовых запросов. 
   * Здесь можно составить пробный запрос и получить ответ с требуемой информацией. 

## 1. Python установка `библиотеки requests`

Для начала работы потребуется установить библиотеку requests. Для этого используется следующая команда:

`pip install requests`


Сразу после установки requests можно полноценно использовать в приложении. Импорт requests производится следующим образом:
```python
import requests
```

## 2. Python библиотека `Requests` метод `GET`

* **GET** является одним из самых популярных **HTTP методов**. 
* Метод **GET** указывает на то, что происходит попытка извлечь данные из определенного ресурса. 
* Для того, чтобы выполнить запрос **GET**, используется `requests.get()`.

> Для проверки работы команд будем выполнять запрос в отношении **Root REST API** на **GitHub**.`

Выполним **запрос GET** в отношении указанного в скобках URL (вызовем `метод get()`):
```python
request.get('https://api.github.com')
```

* Если никакие python ошибки не возникло – первый запрос успешно выполнен. Далее будет рассмотрен ответ на данный запрос, который можно получить при помощи объекта `Response`.

## 3. Объект `Response` получение ответа на запрос в Python

* `Response` представляет собой довольно мощный объект для анализа результатов запроса. 
* В качестве примера будет использован предыдущий запрос, только на этот раз результат будет представлен в виде переменной.
* Таким образом, получится лучше изучить его атрибуты и особенности использования.

```python
import requests

response = requests.get('https://api.github.com')
```

* В данном примере при помощи `get(`) захватывается определенное значение, что является частью объекта `Response`, и помещается в переменную под названием **response**. 
* Теперь можно использовать переменную **response** для того, чтобы изучить данные, которые были получены в результате запроса **GET**.

## 4. HTTP коды состояний

* Самыми первыми данными, которые будут получены через `Response`, будут **коды состояния**. 
* **Коды состояния** сообщают о статусе запроса.
* Например, статус **200 OK** значит, что запрос успешно выполнен. А вот статус **404 NOT FOUND** говорит о том, что запрашиваемый ресурс не был найден. 
* Существует множество других статусных кодов, которые могут сообщить важную информацию, связанную с запросом.

### `.status_code`

* Используя `.status_code`, можно увидеть код состояния, который возвращается с сервера:


```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
```

    200
    

* `.status_code` вернул значение **200**. Это значит, что запрос был выполнен успешно, а сервер ответил, отобразив запрашиваемую информацию.

В некоторых случаях необходимо использовать полученную информацию для написания программного кода.

Например:


```python
import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
```

    Success!
    

* В таком случае, если с сервера будет получен код состояния **200**, тогда программа выведет значение **Success!**. Однако, если от сервера поступит код **404**, тогда программа выведет значение **Not Found**.

 Если использовать `Response` в условных конструкциях, то при получении кода состояния в промежутке от **200** до **400**, будет выведено значение **True**. В противном случае отобразится значение **False**:


```python
import requests

response = requests.get('https://api.github.com')

if response:
    print('Success!')
else:
    print('An error has occurred.')
```

    Success!
    

* Стоит иметь в виду, что данный способ не проверяет, имеет ли статусный код точное значение **200**. 
* Причина заключается в том, что другие коды в промежутке от **200** до **400**, например, **204 NO CONTENT** и **304 NOT MODIFIED**, также считаются успешными в случае, если они могут предоставить действительный ответ.
* К примеру, код состояния **204** говорит о том, что ответ успешно получен, однако в полученном объекте нет содержимого.
* Можно сказать, что для оптимально эффективного использования способа необходимо убедиться, что начальный запрос был успешно выполнен. 
* Требуется изучить код состояния и в случае необходимости произвести необходимые поправки, которые будут зависеть от значения полученного кода.

### `.raise_for_status()` и `HTTPError`

* Если при использовании оператора **if** вы не хотите проверять код состояния, можно расширить диапазон исключений для неудачных результатов запроса. 
* Это можно сделать при помощи использования `.raise_for_status()`


```python
import requests
from requests.exceptions import HTTPError
 
for url in ['https://api.github.com']:
    try:
        response = requests.get(url)
 
        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
```

    Success!
    

* В случае вызова исключений через `.raise_for_status()` к некоторым кодам состояния применяется `HTTPError`. 
* Когда код состояния показывает, что запрос успешно выполнен, программа продолжает работу без применения политики исключений.

**Подыто́жим:**
* Анализ способов использования кодов состояния, полученных с сервера, является неплохим стартом для изучения `requests`.
* Тем не менее, при создании запроса **GET**, значение кода состояния является не самой важной информацией, которую хочет получить программист. 
* Обычно запрос производится для извлечения более содержательной информации. 
* В дальнейшем будет показано, как добраться до актуальных данных, которые сервер высылает отправителю в ответ на запрос.

## 5. Получить содержимое страницы в `Requests`

### `payload`

* Ответ на запрос **GET** содержит информацию. 
* Она находится в теле сообщения и называется **пейлоад** (`payload`). 
* Используя атрибуты и методы библиотеки `Response`, можно получить **пейлоад** в различных форматах.



### `.content` ,  `.text`  ,  `.encoding=" "`  ,  `json()`






* Для того, чтобы получить содержимое запроса в байтах, необходимо использовать `.content`.
* Использование `.content` обеспечивает доступ к чистым байтам ответного пейлоада, то есть к любым данным в теле запроса.


```python
import requests

response = requests.get('https://api.github.com')
response.content
```




    b'{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","topic_search_url":"https://api.github.com/search/topics?q={query}{&page,per_page}","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'



* Однако, зачастую требуется конвертировать полученную информацию в строку в кодировке UTF-8. response делает это при помощи `.text`.


```python
import requests

response = requests.get('https://api.github.com')
response.text
```




    '{"current_user_url":"https://api.github.com/user","current_user_authorizations_html_url":"https://github.com/settings/connections/applications{/client_id}","authorizations_url":"https://api.github.com/authorizations","code_search_url":"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}","commit_search_url":"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}","emails_url":"https://api.github.com/user/emails","emojis_url":"https://api.github.com/emojis","events_url":"https://api.github.com/events","feeds_url":"https://api.github.com/feeds","followers_url":"https://api.github.com/user/followers","following_url":"https://api.github.com/user/following{/target}","gists_url":"https://api.github.com/gists{/gist_id}","hub_url":"https://api.github.com/hub","issue_search_url":"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}","issues_url":"https://api.github.com/issues","keys_url":"https://api.github.com/user/keys","label_search_url":"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}","notifications_url":"https://api.github.com/notifications","organization_url":"https://api.github.com/orgs/{org}","organization_repositories_url":"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}","organization_teams_url":"https://api.github.com/orgs/{org}/teams","public_gists_url":"https://api.github.com/gists/public","rate_limit_url":"https://api.github.com/rate_limit","repository_url":"https://api.github.com/repos/{owner}/{repo}","repository_search_url":"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}","current_user_repositories_url":"https://api.github.com/user/repos{?type,page,per_page,sort}","starred_url":"https://api.github.com/user/starred{/owner}{/repo}","starred_gists_url":"https://api.github.com/gists/starred","topic_search_url":"https://api.github.com/search/topics?q={query}{&page,per_page}","user_url":"https://api.github.com/users/{user}","user_organizations_url":"https://api.github.com/user/orgs","user_repositories_url":"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}","user_search_url":"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"}'



* Декодирование байтов в строку требует наличия определенной модели кодировки. 
* По умолчанию `requests` попытается узнать текущую кодировку, ориентируясь по заголовкам **HTTP**. 
* Указать необходимую кодировку можно при помощи добавления `.encoding` перед `.text`.


```python
import requests

response = requests.get('https://api.github.com')
response.encoding = 'utf-8' 
response.text
```




    '{\n  "current_user_url": "https://api.github.com/user",\n  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",\n  "authorizations_url": "https://api.github.com/authorizations",\n  "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",\n  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",\n  "emails_url": "https://api.github.com/user/emails",\n  "emojis_url": "https://api.github.com/emojis",\n  "events_url": "https://api.github.com/events",\n  "feeds_url": "https://api.github.com/feeds",\n  "followers_url": "https://api.github.com/user/followers",\n  "following_url": "https://api.github.com/user/following{/target}",\n  "gists_url": "https://api.github.com/gists{/gist_id}",\n  "hub_url": "https://api.github.com/hub",\n  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",\n  "issues_url": "https://api.github.com/issues",\n  "keys_url": "https://api.github.com/user/keys",\n  "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",\n  "notifications_url": "https://api.github.com/notifications",\n  "organization_url": "https://api.github.com/orgs/{org}",\n  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",\n  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",\n  "public_gists_url": "https://api.github.com/gists/public",\n  "rate_limit_url": "https://api.github.com/rate_limit",\n  "repository_url": "https://api.github.com/repos/{owner}/{repo}",\n  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",\n  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",\n  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",\n  "starred_gists_url": "https://api.github.com/gists/starred",\n  "topic_search_url": "https://api.github.com/search/topics?q={query}{&page,per_page}",\n  "user_url": "https://api.github.com/users/{user}",\n  "user_organizations_url": "https://api.github.com/user/orgs",\n  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",\n  "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"\n}\n'



* Если присмотреться к ответу, можно заметить, что его содержимое является сериализированным **JSON** контентом.
* Воспользовавшись словарем, можно взять полученные из `.text` строки **str** и провести с ними обратную сериализацию при помощи использования `json.loads()`. 
* Есть и более простой способ, который требует применения `.json()`.


```python
import requests

response = requests.get('https://api.github.com')
response.json()
```




    {'current_user_url': 'https://api.github.com/user',
     'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}',
     'authorizations_url': 'https://api.github.com/authorizations',
     'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}',
     'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}',
     'emails_url': 'https://api.github.com/user/emails',
     'emojis_url': 'https://api.github.com/emojis',
     'events_url': 'https://api.github.com/events',
     'feeds_url': 'https://api.github.com/feeds',
     'followers_url': 'https://api.github.com/user/followers',
     'following_url': 'https://api.github.com/user/following{/target}',
     'gists_url': 'https://api.github.com/gists{/gist_id}',
     'hub_url': 'https://api.github.com/hub',
     'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}',
     'issues_url': 'https://api.github.com/issues',
     'keys_url': 'https://api.github.com/user/keys',
     'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}',
     'notifications_url': 'https://api.github.com/notifications',
     'organization_url': 'https://api.github.com/orgs/{org}',
     'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}',
     'organization_teams_url': 'https://api.github.com/orgs/{org}/teams',
     'public_gists_url': 'https://api.github.com/gists/public',
     'rate_limit_url': 'https://api.github.com/rate_limit',
     'repository_url': 'https://api.github.com/repos/{owner}/{repo}',
     'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}',
     'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}',
     'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}',
     'starred_gists_url': 'https://api.github.com/gists/starred',
     'topic_search_url': 'https://api.github.com/search/topics?q={query}{&page,per_page}',
     'user_url': 'https://api.github.com/users/{user}',
     'user_organizations_url': 'https://api.github.com/user/orgs',
     'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}',
     'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}



* Тип полученного значения из `.json()`, является словарем. 
* Это значит, что доступ к его содержимому можно получить по ключу:


```python
response.json()['current_user_url']
```




    'https://api.github.com/user'



> **Коды состояния** и **тело сообщения** предоставляют огромный диапазон возможностей. Однако, для их оптимального использования требуется изучить метаданные и заголовки **HTTP**.

## 6. HTTP заголовки в `Requests`

* **HTTP** заголовки ответов на запрос могут предоставить определенную полезную информацию. 
* Это может быть тип содержимого ответного **пейлоада**, а также ограничение по времени для **кеширования ответа**. 
* Для просмотра **HTTP** заголовков загляните в атрибут `.headers.`



### `.headers`


```python
import requests

response = requests.get('https://api.github.com')
response.headers
```




    {'Server': 'GitHub.com', 'Date': 'Sat, 11 Mar 2023 12:27:52 GMT', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With', 'ETag': '"4f825cc84e1c733059d46e76e6df9db557ae5254f9625dfe8e1b09499c449438"', 'x-github-api-version-selected': '2022-11-28', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Type': 'application/json; charset=utf-8', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Content-Encoding': 'gzip', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '52', 'X-RateLimit-Reset': '1678540711', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Used': '8', 'Accept-Ranges': 'bytes', 'Content-Length': '530', 'X-GitHub-Request-Id': '0683:74B9:4F29728:5069735:640C73D6'}



* `.headers` возвращает словарь, что позволяет получить доступ к значению заголовка **HTTP** по ключу. 
* Например, для просмотра типа содержимого ответного **пейлоада**, требуется использовать ключ словаря **'Content-Type'**:


```python
import requests

response = requests.get('https://api.github.com')
response.headers['Content-Type']
```




    'application/json; charset=utf-8'



* У объектов словарей в качестве заголовков есть своим особенности. 
* Специфика **HTTP** предполагает, что заголовки не чувствительны к регистру.
* Это значит, что при получении доступа к заголовкам можно не беспокоится о том, использованы строчным или прописные буквы.
* При использовании ключей **'content-type'** и **'Content-Type'** результат будет получен один и тот же.



**Подыто́жим:**
* Это была основная информация, требуемая для работы с `Response`. 
* Были задействованы главные атрибуты и методы, а также представлены примеры их использования. 
* В дальнейшем будет показано, как изменится ответ после настройки **запроса GET**.

## 7. Python `Requests` параметры запроса (Нихрена не понятно, но очень интересно!)

* Наиболее простым способом настроить **запрос GET** является передача значений через параметры строки запроса в URL.
* При использовании метода `get()`, данные передаются в `params`. 
* Например, для того, чтобы посмотреть на библиотеку `requests` можно использовать **Search API** на **GitHub** :


```python
import requests
 
# Поиск местонахождения для запросов на GitHub
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
 
# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
pprint(repository)
print('=========================================')
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+
```

    {'allow_forking': True,
     'archive_url': 'https://api.github.com/repos/spyoungtech/grequests/{archive_format}{/ref}',
     'archived': False,
     'assignees_url': 'https://api.github.com/repos/spyoungtech/grequests/assignees{/user}',
     'blobs_url': 'https://api.github.com/repos/spyoungtech/grequests/git/blobs{/sha}',
     'branches_url': 'https://api.github.com/repos/spyoungtech/grequests/branches{/branch}',
     'clone_url': 'https://github.com/spyoungtech/grequests.git',
     'collaborators_url': 'https://api.github.com/repos/spyoungtech/grequests/collaborators{/collaborator}',
     'comments_url': 'https://api.github.com/repos/spyoungtech/grequests/comments{/number}',
     'commits_url': 'https://api.github.com/repos/spyoungtech/grequests/commits{/sha}',
     'compare_url': 'https://api.github.com/repos/spyoungtech/grequests/compare/{base}...{head}',
     'contents_url': 'https://api.github.com/repos/spyoungtech/grequests/contents/{+path}',
     'contributors_url': 'https://api.github.com/repos/spyoungtech/grequests/contributors',
     'created_at': '2012-05-10T21:50:15Z',
     'default_branch': 'master',
     'deployments_url': 'https://api.github.com/repos/spyoungtech/grequests/deployments',
     'description': 'Requests + Gevent = <3',
     'disabled': False,
     'downloads_url': 'https://api.github.com/repos/spyoungtech/grequests/downloads',
     'events_url': 'https://api.github.com/repos/spyoungtech/grequests/events',
     'fork': False,
     'forks': 330,
     'forks_count': 330,
     'forks_url': 'https://api.github.com/repos/spyoungtech/grequests/forks',
     'full_name': 'spyoungtech/grequests',
     'git_commits_url': 'https://api.github.com/repos/spyoungtech/grequests/git/commits{/sha}',
     'git_refs_url': 'https://api.github.com/repos/spyoungtech/grequests/git/refs{/sha}',
     'git_tags_url': 'https://api.github.com/repos/spyoungtech/grequests/git/tags{/sha}',
     'git_url': 'git://github.com/spyoungtech/grequests.git',
     'has_discussions': False,
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_projects': True,
     'has_wiki': True,
     'homepage': 'https://pypi.python.org/pypi/grequests',
     'hooks_url': 'https://api.github.com/repos/spyoungtech/grequests/hooks',
     'html_url': 'https://github.com/spyoungtech/grequests',
     'id': 4290214,
     'is_template': False,
     'issue_comment_url': 'https://api.github.com/repos/spyoungtech/grequests/issues/comments{/number}',
     'issue_events_url': 'https://api.github.com/repos/spyoungtech/grequests/issues/events{/number}',
     'issues_url': 'https://api.github.com/repos/spyoungtech/grequests/issues{/number}',
     'keys_url': 'https://api.github.com/repos/spyoungtech/grequests/keys{/key_id}',
     'labels_url': 'https://api.github.com/repos/spyoungtech/grequests/labels{/name}',
     'language': 'Python',
     'languages_url': 'https://api.github.com/repos/spyoungtech/grequests/languages',
     'license': {'key': 'bsd-2-clause',
                 'name': 'BSD 2-Clause "Simplified" License',
                 'node_id': 'MDc6TGljZW5zZTQ=',
                 'spdx_id': 'BSD-2-Clause',
                 'url': 'https://api.github.com/licenses/bsd-2-clause'},
     'merges_url': 'https://api.github.com/repos/spyoungtech/grequests/merges',
     'milestones_url': 'https://api.github.com/repos/spyoungtech/grequests/milestones{/number}',
     'mirror_url': None,
     'name': 'grequests',
     'node_id': 'MDEwOlJlcG9zaXRvcnk0MjkwMjE0',
     'notifications_url': 'https://api.github.com/repos/spyoungtech/grequests/notifications{?since,all,participating}',
     'open_issues': 5,
     'open_issues_count': 5,
     'owner': {'avatar_url': 'https://avatars.githubusercontent.com/u/15212758?v=4',
               'events_url': 'https://api.github.com/users/spyoungtech/events{/privacy}',
               'followers_url': 'https://api.github.com/users/spyoungtech/followers',
               'following_url': 'https://api.github.com/users/spyoungtech/following{/other_user}',
               'gists_url': 'https://api.github.com/users/spyoungtech/gists{/gist_id}',
               'gravatar_id': '',
               'html_url': 'https://github.com/spyoungtech',
               'id': 15212758,
               'login': 'spyoungtech',
               'node_id': 'MDQ6VXNlcjE1MjEyNzU4',
               'organizations_url': 'https://api.github.com/users/spyoungtech/orgs',
               'received_events_url': 'https://api.github.com/users/spyoungtech/received_events',
               'repos_url': 'https://api.github.com/users/spyoungtech/repos',
               'site_admin': False,
               'starred_url': 'https://api.github.com/users/spyoungtech/starred{/owner}{/repo}',
               'subscriptions_url': 'https://api.github.com/users/spyoungtech/subscriptions',
               'type': 'User',
               'url': 'https://api.github.com/users/spyoungtech'},
     'private': False,
     'pulls_url': 'https://api.github.com/repos/spyoungtech/grequests/pulls{/number}',
     'pushed_at': '2022-12-29T03:07:40Z',
     'releases_url': 'https://api.github.com/repos/spyoungtech/grequests/releases{/id}',
     'score': 1.0,
     'size': 56,
     'ssh_url': 'git@github.com:spyoungtech/grequests.git',
     'stargazers_count': 4195,
     'stargazers_url': 'https://api.github.com/repos/spyoungtech/grequests/stargazers',
     'statuses_url': 'https://api.github.com/repos/spyoungtech/grequests/statuses/{sha}',
     'subscribers_url': 'https://api.github.com/repos/spyoungtech/grequests/subscribers',
     'subscription_url': 'https://api.github.com/repos/spyoungtech/grequests/subscription',
     'svn_url': 'https://github.com/spyoungtech/grequests',
     'tags_url': 'https://api.github.com/repos/spyoungtech/grequests/tags',
     'teams_url': 'https://api.github.com/repos/spyoungtech/grequests/teams',
     'topics': [],
     'trees_url': 'https://api.github.com/repos/spyoungtech/grequests/git/trees{/sha}',
     'updated_at': '2023-03-11T00:49:05Z',
     'url': 'https://api.github.com/repos/spyoungtech/grequests',
     'visibility': 'public',
     'watchers': 4195,
     'watchers_count': 4195,
     'web_commit_signoff_required': False}
    =========================================
    Repository name: grequests
    Repository description: Requests + Gevent = <3
    

* Передавая словарь **{'q': 'requests+language:python'}** в параметр `params`, который является частью `.get()`, можно изменить ответ, что был получен при использовании **Search API**.

* Можно передать параметры в `get()` в форме **словаря**, как было показано выше. Также можно использовать **список кортежей** :


```python
requests.get(
            'https://api.github.com/search/repositories',
            params=[('q', 'requests+language:python')],
            )
```




    <Response [200]>



* Также можно передать значение в байтах :


```python
requests.get(
            'https://api.github.com/search/repositories',
            params=b'q=requests+language:python',
            )
```




    <Response [200]>



* Строки запроса полезны для уточнения параметров в **запросах GET**. 
* Также можно настроить запросы при помощи добавления или изменения заголовков отправленных сообщений.

## 8. Настройка HTTP заголовка запроса (`headers`) (Нихрена не понятно, но очень интересно!)

* Для изменения **HTTP** заголовка требуется передать словарь данного **HTTP** заголовка в `get()` при помощи использования параметра `headers`. 
* Например, можно изменить предыдущий поисковой запрос, подсветив совпадения в результате. 
* Для этого в заголовке `Accept` медиа тип уточняется при помощи `text-match`.


```python
import requests
 
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
 
# просмотр нового массива `text-matches` с предоставленными данными
# о поиске в пределах результатов
json_response = response.json()
repository = json_response['items'][0]
pprint(repository)
print('=========================================')
print(f'Text matches: {repository["text_matches"]}')
```

    {'allow_forking': True,
     'archive_url': 'https://api.github.com/repos/spyoungtech/grequests/{archive_format}{/ref}',
     'archived': False,
     'assignees_url': 'https://api.github.com/repos/spyoungtech/grequests/assignees{/user}',
     'blobs_url': 'https://api.github.com/repos/spyoungtech/grequests/git/blobs{/sha}',
     'branches_url': 'https://api.github.com/repos/spyoungtech/grequests/branches{/branch}',
     'clone_url': 'https://github.com/spyoungtech/grequests.git',
     'collaborators_url': 'https://api.github.com/repos/spyoungtech/grequests/collaborators{/collaborator}',
     'comments_url': 'https://api.github.com/repos/spyoungtech/grequests/comments{/number}',
     'commits_url': 'https://api.github.com/repos/spyoungtech/grequests/commits{/sha}',
     'compare_url': 'https://api.github.com/repos/spyoungtech/grequests/compare/{base}...{head}',
     'contents_url': 'https://api.github.com/repos/spyoungtech/grequests/contents/{+path}',
     'contributors_url': 'https://api.github.com/repos/spyoungtech/grequests/contributors',
     'created_at': '2012-05-10T21:50:15Z',
     'default_branch': 'master',
     'deployments_url': 'https://api.github.com/repos/spyoungtech/grequests/deployments',
     'description': 'Requests + Gevent = <3',
     'disabled': False,
     'downloads_url': 'https://api.github.com/repos/spyoungtech/grequests/downloads',
     'events_url': 'https://api.github.com/repos/spyoungtech/grequests/events',
     'fork': False,
     'forks': 330,
     'forks_count': 330,
     'forks_url': 'https://api.github.com/repos/spyoungtech/grequests/forks',
     'full_name': 'spyoungtech/grequests',
     'git_commits_url': 'https://api.github.com/repos/spyoungtech/grequests/git/commits{/sha}',
     'git_refs_url': 'https://api.github.com/repos/spyoungtech/grequests/git/refs{/sha}',
     'git_tags_url': 'https://api.github.com/repos/spyoungtech/grequests/git/tags{/sha}',
     'git_url': 'git://github.com/spyoungtech/grequests.git',
     'has_discussions': False,
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_projects': True,
     'has_wiki': True,
     'homepage': 'https://pypi.python.org/pypi/grequests',
     'hooks_url': 'https://api.github.com/repos/spyoungtech/grequests/hooks',
     'html_url': 'https://github.com/spyoungtech/grequests',
     'id': 4290214,
     'is_template': False,
     'issue_comment_url': 'https://api.github.com/repos/spyoungtech/grequests/issues/comments{/number}',
     'issue_events_url': 'https://api.github.com/repos/spyoungtech/grequests/issues/events{/number}',
     'issues_url': 'https://api.github.com/repos/spyoungtech/grequests/issues{/number}',
     'keys_url': 'https://api.github.com/repos/spyoungtech/grequests/keys{/key_id}',
     'labels_url': 'https://api.github.com/repos/spyoungtech/grequests/labels{/name}',
     'language': 'Python',
     'languages_url': 'https://api.github.com/repos/spyoungtech/grequests/languages',
     'license': {'key': 'bsd-2-clause',
                 'name': 'BSD 2-Clause "Simplified" License',
                 'node_id': 'MDc6TGljZW5zZTQ=',
                 'spdx_id': 'BSD-2-Clause',
                 'url': 'https://api.github.com/licenses/bsd-2-clause'},
     'merges_url': 'https://api.github.com/repos/spyoungtech/grequests/merges',
     'milestones_url': 'https://api.github.com/repos/spyoungtech/grequests/milestones{/number}',
     'mirror_url': None,
     'name': 'grequests',
     'node_id': 'MDEwOlJlcG9zaXRvcnk0MjkwMjE0',
     'notifications_url': 'https://api.github.com/repos/spyoungtech/grequests/notifications{?since,all,participating}',
     'open_issues': 5,
     'open_issues_count': 5,
     'owner': {'avatar_url': 'https://avatars.githubusercontent.com/u/15212758?v=4',
               'events_url': 'https://api.github.com/users/spyoungtech/events{/privacy}',
               'followers_url': 'https://api.github.com/users/spyoungtech/followers',
               'following_url': 'https://api.github.com/users/spyoungtech/following{/other_user}',
               'gists_url': 'https://api.github.com/users/spyoungtech/gists{/gist_id}',
               'gravatar_id': '',
               'html_url': 'https://github.com/spyoungtech',
               'id': 15212758,
               'login': 'spyoungtech',
               'node_id': 'MDQ6VXNlcjE1MjEyNzU4',
               'organizations_url': 'https://api.github.com/users/spyoungtech/orgs',
               'received_events_url': 'https://api.github.com/users/spyoungtech/received_events',
               'repos_url': 'https://api.github.com/users/spyoungtech/repos',
               'site_admin': False,
               'starred_url': 'https://api.github.com/users/spyoungtech/starred{/owner}{/repo}',
               'subscriptions_url': 'https://api.github.com/users/spyoungtech/subscriptions',
               'type': 'User',
               'url': 'https://api.github.com/users/spyoungtech'},
     'private': False,
     'pulls_url': 'https://api.github.com/repos/spyoungtech/grequests/pulls{/number}',
     'pushed_at': '2022-12-29T03:07:40Z',
     'releases_url': 'https://api.github.com/repos/spyoungtech/grequests/releases{/id}',
     'score': 1.0,
     'size': 56,
     'ssh_url': 'git@github.com:spyoungtech/grequests.git',
     'stargazers_count': 4195,
     'stargazers_url': 'https://api.github.com/repos/spyoungtech/grequests/stargazers',
     'statuses_url': 'https://api.github.com/repos/spyoungtech/grequests/statuses/{sha}',
     'subscribers_url': 'https://api.github.com/repos/spyoungtech/grequests/subscribers',
     'subscription_url': 'https://api.github.com/repos/spyoungtech/grequests/subscription',
     'svn_url': 'https://github.com/spyoungtech/grequests',
     'tags_url': 'https://api.github.com/repos/spyoungtech/grequests/tags',
     'teams_url': 'https://api.github.com/repos/spyoungtech/grequests/teams',
     'text_matches': [{'fragment': 'Requests + Gevent = <3',
                       'matches': [{'indices': [0, 8], 'text': 'Requests'}],
                       'object_type': 'Repository',
                       'object_url': 'https://api.github.com/repositories/4290214',
                       'property': 'description'}],
     'topics': [],
     'trees_url': 'https://api.github.com/repos/spyoungtech/grequests/git/trees{/sha}',
     'updated_at': '2023-03-11T00:49:05Z',
     'url': 'https://api.github.com/repos/spyoungtech/grequests',
     'visibility': 'public',
     'watchers': 4195,
     'watchers_count': 4195,
     'web_commit_signoff_required': False}
    =========================================
    Text matches: [{'object_url': 'https://api.github.com/repositories/4290214', 'object_type': 'Repository', 'property': 'description', 'fragment': 'Requests + Gevent = <3', 'matches': [{'text': 'Requests', 'indices': [0, 8]}]}]
    

* Заголовок `Accept` сообщает серверу о типах контента, который можно использовать в рассматриваемом приложении. 
* Здесь подразумевается, что все совпадения будут подсвечены, для чего в заголовке используется значение **application/vnd.github.v3.text-match+json**. 
* Это уникальный заголовок `Accept` для **GitHub**. 
* В данном случае содержимое представлено в специальном **JSON** формате.

Перед более глубоким изучением способов редактирования запросов, будет не лишним остановиться на некоторых других методах **HTTP**.

## 9. Примеры HTTP методов в `Requests` ( !!!Надо дорабатывать!!! )

* Помимо **GET**, большой популярностью пользуются такие методы, как:
    * `POST`
    * `PUT`
    * `DELETE`
    * `HEAD`
    * `PATCH`
    * `OPTIONS`
* Для каждого из этих методов существует своя сигнатура, которая очень похожа на метод `get()`.
* Каждая функция создает запрос к **httpbin сервису**, используя при этом ответный **HTTP метод**. 


```python
requests.post('https://httpbin.org/post', data={'key':'value'})
```




    <Response [200]>




```python
requests.put('https://httpbin.org/put', data={'key':'value'})
```




    <Response [200]>




```python

requests.delete('https://httpbin.org/delete')
```




    <Response [200]>




```python
requests.head('https://httpbin.org/get')
```




    <Response [200]>




```python
requests.patch('https://httpbin.org/patch', data={'key':'value'})
```




    <Response [200]>




```python
requests.options('https://httpbin.org/get')
```




    <Response [200]>



* При использовании каждого из данных методов в `Response` могут быть возвращены **заголовки**, **тело запроса**, **коды состояния** и многие другие аспекты.

## 10. Python `Requests` тело сообщения

* В соответствии со спецификацией **HTTP** запросы `POST`, `PUT` и `PATCH` передают информацию через тело сообщения, а не через параметры строки запроса. 
* Используя `requests`, можно передать данные в параметр `data`.
* В свою очередь `data` использует **словарь**, **список кортежей**, **байтов** или **объект файла**.
* Это особенно важно, так как может возникнуть необходимость адаптации отправляемых с запросом данных в соответствии с определенными параметрами сервера.
* В том случае, если требуется отравить данные **JSON**, можно использовать параметр `json`. 
* При передачи данных **JSON** через `json()`, `requests` произведет **сериализацию** данных и добавит правильный **Content-Type** заголовок.

* Стоит взять на заметку сайт **httpbin.org**. 
* Это чрезвычайно полезный ресурс, созданный человеком, который внедрил использование `requests` – Кеннетом Рейтцом. 
* Данный сервис предназначен для тестовых запросов. 
* Здесь можно составить пробный запрос и получить ответ с требуемой информацией. 

В качестве примера рассмотрим базовый запрос с использованием `POST`:


```python
response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
pprint(json_response)
json_response['data']
```

    {'args': {},
     'data': '{"key": "value"}',
     'files': {},
     'form': {},
     'headers': {'Accept': '*/*',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Content-Length': '16',
                 'Content-Type': 'application/json',
                 'Host': 'httpbin.org',
                 'User-Agent': 'python-requests/2.28.1',
                 'X-Amzn-Trace-Id': 'Root=1-640c9f37-64f8d2ea63e8d2962d0d3189'},
     'json': {'key': 'value'},
     'origin': '5.34.70.54',
     'url': 'https://httpbin.org/post'}
    




    '{"key": "value"}'




```python
json_response['headers']['Content-Type']
```




    'application/json'



* Здесь видно, что сервер получил данные и **HTTP** заголовки, отправленные вместе с запросом. 
* `requests` также предоставляет информацию в форме `PreparedRequest`.

## 11. Python `Requests` анализ запроса (Надо углубляться!!!)

* При составлении запроса стоит иметь в виду, что перед его фактической отправкой на целевой сервер библиотека `requests` выполняет определенную подготовку. 
* Подготовка запроса включает в себя такие вещи, как проверка заголовков и сериализация содержимого **JSON**.

### `.request`

* Если открыть `.request`, можно просмотреть **PreparedRequest** (*пер. "подготовленный запрос"*).


```python
response = requests.post('https://httpbin.org/post', json={'key':'value'})
pprint(response)
response.request.headers['Content-Type']
```

    <Response [200]>
    




    'application/json'




```python
response.request.url
```




    'https://httpbin.org/post'




```python
response.request.body
```




    b'{"key": "value"}'



* Проверка **PreparedRequest** открывает доступ ко всей информации о выполняемом запросе. 
* Это может быть пейлоад, URL, заголовки, аутентификация и многое другое.

* У всех описанных ранее типов запросов была одна общая черта – они представляли собой **неаутентифицированные запросы к публичным API**. 
* Однако, подобающее большинство служб, с которыми может столкнуться пользователь, **запрашивают аутентификацию**.

## 12. Python Requests аутентификация HTTP AUTH

* Аутентификация помогает сервису понять, кто вы. 
* Как правило, вы предоставляете свои учетные данные на сервер, передавая данные через заголовок Authorization или пользовательский заголовок, определенной службы. 
* Все функции запроса, которые вы видели до этого момента, предоставляют параметр с именем auth, который позволяет вам передавать свои учетные данные.

* Одним из примеров **API**, который требует аутентификации, является **Authenticated User API на GitHub**.
* Это конечная точка веб-сервиса, которая предоставляет информацию о профиле аутентифицированного пользователя.
* Чтобы отправить запрос **API-интерфейсу аутентифицированного пользователя**, вы можете передать свое имя пользователя и пароль на **GitHub** через кортеж в `get()`.


```python
from getpass import getpass
requests.get('https://api.github.com/user', auth=('username', getpass()))
```

    ········
    




    <Response [401]>



* Запрос выполнен успешно, если учетные данные, которые вы передали в кортеже `auth`, действительны. 
* Если вы попытаетесь сделать этот запрос без учетных данных, вы увидите, что код состояния **401 Unauthorized**.

* Когда вы передаете имя пользователя и пароль в кортеже параметру `auth`, вы используете учетные данные при помощи базовой схемы аутентификации **HTTP**.
* Таким образом, вы можете создать тот же запрос, передав подробные учетные данные базовой аутентификации, используя **HTTPBasicAuth**.


```python

from requests.auth import HTTPBasicAuth
from getpass import getpass
requests.get(
            'https://api.github.com/user',
            auth=HTTPBasicAuth('username', getpass()))
```

    ········
    




    <Response [401]>



* Хотя вам не нужно явно указывать обычную аутентификацию, может потребоваться аутентификация с использованием другого метода. 
* `Requests` предоставляет другие методы аутентификации, например: **HTTPDigestAuth** и **HTTPProxyAuth**.

* Вы даже можете предоставить свой собственный механизм аутентификации. 
* Для этого необходимо сначала создать подкласс **AuthBase**. 
* Затем происходит имплементация `__call__()`. (**Имплементация** - «осуществление, выполнение, практическая реализация»)


```python
import requests
from requests.auth import AuthBase
 
class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""
 
    def __init__(self, token):
        self.token = token
 
    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r
 
 
requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
```




    <Response [200]>



* Здесь пользовательский механизм **TokenAuth** получает специальный токен. 
* Затем этот токен включается заголовок **X-TokenAuth** запроса.

* Плохие механизмы аутентификации могут привести к уязвимостям безопасности. 
* Поэтому, если службе по какой-то причине не нужен настраиваемый механизм аутентификации, вы всегда можете использовать проверенную схему аутентификации, такую как **Basic** или **OAuth**.

Далее рассмотрим использование `requests` в **SSL сертификатах**.

## 13. Python Requests проверка SSL сертификата

* Всякий раз, когда данные, которые вы пытаетесь отправить или получить, являются конфиденциальными, безопасность важна.
* Вы общаетесь с защищенными сайтами через HTTP, устанавливая зашифрованное соединение с использованием **SSL**, что означает, что проверка **SSL сертификата** целевого сервера имеет решающее значение.
* Хорошей новостью является то, что `requests` по умолчанию все делает сам. Однако в некоторых случаях необходимо внести определенные поправки.
* Если требуется отключить проверку **SSL-сертификата**, параметру `verify` функции запроса можно присвоить значение `False`.


```python
 requests.get('https://api.github.com', verify=False)
```

    C:\ProgramData\anaconda3\lib\site-packages\urllib3\connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'api.github.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      warnings.warn(
    




    <Response [200]>



* В случае небезопасного запроса `requests` предупреждает о возможности потери информации и просит сохранить данные или отказаться от запроса.

**Примечание:** Для предоставления сертификатов `requests` использует пакет, который вызывается `certifi`. Это дает понять `requests`, каким ответам можно доверять. Поэтому вам следует часто обновлять `certifi`, чтобы обеспечить максимальную безопасность ваших соединений.

## 14. Python Requests производительность приложений

* При использовании `requests`, особенно в среде приложений, важно учитывать влияние на производительность. 
* Такие функции, как контроль таймаута, сеансы и ограничения повторных попыток, могут помочь обеспечить бесперебойную работу приложения.

### `timeout` (Таймауты)

* Когда вы отправляете встроенный запрос во внешнюю службу, вашей системе нужно будет дождаться ответа, прежде чем двигаться дальше.
* Если ваше приложение слишком долго ожидает ответа, запросы к службе могут быть сохранены, пользовательский интерфейс может пострадать или фоновые задания могут зависнуть.
* По умолчанию в `requests` на ответ время не ограничено, и весь процесс может занять значительный промежуток.
* По этой причине вы всегда должны указывать время ожидания, чтобы такого не происходило. 
* Чтобы установить время ожидания запроса, используйте параметр `timeout`.
* `timeout` может быть целым числом или числом с плавающей точкой, представляющим количество секунд ожидания ответа до истечения времени ожидания.


```python
requests.get('https://api.github.com', timeout=1)
```




    <Response [200]>




```python
requests.get('https://api.github.com', timeout=3.05)
```




    <Response [200]>



* В первом примере запрос истекает через 1 секунду. Во втором примере запрос истекает через 3,05 секунды.

* Мы также можете передать **кортеж**. 
* Это – таймаут соединения (время, за которое клиент может установить соединение с сервером), а второй – таймаут чтения (время ожидания ответа, как только ваш клиент установил соединение):


```python
requests.get('https://api.github.com', timeout=(2, 5))
```




    <Response [200]>



* Если запрос устанавливает соединение в течение 2 секунд и получает данные в течение 5 секунд после установления соединения, то ответ будет возвращен, как это было раньше. 
* Если время ожидания истекло, функция вызовет исключение `Timeout`.



Наша программа может поймать `исключение Timeout` и ответить соответственно:


```python
import requests
from requests.exceptions import Timeout
 
try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')
```

    The request did not time out
    

## 15. Объект `Session` в `Requests`

* До сих пор вы имели дело с **requests API высокого уровня**, такими как `get()` и `post()`.
* Эти функции являются абстракцией того, что происходит, когда вы делаете свои запросы. 
* Они скрывают детали реализации, такие как управление соединениями, так что вам не нужно о них беспокоиться.
* Под этими абстракциями находится **класс** под названием `Session`. 
* Если вам необходимо настроить контроль над выполнением запросов или повысить производительность ваших запросов, вам может потребоваться использовать `Session` напрямую.

> **Сессии** используются для сохранения параметров в запросах.

Если вы хотите использовать одну и ту же аутентификацию для нескольких запросов, вы можете использовать сеанс:


```python
import requests
from getpass import getpass
 
# используя менеджер контента, можно убедиться, что ресурсы, применимые
# во время сессии будут свободны после использования
with requests.Session() as session:
    session.auth = ('username', getpass())
 
    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')
 
# здесь можно изучить ответ 
print(response.headers)
print('===================================================================================================================')
print(response.json())
```

    ········
    {'Server': 'GitHub.com', 'Date': 'Sun, 12 Mar 2023 17:05:47 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '131', 'X-GitHub-Media-Type': 'github.v3; format=json', 'x-github-api-version-selected': '2022-11-28', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '56', 'X-RateLimit-Reset': '1678644162', 'X-RateLimit-Used': '4', 'X-RateLimit-Resource': 'core', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Vary': 'Accept-Encoding, Accept, X-Requested-With', 'X-GitHub-Request-Id': '8564:66E7:EA0BE7E:ED7A0F7:640E066B'}
    ===================================================================================================================
    {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/reference/users#get-the-authenticated-user'}
    

* Каждый раз, когда вы делаете запрос `session`, после того как он был инициализирован с учетными данными аутентификации, учетные данные будут сохраняться.

* Первичная оптимизация производительности сеансов происходит в форме постоянных соединений. 
* Когда ваше приложение устанавливает соединение с сервером с помощью `Session`, оно сохраняет это соединение в пуле соединений.
* Когда ваше приложение снова хочет подключиться к тому же серверу, оно будет использовать соединение из пула, а не устанавливать новое.

# 16. `HTTPAdapter` — Максимальное количество повторов запроса в `Requests`

* В случае сбоя запроса возникает необходимость сделать повторный запрос. 
* Однако `requests` не будет делать это самостоятельно. 
* Для применения функции повторного запроса требуется реализовать собственный **транспортный адаптер**.



* **Транспортные адаптеры** позволяют определить набор конфигураций для каждой службы, с которой вы взаимодействуете.
* Предположим, вы хотите, чтобы все запросы к https://api.github.com были повторены три раза, прежде чем, наконец, появится **ConnectionError**. 
* Для этого нужно построить **транспортный адаптер**, установить его параметр **max_retries** и подключить его к существующему объекту `Session`.


```python
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
 
github_adapter = HTTPAdapter(max_retries=3)
 
session = requests.Session()
 
# использование `github_adapter` для всех запросов, которые начинаются с указанным URL
session.mount('https://api.github.com', github_adapter)
 
try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
```

* При установке **HTTPAdapter**, **github_adapter** к `session`, `session` будет придерживаться своей конфигурации для каждого запроса к https://api.github.com.

* **Таймауты**, **транспортные адаптеры** и **сессии** предназначены для обеспечения эффективности используемого кода и стабильности приложения.

> *Данная статья является переводом статьи:* **Python’s Requests Library (Guide)** --->>>   https://realpython.com/python-requests/


```python

```
