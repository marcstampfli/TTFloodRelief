import datetime
from haystack import indexes
from .models import Location


class LocationIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Location

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
