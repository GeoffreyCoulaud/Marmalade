from enum import Enum


class CollectionTypeOptions(str, Enum):
    BOOKS = "Books"
    BOXSETS = "BoxSets"
    HOMEVIDEOS = "HomeVideos"
    MIXED = "Mixed"
    MOVIES = "Movies"
    MUSIC = "Music"
    MUSICVIDEOS = "MusicVideos"
    TVSHOWS = "TvShows"

    def __str__(self) -> str:
        return str(self.value)
