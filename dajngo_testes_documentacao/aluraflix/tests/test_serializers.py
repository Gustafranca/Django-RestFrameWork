from django.test import TestCase
from aluraflix.models import Programa 
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            data_lancamento = '2003-07-94',
            tipo = 'F',
            likes= 2332,
            dislikes = 40,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)
        
    def test_verifica_campos_serializados(self):
        """TESTE QUE VERIFICA OS CAMPOS QUE ESTAO SENDO SERIALIZADOS"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo','tipo', 'data_lancamento','likes']))
        
    def test_verifica_conteudo_dos_campos_serialzados(self):
        """TESET QUE VERIFICA O CONTEUDO DOS CAMPOS SERIALIZADOS"""

        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
