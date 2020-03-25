from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0:]
    else:
        return None


def show_album_tracks(album):
    tracks = []
    results = sp.album_tracks(album['id'])
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for track in tracks:
        print('  ', track['name'])
        # print()
        # print(track)


def show_artist_albums(id):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    print('Total albums:', len(albums))
    unique = set()  # skip duplicate albums
    for album in albums:
        name = album['name']
        image = album['images']
        release = album['release_date']
        if name not in unique:
            print(name)
            print(image)
            print(release)
            unique.add(name)
            show_album_tracks(album)


def show_artist(artist):
    for artist in artist:
        print('====', artist['name'], '====')
        print('Popularity: ', artist['popularity'])
        if len(artist['genres']) > 0:
            print('Genres: ', ','.join(artist['genres']))


if __name__ == '__main__':
    client_credentials_manager = SpotifyClientCredentials(client_id='26b8ce1fe9a140f8a1867a55b7c0118e', client_secret='e8576337c58449e48270f0b90c1d8714')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False

    if len(sys.argv) < 2:
        print(('Usage: {0} artist name'.format(sys.argv[0])))
    else:
        name = ' '.join(sys.argv[1:])
        artist = get_artist(name)
        show_artist(artist)
        show_artist_albums(artist)