# arXiv search Engine 

## Get start

### Host Websit locally

#### 1. create **Virtual Enviroment** (suggested)

The code is based on [Django](https://www.djangoproject.com/), tested on Python 3.9.0+

**bash**

```shell
python3.9 -m venv venv
source venv/bin/activate
```

**csh**

```shell
python3.9 -m venv venv
source venv/bin/activate.csh
```

#### 2. install the required package

```shell
pip install requirements.txt
```

#### 3. start the server 

```shell

python manage.py runserver
```

## contribute

## UI design

### Home Page

![](doc/resource/homepage.jpg)

### search page 

![](doc/resource/searchresult.jpg)

### data flow

![](doc/resource/dataflow.jpg)

## dev plan

### 1. front end

- [x] homepage UI
- [x] send post-request
- [ ] display the search result
---
**Optional**

- [ ] Voice to Text (record and convert)
- [ ] type suggestions
- [ ] today's new papers

### 2. backend

- [ ] respond the request
- [ ] rank the paper according to its search score

---

**Optional**

- [ ] voice to text
- [ ] type suggestion and correction
- [ ] push suggested readings


### 3. Develop Schedual

- [ ] Java backend http response 
- [ ] result display webpage
- [ ] search server code 
- [ ] voice to text 
- [ ] search suggestions
- [ ] recommendation



###TODO 

- [ ] front end
- [ ] send the request with the search string 
- [ ] display the search result according to the return json 

- [x] server side
- [ ] build server to respond the request 
- [ ] database 
- [ ] use json ?
- [ ] mysql , form query from string
- [ ] rank, how yo rank the papers
  
## next step
- [ ] voice to text 
- [ ] adapt it to the front end 
- [ ] ask, and answer 
## Q&A

* if port 8000 is in use
  
```bash
sudo kill -9 `sudo lsof -t -i:8000`
```