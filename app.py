
import os
import sys
import requests
from downloadTorrent import downloadMovie



def fetchLatestMovies ( ):
    #fetch movies from ther server
    api_url = "https://yts.mx/api/v2/list_movies.json?limit=50"
    readFile  =  open('moviesIds.txt','r')
    writeFile  =  open('moviesIds.txt','a');
    values= readFile.readlines()
    
    for v in requests.get(api_url).json()['data']['movies']:  
        if(len(values)):
            for value in values:
                if (str(value)  !=  str(v["id"])):
                    writeFile.write("\n"+str(v["id"]))
                    download(v["torrents"][0]["url"])
                    print("loading and torrent movies")
        else:
            writeFile.write("\n"+str(v["id"]))
            download(v["torrents"][0]["url"]) 
           
        
def download(url: str, dest_folder ="./tfiles"):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    # print(url)
    file_path = os.path.join(dest_folder,(filename))

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
  
fetchLatestMovies()