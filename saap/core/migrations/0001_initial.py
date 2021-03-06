# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-02 13:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import image_cropping.fields
import saap.core.models
import saap.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', image_cropping.fields.ImageCropField(blank=True, null=True, upload_to='avatars/', validators=[saap.core.models.avatar_validation], verbose_name='profile picture')),
                ('cropping', image_cropping.fields.ImageRatioField('avatar', '70x70', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text='Note that the preview above will only be updated after you submit the form.', hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('menu_dados_auxiliares', 'Mostrar Menu Dados Auxiliares'), ('menu_tabelas_auxiliares', 'Mostrar Menu de Tabelas Auxiliares'), ('menu_contatos', 'Mostrar Menu de Cadastro de Contatos'), ('menu_grupocontatos', 'Mostrar Menu de Cadastro de Grupos de Contatos'), ('menu_processos', 'Mostrar Menu de Cadastro de Processos'), ('menu_area_trabalho', 'Mostrar Menu de Áreas de Trabalho'), ('menu_impresso_enderecamento', 'Mostrar Menu de Impressos de Endereçamento'), ('menu_relatorios', 'Mostrar Menu de Relatórios')),
                'abstract': False,
            },
            managers=[
                ('objects', saap.core.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AreaTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(blank=True, default='', max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(default='', max_length=254, verbose_name='Descrição')),
                ('modifier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier')),
            ],
            options={
                'verbose_name_plural': 'Áreas de Trabalho',
                'verbose_name': 'Área de Trabalho',
            },
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, unique=True, verbose_name='Bairro')),
                ('codigo', models.PositiveIntegerField(default=0, help_text='Código do Bairro no Cadastro Oficial do Município', verbose_name='Código')),
                ('outros_nomes', models.TextField(blank=True, help_text='Ocorrências similares', verbose_name='Outros Nomes')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name_plural': 'Bairros',
                'verbose_name': 'Bairro',
            },
        ),
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=9, unique=True, verbose_name='CEP')),
            ],
            options={
                'ordering': ('numero',),
                'verbose_name_plural': "CEP's",
                'verbose_name': 'CEP',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, unique=True, verbose_name='Nome do Distrito')),
            ],
            options={
                'verbose_name_plural': 'Distritos',
                'verbose_name': 'Distrito',
            },
        ),
        migrations.CreateModel(
            name='Filiacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data Filiação')),
                ('data_desfiliacao', models.DateField(blank=True, null=True, verbose_name='Data Desfiliação')),
            ],
            options={
                'ordering': ('parlamentar', '-data', '-data_desfiliacao'),
                'verbose_name_plural': 'Filiações',
                'verbose_name': 'Filiação',
            },
        ),
        migrations.CreateModel(
            name='ImpressoEnderecamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome do Impresso')),
                ('tipo', models.CharField(choices=[('ET', 'Folha de Etiquetas'), ('EV', 'Envelopes')], default='ET', max_length=2, verbose_name='Tipo do Impresso')),
                ('largura_pagina', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Largura da Página')),
                ('altura_pagina', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Altura da Página')),
                ('margem_esquerda', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Margem Esquerda')),
                ('margem_superior', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Margem Superior')),
                ('colunasfolha', models.PositiveSmallIntegerField(verbose_name='Colunas')),
                ('linhasfolha', models.PositiveSmallIntegerField(verbose_name='Linhas')),
                ('larguraetiqueta', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Largura da Etiqueta')),
                ('alturaetiqueta', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Altura da Etiquta')),
                ('entre_colunas', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Distância Entre Colunas')),
                ('entre_linhas', models.DecimalField(decimal_places=2, help_text='Em centímetros', max_digits=5, verbose_name='Distância Entre Linhas')),
                ('fontsize', models.DecimalField(decimal_places=2, help_text='Em Pixels', max_digits=5, verbose_name='Tamanho da Letra')),
                ('rotate', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Rotacionar Texto')),
            ],
            options={
                'verbose_name_plural': 'Impressos para Endereçamento',
                'verbose_name': 'Impresso para Endereçamento',
            },
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, unique=True, verbose_name='Logradouro')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name_plural': 'Logradouros',
                'verbose_name': 'Logradouro',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('PB', 'Paraíba'), ('PA', 'Pará'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins'), ('EX', 'Exterior')], max_length=2)),
                ('regiao', models.CharField(blank=True, choices=[('CO', 'Centro-Oeste'), ('NE', 'Nordeste'), ('NO', 'Norte'), ('SE', 'Sudeste'), ('SL', 'Sul'), ('EX', 'Exterior')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Municípios',
                'verbose_name': 'Município',
            },
        ),
        migrations.CreateModel(
            name='NivelInstrucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Nível de Instrução')),
            ],
            options={
                'verbose_name_plural': 'Níveis Instrução',
                'verbose_name': 'Nível Instrução',
            },
        ),
        migrations.CreateModel(
            name='OperadorAreaTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('areatrabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operadorareatrabalho_set', to='core.AreaTrabalho', verbose_name='Área de Trabalho')),
                ('grupos_associados', models.ManyToManyField(related_name='operadorareatrabalho_set', to='auth.Group', verbose_name='Grupos Associados')),
                ('modifier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operadorareatrabalho_set', to=settings.AUTH_USER_MODEL, verbose_name='Operador da Área de Trabalho')),
            ],
            options={
                'verbose_name_plural': 'Operadores',
                'verbose_name': 'Operador',
            },
        ),
        migrations.CreateModel(
            name='Parlamentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('nome_parlamentar', models.CharField(max_length=50, verbose_name='Nome Parlamentar')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, verbose_name='Sexo')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data Nascimento')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='C.P.F')),
                ('rg', models.CharField(blank=True, max_length=15, verbose_name='R.G.')),
                ('titulo_eleitor', models.CharField(blank=True, max_length=15, verbose_name='Título de Eleitor')),
                ('numero_gab_parlamentar', models.CharField(blank=True, max_length=10, verbose_name='Nº Gabinete')),
                ('telefone', models.CharField(blank=True, max_length=50, verbose_name='Telefone')),
                ('fax', models.CharField(blank=True, max_length=50, verbose_name='Fax')),
                ('endereco_residencia', models.CharField(blank=True, max_length=100, verbose_name='Endereço Residencial')),
                ('cep_residencia', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('telefone_residencia', models.CharField(blank=True, max_length=50, verbose_name='Telefone Residencial')),
                ('fax_residencia', models.CharField(blank=True, max_length=50, verbose_name='Fax Residencial')),
                ('endereco_web', models.URLField(blank=True, max_length=100, verbose_name='HomePage')),
                ('profissao', models.CharField(blank=True, max_length=50, verbose_name='Profissão')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='E-mail')),
                ('locais_atuacao', models.CharField(blank=True, max_length=100, verbose_name='Locais de Atuação')),
                ('ativo', models.BooleanField(verbose_name='Ativo na Casa?')),
                ('biografia', models.TextField(blank=True, verbose_name='Biografia')),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to=saap.core.models.foto_upload_path, validators=[saap.utils.restringe_tipos_de_arquivo_img], verbose_name='Fotografia')),
                ('municipio_residencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Municipio', verbose_name='Município')),
                ('nivel_instrucao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.NivelInstrucao', verbose_name='Nível Instrução')),
            ],
            options={
                'ordering': ['nome_parlamentar'],
                'verbose_name_plural': 'Parlamentares',
                'verbose_name': 'Parlamentar',
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=9, verbose_name='Sigla')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('data_criacao', models.DateField(blank=True, null=True, verbose_name='Data Criação')),
                ('data_extincao', models.DateField(blank=True, null=True, verbose_name='Data Extinção')),
            ],
            options={
                'verbose_name_plural': 'Partidos',
                'verbose_name': 'Partido',
            },
        ),
        migrations.CreateModel(
            name='RegiaoMunicipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Região Municipal')),
                ('tipo', models.CharField(choices=[('AU', 'Área Urbana'), ('AR', 'Área Rural'), ('UA', 'Área Única')], default='AU', max_length=2, verbose_name='Tipo da Região')),
            ],
            options={
                'verbose_name_plural': 'Regiões Municipais',
                'verbose_name': 'Região Municipal',
            },
        ),
        migrations.CreateModel(
            name='SituacaoMilitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Situação Militar')),
            ],
            options={
                'verbose_name_plural': 'Tipos Situações Militares',
                'verbose_name': 'Tipo Situação Militar',
            },
        ),
        migrations.CreateModel(
            name='TipoLogradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, unique=True, verbose_name='Tipo de Logradouro')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name_plural': 'Tipos de Logradouros',
                'verbose_name': 'Tipo de Logradouro',
            },
        ),
        migrations.CreateModel(
            name='Trecho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('lado', models.CharField(choices=[('NA', 'Não Aplicável'), ('AL', 'Ambos os Lados'), ('LE', 'Lado Esquerdo'), ('LD', 'Lado Direito')], default='AL', max_length=2, verbose_name='Lado do Logradouro')),
                ('numero_inicial', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número Inicial')),
                ('numero_final', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número Final')),
                ('bairro', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.Bairro', verbose_name='Bairro')),
                ('cep', models.ManyToManyField(related_name='trechos_set', to='core.Cep', verbose_name='Cep')),
                ('distrito', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.Distrito', verbose_name='Distrito')),
                ('logradouro', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.Logradouro', verbose_name='Logradouro')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.Municipio', verbose_name='Município')),
                ('regiao_municipal', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.RegiaoMunicipal', verbose_name='Região Municipal')),
                ('tipo', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trechos_set', to='core.TipoLogradouro', verbose_name='Tipo de Logradouro')),
            ],
            options={
                'ordering': ['municipio__nome', 'regiao_municipal__nome', 'distrito__nome', 'bairro__nome', 'tipo__nome', 'logradouro__nome'],
                'verbose_name_plural': 'Trechos de Logradouro',
                'verbose_name': 'Trecho de Logradouro',
            },
        ),
        migrations.AlterUniqueTogether(
            name='regiaomunicipal',
            unique_together=set([('nome', 'tipo')]),
        ),
        migrations.AddField(
            model_name='parlamentar',
            name='situacao_militar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SituacaoMilitar', verbose_name='Situação Militar'),
        ),
        migrations.AddField(
            model_name='filiacao',
            name='parlamentar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parlamentar'),
        ),
        migrations.AddField(
            model_name='filiacao',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Partido', verbose_name='Partido'),
        ),
        migrations.AddField(
            model_name='areatrabalho',
            name='operadores',
            field=models.ManyToManyField(related_name='areatrabalho_set', through='core.OperadorAreaTrabalho', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='areatrabalho',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='areatrabalho',
            name='parlamentar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areatrabalho_set', to='core.Parlamentar', verbose_name='Parlamentar'),
        ),
        migrations.AlterUniqueTogether(
            name='trecho',
            unique_together=set([('municipio', 'regiao_municipal', 'distrito', 'bairro', 'logradouro', 'tipo', 'lado', 'numero_inicial', 'numero_final')]),
        ),
    ]
