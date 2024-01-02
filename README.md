# Single website search
This code was created to make [daft.dev blog posts](https://draft.dev/learn/)
and Karl Hughes
[personal site](https://www.karllhughes.com/)
searchable.

There are two different approaches, both utilize public search
engines for the underlying search functionality.

## Form based search
Both DuckDuckGo and Google have features to allow web searches
to be scoped for a specific domain or URL. The syntax for each
is the same:
```
site:example.com  example search terms
```
Draft.dev example
```
site:draft.dev/learn/ developer marketing
```

To use this functionality within an existing website
the file [index.html](index.html) was used as an example. It is a 
simple html file with two forms. One example using DuckDuckGo and 
another using Google. 

These forms can be embedded into any webpage to add search. However
it opens up a new tab to the search engine page to display the results.
For example using the DuckDuckGo form will open up the search results
for the draft.dev blog in a new tab on the DuckDuckGo site. This is 
different than most sites which keep the user on the website that is
being searched.

## DuckDuckGo using Python 
There is a [python library](https://pypi.org/project/duckduckgo-search/) 
that uses DuckDuckGo search to provide results. This approach should provide
the same results as the DuckDuckGo form above, however the results are returned
as a JSON string. The python code could be added and called from any python webapp.

The code is in the file [ddgs_example.py](ddgs_example.py).
You can install the dependencies using pip or pipenv. 
*Note: The pipenv options is a bit safer
because it be isolated in a virtual env and use the exact versions of all dependencies.*
```
# using pip
pip install requirements.txt

# using pipenv 
pipenv shell
pipenv install

```
After the libraries are installed the code can be run via
```
python ddgs_example.py

# or using bash shell script
./run_python_example.sh 
```

## Other options
Elastic search is another option but to use it the entire index state would
have to be stored. So its a greater technical burden to handle that. 
There is also AWS Opensearch which has the same draw back and probably a worse
product compared to Elastic search. For these reasons there is no example for
using Elastic search or Opensearch in this repo.
