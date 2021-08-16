from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from titles.models import Title
from users.models import User


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews', db_index=True)
    text = models.TextField(verbose_name='Отзыв', help_text='Напишите отзыв',
                            db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)],
                                db_index=True)

    class Meta:
        ordering = ('-pub_date', 'score')
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique review')
        ]


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments',
                               db_index=True)
    text = models.TextField(verbose_name='Комментарий',
                            help_text='Введите текст комментария',
                            db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               db_index=True)

    class Meta:
        ordering = ('-pub_date',)
