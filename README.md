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




related_name will be the attribute of the related object that allows you to go 'backwards'
to the model with the foreign key on it. For example, if ModelA has a field like:
model_b = ForeignKeyField(ModelB, related_name='model_as'), this would enable you
to access the ModelA instances that are related to your ModelB instance by going
model_b_instance.model_as.all(). 

related_query_name is for use in Django querysets. It allows you to
filter on the reverse relationship of a foreign key related field.
To continue our example - having a field on Model A like:
model_b = ForeignKeyField(ModelB, related_query_name='model_a') would enable you
to use model_a as a lookup parameter in a queryset, like: ModelB.objects.filter(model_a=whatever).
It is more common to use a singular form for the related_query_name. As the docs say, it isn't
necessary to specify both (or either of) related_name and related_query_name. Django has sensible defaults.


The difference between get() and get_object_or_404 is that when by using get() when the object doesn't exist
it raise the exception, taht's why it's rather to use get_object_or_404 because it handles the error

Using a model Manager is very important


Consumers are structured around a series of named methods corresponding to the type value of the messages they are going to receive, with any . replaced by _. The two handlers above are handling websocket.connect and websocket.receive messages respectively.


It is important to note that you can't use a cached QuerySet to build other QuerySets,
since what you cached are actually the results of the QuerySet. So you can't do the
following:
  courses = cache.get('all_courses')
  courses.filter(subject=subject)
Instead, you have to create the base QuerySet Course.objects.annotate(total_
modules=Count('modules')) , which is not going to be executed until it
is forced, and use it to further restrict the QuerySet with all_courses.
filter(subject=subject) in case the data was not found in the cache.

def get_list_or_404(klass, *args, **kwargs):
Returns the result of filter() on a given model manager cast to a list, raising Http404 if the resulting list is empty.

is shortcut for

obj_list = list(Model.objects.filter(title=...))
if not obj_list:
    raise Http404()
return obj_list
