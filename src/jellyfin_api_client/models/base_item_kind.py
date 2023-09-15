from enum import Enum


class BaseItemKind(str, Enum):
    AGGREGATEFOLDER = "AggregateFolder"
    AUDIO = "Audio"
    AUDIOBOOK = "AudioBook"
    BASEPLUGINFOLDER = "BasePluginFolder"
    BOOK = "Book"
    BOXSET = "BoxSet"
    CHANNEL = "Channel"
    CHANNELFOLDERITEM = "ChannelFolderItem"
    COLLECTIONFOLDER = "CollectionFolder"
    EPISODE = "Episode"
    FOLDER = "Folder"
    GENRE = "Genre"
    LIVETVCHANNEL = "LiveTvChannel"
    LIVETVPROGRAM = "LiveTvProgram"
    MANUALPLAYLISTSFOLDER = "ManualPlaylistsFolder"
    MOVIE = "Movie"
    MUSICALBUM = "MusicAlbum"
    MUSICARTIST = "MusicArtist"
    MUSICGENRE = "MusicGenre"
    MUSICVIDEO = "MusicVideo"
    PERSON = "Person"
    PHOTO = "Photo"
    PHOTOALBUM = "PhotoAlbum"
    PLAYLIST = "Playlist"
    PLAYLISTSFOLDER = "PlaylistsFolder"
    PROGRAM = "Program"
    RECORDING = "Recording"
    SEASON = "Season"
    SERIES = "Series"
    STUDIO = "Studio"
    TRAILER = "Trailer"
    TVCHANNEL = "TvChannel"
    TVPROGRAM = "TvProgram"
    USERROOTFOLDER = "UserRootFolder"
    USERVIEW = "UserView"
    VIDEO = "Video"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
