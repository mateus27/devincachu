# -*- coding: utf-8 -*-
import unittest

from django.contrib.auth import models as auth_models
from django.db import models as django_models

from destaques import models


class DestaqueTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.field_names = [f.name for f in models.Destaque._meta.fields]

    def test_model_destaque_deve_ter_um_campo_titulo(self):
        self.assertIn('titulo', self.field_names)

    def test_campo_titulo_deve_ser_CharField(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'titulo'][0]
        self.assertIsInstance(field, django_models.CharField)

    def test_campo_titulo_nao_deve_aceitar_blank(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'titulo'][0]
        self.assertFalse(field.blank)

    def test_campo_titulo_deve_ter_no_maximo_60_caracteres(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'titulo'][0]
        self.assertEquals(60, field.max_length)

    def test_model_destaque_deve_ter_um_campo_conteudo(self):
        self.assertIn('conteudo', self.field_names)

    def test_campo_conteudo_deve_ser_CharField(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'conteudo'][0]
        self.assertIsInstance(field, django_models.CharField)

    def test_campo_conteudo_nao_deve_aceitar_blank(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'conteudo'][0]
        self.assertFalse(field.blank)

    def test_campo_conteudo_deve_ter_no_maximo_500_caracteres(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'conteudo'][0]
        self.assertEquals(500, field.max_length)

    def test_model_destaque_deve_ter_um_campo_autor(self):
        self.assertIn('autor', self.field_names)

    def test_campo_autor_deve_ser_uma_FK(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'autor'][0]
        self.assertIsInstance(field, django_models.ForeignKey)

    def test_campo_autor_deve_ser_uma_FK_para_o_model_User_da_app_auth(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'autor'][0]
        self.assertEquals(auth_models.User, field.related.parent_model)

    def test_model_destaque_deve_ter_data(self):
        self.assertIn('data', self.field_names)

    def test_campo_data_deve_ser_do_tipo_datetime(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'data'][0]
        self.assertIsInstance(field, django_models.DateTimeField)

    def test_campo_data_deve_ter_auto_now_False(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'data'][0]
        self.assertFalse(field.auto_now)

    def test_campo_data_deve_ter_auto_now_add_True(self):
        field = [f for f in models.Destaque._meta.fields if f.name == 'data'][0]
        self.assertTrue(field.auto_now_add)