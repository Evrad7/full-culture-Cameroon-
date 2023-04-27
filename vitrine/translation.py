from modeltranslation.translator import register, TranslationOptions
from .models import Sector, Region, Company, Content


@register(Sector)
class SectorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('slogan', 'description')


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'body', )
