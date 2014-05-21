from django.db import models

# Create your models here.
class ProbaModel(models.Model):
	num = models.IntegerField(null=True, blank=True)


class ProbaModel2(models.Model):
	CharField = models.CharField(max_length=2048)
	CommaSeparatedIntegerField = models.CommaSeparatedIntegerField(max_length=2048)
	EmailField = models.EmailField()
	FileField = models.FileField(upload_to='upload')
	FilePathField = models.FilePathField()
	ImageField = models.ImageField(upload_to='upload')
	IPAddressField = models.IPAddressField()
	GenericIPAddressField = models.GenericIPAddressField()
	SlugField = models.SlugField()
	URLField = models.URLField()
	AutoField = models.AutoField(primary_key=True)
	BigIntegerField = models.BigIntegerField()
	BooleanField = models.BooleanField()
	DecimalField = models.DecimalField(decimal_places=16, max_digits=16)
	FloatField = models.FloatField()
	IntegerField = models.IntegerField()
	NullBooleanField = models.NullBooleanField()
	PositiveIntegerField = models.PositiveIntegerField()
	PositiveSmallIntegerField = models.PositiveSmallIntegerField()
	SmallIntegerField = models.SmallIntegerField()
	ForeignKey = models.ForeignKey(ProbaModel, related_name='ProbaFK')
	ManyToManyField = models.ManyToManyField(ProbaModel, related_name='ProbaMM')
	OneToOneField = models.OneToOneField(ProbaModel, related_name='ProbaOO')
	DateField = models.DateField()
	DateTimeField = models.DateTimeField()
	TimeField = models.TimeField()
	BinaryField = models.BinaryField()
	TextField = models.TextField()
