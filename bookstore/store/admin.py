from django.contrib import admin
from .models import Author, Book

class BookInline(admin.TabularInline):  
    model = Book  
    extra = 1  

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    inlines = [BookInline]  # Enables inline book editing inside the author admin page

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author',)
    search_fields = ('title',)

    actions = ['apply_discount']

    def apply_discount(self, request, queryset):
        for book in queryset:
            book.price *= 0.9  # Reduce price by 10%
            book.save()
        self.message_user(request, "Discount applied successfully!")

    apply_discount.short_description = "Apply 10% discount to selected books"
