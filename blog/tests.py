from django.test import TestCase
from django.test import Client
from django.conf import settings
from .models import Article
from vitrine.models import Sector


# Create your tests here.


class TestCaseArticle(TestCase):

    def setUp(self):
        self.client = Client()
        Sector.objects.create(name="Habillement",
                              description="Description de l'habillement")
        Sector.objects.create(
            name="Chefferies", description="Description des chefferies")
        Sector.objects.create(
            name="Sculture", description="Description de la sculture")
        Sector.objects.create(
            name="Peinture", description="Description de la peinture")
        sectors = Sector.objects.all()
        Article.objects.create(
            title="Article1", summary="Résumé de l'article 1", published=True, sector=sectors[0], content="")
        Article.objects.create(
            title="Article2", summary="Résumé de l'article 2", published=True, sector=sectors[1], content="")
        Article.objects.create(
            title="Article3", summary="Résumé de l'article 3", published=True, sector=sectors[3], content="")
        Article.objects.create(
            title="Article4", summary="Résumé de l'article 4", published=True, sector=sectors[2], content="")
        Article.objects.create(
            title="Article5", summary="Résumé de l'article 5", published=True, sector=sectors[2], content="")
        Article.objects.create(
            title="Article6", summary="Résumé de l'article 6", published=True, sector=sectors[1], content="")

    def test_case_ajout_commentaire(self):
        from django.urls import reverse
        url = "/fr/blog/add-comment-ajax/"
        article = Article.objects.get(id=1)
        pre_count = article.comment_set.count()
        response = self.client.post(
            url, {"article": article.id, "author": "Jean Paul", "content": "Merveilleur article"})
        post_count = article.comment_set.count()
        self.assertEqual(pre_count+1, post_count)

    def test_case_ajout_plusieurs_commentaires(self):
        from django.urls import reverse
        url = "/fr/blog/add-comment-ajax/"

        article = Article.objects.get(id=1)
        pre_count = article.comment_set.count()
        number = settings.THROTTLE_ZONES["comment"]["BUCKET_CAPACITY"]
        for _ in range(number+100):
            try:
                response = self.client.post(
                    url, {"article": article.id, "author": f"Jean Paul {_}", "content ": f"Merveilleur article {_}"})
            except:
                break
        if _ == number-1:
            self.assertFalse(True)
