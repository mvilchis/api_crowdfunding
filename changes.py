from api_core.models import (FundingDeuda, ProjectCapital, ProjectDeuda,
                             ProjectDonation, ProjectRecompesas, User,
                             UserDeuda)
from django.db.models import Count, Max

# Cambio 1
doopla = User.objects.filter(username='doopla')[0]
ProjectDeuda.objects.filter(
    user=doopla, TasaInteresAnual__isnull=True).delete()
# Cambio 2
kubo = User.objects.filter(username='kubo')[0]
FundingDeuda.objects.filter(user=kubo, Fondeadores__isnull=True).delete()
#Cambio 3
UserDeuda.objects.filter(user=kubo, CodigoPostal__isnull=True).delete()
# Cambio 4
unique_fields = ['IdUsuario', 'IdProyecto']

duplicates = (ProjectDeuda.objects.filter(user=kubo).values(
    *unique_fields).order_by().annotate(
        max_id=Max('id'), count_id=Count('id')).filter(count_id__gt=1))

for duplicate in duplicates:
    (ProjectDeuda.objects.filter(**{x: duplicate[x]
                                    for x in unique_fields}).exclude(
                                        id=duplicate['max_id']).delete())
# Delete pruebas
ProjectCapital.objects.filter(Categoria='Prueba').delete()
ProjectDeuda.objects.filter(Categoria='Prueba').delete()
ProjectRecompesas.objects.filter(Categoria='Prueba').delete()
ProjectDonation.objects.filter(Categoria='Prueba').delete()
