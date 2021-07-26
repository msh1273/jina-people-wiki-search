# in executors.py
model = "sentence-transformers/msmarco-distilbert-base-v3" # Language model will we use to "understand" the text
top_k = 15 # How many results will a query return?

# in app.py
port = 45678 # Port for REST query gateway
workdir = "workspace" # Directory where we will store the index
datafile = "./data/input.csv" # Processed datafile
text_length = 50 # How many words to index for each app? Longer = more accurate, shorter = quicker
max_docs = 3000 # How many apps to index. Can override with "-n" flag

# dataset
dataset_url = "kaggle datasets download -d sameersmahajan/people-wikipedia-data" # URL to download dataset
dataset_filename = 'people_wiki.csv' # Original dataset filename
random_seed = 42 # Ensure we can replicate shuffling so we get consistent results
