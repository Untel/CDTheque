class Album:
    
    def __init__(self, id, name, track, title, cover):
        self._id = id
        self._name = name
        self._track = track
        self._title = title
        self._cover = cover

    def _get_name(self):
        return self._name
    def _set_name(self, name):
        self._name = name.upper()
    name = property(_get_name, _set_name)

    def _get_track(self):
        return self._track
    def _set_track(self, track):
        self._track = track
    track = property(_get_track, _set_track)

    def _get_title(self):
        return self._title
    def _set_title(self, title):
        self._title = title
    title = property(_get_title, _set_title)

    def _get_cover(self):
        return self._cover
    def _set_cover(self, cover):
        self._cover = cover
    cover = property(_get_cover, _set_cover)