from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Импортируем messages для вывода сообщений об ошибках
from .models import Product, Category, ShoppingCart
from users.models import User
from .utils import paginate
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

PAGE_FOR_LIST = 8


def index(request):
    title = 'КомфортСтрой'
    context = {
        'title': title
    }
    return render(request, 'products/index.html', context)


def products_list(request):
    product = Product.objects.all()
    page_obj = paginate(request, product, PAGE_FOR_LIST)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'products/products_list.html', context)


def products_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    in_cart = False  # По умолчанию предполагаем, что товар не добавлен в корзину

    # Проверяем, аутентифицирован ли пользователь
    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, проверяем, есть ли товар в корзине
        in_cart = ShoppingCart.objects.filter(user=request.user, product=product).exists()

    context = {
        'product': product,
        'in_cart': in_cart,
    }
    return render(request, 'products/products_detail.html', context)

@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            return redirect('products:products_detail', product_id=product_id)
        else:
            messages.error(request, 'Пожалуйста, напишите комментарий')  
    
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'products/comment_form.html', context)


def comment_form(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'products/comment_form.html', context)


def category_list(request, category_id):
    category_name = Category.objects.get(id=category_id)
    product = Product.objects.filter(category=category_name)
    page_obj = paginate(request, product, PAGE_FOR_LIST)
    context = {
        'page_obj': page_obj,
        'category_name': category_name,
    }
    return render(request, 'products/category_list.html', context)


def profile(request, username):
    title = "Профиль"
    user = get_object_or_404(User, username=username)
    card = ShoppingCart.objects.filter(user=user.id)
    card_products = card.all()
    count_products = card_products.count()
    page_obj = paginate(request, card_products, PAGE_FOR_LIST)

    context =  {
        'page_obj': page_obj,
        'user': user,
        'title': title,
        'count_products': count_products,
    }
    return render(request, 'products/profile.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ShoppingCart.objects.create(user=request.user, product=product)
    return redirect('products:products_detail', product_id=product_id)


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ShoppingCart.objects.filter(user=request.user, product=product).delete()
    return redirect('products:products_detail', product_id=product_id)


@login_required
def remove_from_cart_profile(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ShoppingCart.objects.filter(user=request.user, product=product).delete()
    return redirect('products:profile', username=request.user.username)


def search_view(request):
    query = request.GET.get('query')
    if query:
        # Выполните частичный поиск товаров по названию
        products = Product.objects.filter(Q(name__icontains=query))
        count_products = products.count()
    else:
        products = None
    return render(request, 'products/search_results.html', {'products': products,
                                                            'count_products': count_products})
