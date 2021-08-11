from django.db import models
# импорт юзера
from users.models import User

from .validators import score_validation


class Comment(models.Model):
    text = models.TextField(verbose_name='Комментарий',
                            help_text='Введите текст комментария')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField(verbose_name='Отзыв', help_text='Напишите отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(validators=[score_validation],
                                help_text='Поставьте оценку произведению'
                                          ' от 1 до 10')
