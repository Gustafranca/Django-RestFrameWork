from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class CursosTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
        email='gusta@gmail.com',
        password='123123',
        username='guug'
        )
        self.client.force_authenticate(self.user)
        self.list_url = reverse('Cursos-list') 
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT', descricao='Curso teste 1', nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso teste 2', nivel = 'A'
        )
        
    def test_requisicao_list_curso(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_requisicao_creat_curso(self):
        """Teste para verificar a requisição POST para criar um cursos"""
        data = {
            'codigo_curso':'CTT3',
            'descricao': 'Curso teste 3',
            'nivel' : 'I'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_requesicao_delete_curso(self):
        """Teste para verificar a requisição DELETE nao permitida deletar um cursos"""
        
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_requesicao_PUT_atualziar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um cursos"""
        data={
            'codigo_curso':'Curso teste 1',
            'descricao':'Curso teste 1 atualizado',
            'nivel' : 'I'
        }
        response = self.client.put('/curso/1/',data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)