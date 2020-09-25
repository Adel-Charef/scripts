import requests

URL = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"
response = requests.get(URL)     
response.raise_for_status()
      
def main():
    projects = response.json()    
    print("---------Top Django Packages and number of Downloads---------\n")
       
    for project in projects["rows"]:
    
        name = project["project"]
        download_count = project["download_count"]
        if "django" in name:
            print("--The Package: [{0}] has: {1} downloads\n".format(name, download_count))
     
if __name__ == "__main__":  
    main()
