import random

from faker import Faker

from .civil_servant.models import CivilServant
from .entity.models import Entity
from .formality.models import Formality


class FakerApp:
	def __init__(self, cant):
		self._fake = Faker('es_ES')
		self._cant = cant

	def _entities(self):
		for index in range(self._cant):
			Entity.objects.create(
				name=self._fake.name(),
				nit=self._fake.isbn13(separator="-"),
				address=self._fake.address(),
				telephone=self._fake.phone_number(),
				website=self._fake.uri()
			)

	def _formalities(self):
		civil_servants = CivilServant.objects_all.all()
		for index in range(self._cant):
			Formality.objects.create(
				name=self._fake.company(),
				description=self._fake.sentences(nb=3, ext_word_list=None),
				requirements=self._fake.sentences(nb=3, ext_word_list=None),
				realization_form=self._fake.catch_phrase(),
				schedule=self._fake.day_of_week(),
				civil_servant=random.choice(civil_servants),
			)

	def _civil_servants(self):
		entities = Entity.objects_all.all()
		for index in range(self._cant):
			username = f'{str.lower(self._fake.first_name())}2018'
			CivilServant.objects.create(
				first_name=self._fake.first_name(),
				last_name=self._fake.last_name(),
				username=username,
				identification_type='cc',
				identification=self._fake.msisdn(),
				telephone=self._fake.phone_number(),
				address=self._fake.address(),
				avatar='/static/assets/img/avatars/01_80x80.png',
				entity=random.choice(entities)
			)

	def run(self):
		self._entities()
		self._formalities()
		self._civil_servants()
