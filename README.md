# MyDjangoNotes

In Django, the ~ operator for lookups is equivalent to the exclude() method of
a QuerySet, so these QuerySets are equivalent
So ~models.Q(author=None) is equivalent to objects.exclude(author=None)
                                          objects.filter(~models.Q(author=None))
