# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

# class CategoryOwnerFilter(RelatedFieldListFilter):
#
#     @classmethod
#     def test(cls, field, request, params, model, admin_view, field_path):
#         return field.name == 'category'
#
#     def __init__(self, field, request, params, model, model_admin, field_path):
#         super().__init__(field, request, params, model, model_admin, field_path)
#         # 重新获取lookup_choices，根据owner过滤
#         self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')
#
#
# manager.register(CategoryOwnerFilter, take_priority=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('category', 'title'),
        'desc'
        'status',
        'content',
        'tag'
    )
    # exclude = ['owner']
    # form_layout = (
    #     Fieldset(
    #         '基础信息',
    #         Row("title", "category"),
    #         'status',
    #         'tag',
    #     ),
    #     Fieldset(
    #         '内容信息',
    #         'desc',
    #         'is_md',
    #         'content_ck',
    #         'content_md',
    #         'content',
    #     )
    # )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
#
#     # def get_media(self):
#         # # xadmin基于bootstrap，引入会页面样式冲突，仅供参考, 故注释。
#         # media = super().get_media()
#         # media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
#         # media.add_css({
#             # 'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
#         # })
#         # return media
