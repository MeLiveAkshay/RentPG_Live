class room__model__table(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    facility = models.TextField()
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.IntegerField()
