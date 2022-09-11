from django.db import models

STATE_CHOISE = (
("DHAKA","DHAKA"),
("RAJSHAHI","RAJSHAHI"),
("CHITTAGONG","CHITTAGONG"),
("BARISHAL","BARISHAL"),
("KHULNA","KHULNA"),
("RANGPUR","RANGPUR"),
("SYLHET","SYLHET"),
)



# Create your models here.
class Resume(models.Model):
    name= models.CharField(max_length=70)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=70)
    locality= models.CharField(max_length=70)
    city= models.CharField(max_length=100)
    pin= models.PositiveIntegerField()
    state = models.CharField(choices= STATE_CHOISE, max_length=100)
    mobile= models.PositiveIntegerField()
    email= models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)
