from django.test import TestCase
from app1.models import ProbaModel

class ProbaTestCase(TestCase):

	def test_bulk_create(self):
		ProbaModel.objects.bulk_create(
				[
					ProbaModel(num=1),
					ProbaModel()
				]
			)
