from django.contrib import admin

from app_sindicato.models import Socio, Sindicato

class SocioAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'nome', 'cpf', 'matricula', 'updated', 'imprimir')
    list_display_links = ('nome', 'cpf', 'matricula')
    search_fields = ('nome', 'cpf', 'matricula')
    list_filter = ['nome', 'cpf']
    fieldsets = (
        ('Dados Pessoais', {'fields': (
            'nome',
            'cpf',
            'rg',
            'ssp',
            'data_exp',
            'cnh',
            'categoria',
            'titulo',
            'nacionalidade',
            'fator_rh',
            'naturalidade',
            'uf',
            'sexo',
            'data_nascimento',
            'estado_sivil',
            'conjugue',
            'dependentes',
            'email',
            'pai',
            'mae'
        ), 'classes': 'collapse'}),
        ('Endereço', {'fields': (
            'endereco',
            'numero',
            'bairro',
            'cep',
            'cidade',
            'estado',
            'fone_resid',
            'celular'
        ), 'classes': 'collapse wide'}),
        ('Dados Profissionais', {'fields': (
            'profissao',
            'data_admissao',
            'placa_veiculo',
            'concessao',
            'categorias',
            'foto',
            'sindicato'
        ), 'classes': 'collapse wide'}),
    )

    class Media:
        css = {
            'all': ('css/formsistema.css',)
        }
        js = (
            'js/jquery.maskedinput.js',
            'js/scripts.js',
        )



    def imprimir(self, object):
        return '<a class="grp-button" target="_blank" href=/admin/socio/%s/imprimir/><span class="ui-icon  ui-icon-print"></span><a/>' %(object.id)
    imprimir.allow_tags = True






admin.site.register(Sindicato)
admin.site.register(Socio, SocioAdmin)

