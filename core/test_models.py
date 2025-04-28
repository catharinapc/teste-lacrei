from django.test import TestCase
from .models import Profissional

class TestProfissionalModel(TestCase):
    def test_str(self):
        profissional = Profissional.objects.create(
            nome_social="Dra. Ana",
            profissao="Psicóloga",
            endereco="Rua X, 123",
            contato="(11) 99999-9999"
        )
        self.assertEqual(str(profissional), "Dra. Ana")