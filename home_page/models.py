from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class Teacher(models.Model):
    """Класс описания модели Преподавателя
    Основные поля: Имя, SLUG, краткая информация, фото, возраст, опыт, дополнительная информация, персональный рейтинг,
    стоимость проводимого урока, количество проведенных уроков, язык преподавания
    """

    def validate_photo(self):
        """ Функция валидации фото преподавателя. Вводится ограничение на размер файлв"""
        megabyte_limit = 10.0
        if self.file.size > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    # Имя преподавателя
    name = models.CharField(max_length=80, db_index=True, verbose_name='Имя преподавателя')
    #
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name='URL')
    # Краткая информация, изложенная в превью
    brief_info = models.CharField(max_length=400, verbose_name='Краткая информация')
    # Фото преподавателя
    photo = ResizedImageField(size=[400, 400], validators=[validate_photo, FileExtensionValidator(
        allowed_extensions=['jpg', 'jpeg', 'png'])], verbose_name="Фото преподавателя", blank=True, null=True)
    # Возраст (Не знаю, зачем)
    age = models.IntegerField(default=0)
    # Опыт преподавателя, в том числе и описание
    experience = models.CharField(max_length=400, verbose_name="Профессиональный опыт")
    # Дополнительная информация, в том числе и персональная
    add_info = models.CharField(max_length=1000, verbose_name="Дополнительная информация")
    # Время проведения уроков в виде массива дней и часов
    # lessons_time =
    # Персональный рейтинг преподавателя
    rating = models.IntegerField(default=0, verbose_name="Персональный рейтинг")
    # Стоимость проводимых уроков
    price = models.IntegerField(default=0)
    # Количество проведённых уроков
    lessons_amount = models.IntegerField(default=0)
    # Персональные интересы, перечисленные в пунктах
    #    personal_interests =
    # Язык преподавания
    language = models.CharField(max_length=100)

    def __str__(self):
        """"""
        return self.name

    def get_absolute_url(self):
        """Функция возвращает ссылку на преподавателя по его слагу"""
        return reverse('teacher', kwargs={'teacher_slug': self.slug})

    class Meta:
        """Описание класса Мета внутри класса преподавателя для изменений на Admin-странице"""
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['rating', 'name']
