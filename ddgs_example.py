"""
  example site specific search using the library: 
    https://pypi.org/project/duckduckgo-search/

    Tested with urls:
        www.karllhughes.com
        https://draft.dev/learn/
"""
from duckduckgo_search import DDGS
import json

def search_karllhughes_com(search_str, max_results=5):
  domain_search_str = "site:www.karllhughes.com " + search_str
  return ddgs.text(domain_search_str, max_results=max_results)


search_string = "developer marketing"

with DDGS() as ddgs:
    result_list = search_karllhughes_com(search_string)

    # print out the results
    for result in result_list:
      print("Title: " + result['title'])
      print("Description: " + result['body'])
      print()

    # convert the results to a JSON string
    json_str = json.dumps(list(result_list))
    print("successfully converted to json string")
