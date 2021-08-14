from django.db import models

from users.models import User

from titles.models import Title

from .validators import score_validation


class Review(models.Model):

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Отзыв', help_text='Напишите отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(validators=[score_validation],
                                help_text='Поставьте оценку произведению'
                                          ' от 1 до 10')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique review')
        ]


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий',
                            help_text='Введите текст комментария')
