from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField('Название', unique=True, max_length=200)
    measurement_unit = models.CharField('Единица измерения', max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100,
        unique=True)
    color = models.CharField(
        'Цвет',
        max_length=7,
        unique=True)
    slug = models.SlugField(
        'Ссылка',
        max_length=100,
        unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Автор')
    title = models.CharField(
        'Название рецепта',
        max_length=200)
    image = models.ImageField(
        'Изображение рецепта',
        upload_to='static/recipe/',
        blank=True,
        null=True)
    text = models.TextField(
        'Описание рецепта')
    ingredients = models.ManyToManyField(
        Ingredient, related_name='recipes', through='RecipeIngredient',
        verbose_name='Ингредиенты')
    cook_time = models.PositiveSmallIntegerField(
        'Время приготовления (минут)',
        validators=[validators.MinValueValidator(
            1, message='Время приготовления не меньше минуты')])
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
        related_name='recipes')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', )

    def __str__(self):
        return f'{self.author.email}, {self.title}'


class RecipeIngredient(models.Model):
    amount = models.IntegerField('Количество')
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.ingredient.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorites',
                               verbose_name='Избранный рецепт')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'], name='unique_favorite')
        ]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='shopping_cart')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='shopping_cart')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'], name='unique_cart')
        ]
