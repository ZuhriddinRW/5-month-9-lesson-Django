from django.db import models


class Category ( models.Model ) :
    title = models.CharField ( max_length=100 )

    def __str__(self) :
        return self.title


class News ( models.Model ) :
    title = models.CharField ( max_length=100, verbose_name='sarlovha' )
    content = models.TextField ( blank=True, null=True, verbose_name='Text' )
    created_at = models.DateTimeField ( auto_now_add=True, verbose_name='add_date' )
    updated_at = models.DateTimeField ( auto_now=True )
    photo = models.ImageField ( upload_to='photo/%Y/%m/%d', blank=True, null=True )
    bool = models.BooleanField ( default=False, verbose_name='Bool' )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE, default=1 )

    def __str__(self) :
        return self.title