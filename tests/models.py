from tortoise import fields, models


class User(models.Model):

    full_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)


class Address(models.Model):
    # user = fields.ForeignKeyField(model_name='tests.User', related_name='address')
    street_address = fields.CharField(max_length=255)
    city = fields.CharField(max_length=255)