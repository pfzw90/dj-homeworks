from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from pprint import pprint

from .models import Article, Scope, ArticleScopes

ERRORS = {
    'unique_main_scope_error': 'Статья может иметь только одну основную тему.',
    'no_main_scope_error': 'Статья должна иметь одну основную тему.',
    'delete_single_main_scope_error': 'Назначьте другую тему основной перед удалением.',
    'delete_all_main_scopes_error': 'Нельзя удалить все основные темы.',
}


class ArticleScopesInlineFormset(BaseInlineFormSet):

    @staticmethod
    def error(err):
        raise ValidationError(ERRORS[err])

    def clean(self):

        main_in_form = False
        delete_main = False
        err = None
        n = 0

        for form in self.forms:
            main = form.cleaned_data.get('is_main')
            delete = form.cleaned_data.get('DELETE')

            if main and delete:
                if not main_in_form and n > 0:
                    err = 'delete_single_main_scope_error'
                else:
                    main_in_form = True
                    delete_main = True

            elif main and not delete:
                if main_in_form and not delete_main:
                    err = 'unique_main_scope_error'
                else:
                    main_in_form = True

            if main_in_form and delete and delete_main and n > 0:
                err = 'delete_all_main_scopes_error'

            if not main and not main_in_form:
                err = 'no_main_scope_error'

            if err:
                self.error(err)
            else:
                n += 1

        return super().clean()


class ArticleScopesInline(admin.TabularInline):
    model = ArticleScopes
    formset = ArticleScopesInlineFormset


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopesInline]
