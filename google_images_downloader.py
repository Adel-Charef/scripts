import json
import os
import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
SAVE_FOLDER = 'images'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()

def download_images():
    data = input('Search: ')
    n_images = int(input('Number of images: '))
    print('Start searching...')
    search_url = URL + 'q=' + data
    print(search_url)
    response = requests.get(search_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll('div', {'class': 'rg_meta'}, limit=n_images)
    image_links = []
    for re in results:
        text = re.text
        text_dict = json.loads(text)
        link = text_dict['ou']
        image_links.append(link)
    print(f'found {len(image_links)} images')
    print('Start downloading...')
    for j, image_link in enumerate(image_links):
        response = requests.get(image_link)
        image_name = SAVE_FOLDER + '/' + data + str(j + 1) + '.jpg'
        with open(image_name, 'wb') as file:
            file.write(response.content)
    print('Done')
 
if __name__ == '__main__':
    main()
