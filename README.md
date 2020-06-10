# MyDjangoNotes

In Django, the ~ operator for lookups is equivalent to the exclude() method of
a QuerySet, so these QuerySets are equivalent
So ~models.Q(author=None) is equivalent to objects.exclude(author=None)
                                          objects.filter(~models.Q(author=None))


FieldError: Cannot resolve keyword 'venuenotes' into field. Choices are: content_type,
id, object_id, tag, venue, venuenote
actions=GenericRelation("actions.Action", content_type_field='target_ct', 
                            object_id_field='target_id',
                            related_query_name='actions')# must add content_type_field
                            #object_id_field
