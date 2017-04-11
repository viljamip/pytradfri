"""Represent a mood on the gateway."""
from datetime import datetime

from .const import (
    ROOT_MOODS, ATTR_ID, ATTR_NAME, ATTR_CREATED_AT)


class Mood:
    def __init__(self, api, raw, parent):
        self.api = api
        self.raw = raw
        self._parent = parent

    @property
    def id(self):
        return self.raw.get(ATTR_ID)

    @property
    def name(self):
        return self.raw.get(ATTR_NAME)

    @property
    def created_at(self):
        if ATTR_CREATED_AT not in self.raw:
            return None
        return datetime.utcfromtimestamp(self.raw[ATTR_CREATED_AT])

    def update(self):
        self.raw = self.api('get', [ROOT_MOODS, self._parent, self.id])

    def __repr__(self):
        return '<Mood {}>'.format(self.name)
