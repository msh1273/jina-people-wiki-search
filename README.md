# Jina-wiki-people-search
This is a simple example using the jina neural search framework. 
<br>Data set used: [Kaggle](https://www.kaggle.com/sameersmahajan/people-wikipedia-data)

## Instructions
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/msh1273/jina-people-wiki-search)
### Clone this repo

```shell
git clone https://github.com/msh1273/jina-people-wiki-search.git
cd jina-people-wiki-search
```

### Create a virtual environment (optional)

We wouldn't want our project clashing with our system libraries, now would we?

```shell
virtualenv env --python=python3.8 # Python versions >= 3.7 work fine
source env/bin/activate
```

### Get the data

```shell
sh get_data.sh
```

### Install everything

Make sure you're in your virtual environment first!

```shell
pip install -r requirements.txt
```

### Search from the terminal
This project is deployed on ainize. You can get queries without cloning.

```shell
curl --request POST -d '{"top_k":15,"mode":"search","data":["Marlene Dietrich"]}' -H 'Content-Type: application/json' 'https://master-jina-people-wiki-search-msh1273.endpoint.ainize.ai/search'
```
Results may not be accurate as the number of documents currently indexed in the workspace is 3000 lines. For more accurate results, increase the number of documents to be indexed!

Where `Marlene Dietrich` is your query.


## FAQ

### Why this dataset?

This data set contains URIs, names of people, and text from Wikipedia pages. You will be able to search and get information about the person you are curious about easily and conveniently.

### How can I change basic settings?

Edit `backend_config.py`
