from django.db.models import Model, CharField, JSONField, ForeignKey, CASCADE, TextField, ImageField, BooleanField


class User(Model):
    name = CharField(max_length=50)
    username = CharField(max_length=50)
    email = CharField(max_length=75)
    address = JSONField(null=True)
    phone = CharField(max_length=15)
    website = CharField(max_length=100)
    company = JSONField(null=True)

    def __str__(self):
        return self.name


class Post(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='posts')
    title = CharField(max_length=75)
    body = TextField()

    def __str__(self):
        return self.title


class Comments(Model):
    post = ForeignKey('apps.Post', CASCADE, related_name='comments')
    name = CharField(max_length=75)
    email = CharField(max_length=75)
    body = TextField()

    def __str__(self):
        return self.name


class Album(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='albums')
    title = CharField(max_length=75)

    def __str__(self):
        return self.title


class Photo(Model):
    Album = ForeignKey('apps.Album', CASCADE, related_name='photos')
    title = CharField(max_length=75)
    image = ImageField(upload_to='albums/%Y/%m/%d')

    def __str__(self):
        return self.title


class Todo(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='todos')
    title = CharField(max_length=75)
    completed = BooleanField(default=False)

    def __str__(self):
        return self.title