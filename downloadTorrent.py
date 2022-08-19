import os
from torrentp import TorrentDownloader

def downloadMovies():
    path_dataset = "./tfiles"
    filedataset = os.listdir(path_dataset)
    for value in filedataset:
        torrent_file = TorrentDownloader("./tfiles/"+str(value), './movies')
        torrent_file.start_download()

def downloadMovie(fileName):
    torrent_file = TorrentDownloader("./tfiles/"+str(fileName)+ ".torrent", './movies')
    torrent_file.start_download()
   


