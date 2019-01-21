from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Order, Review
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .forms import ReviewForm, ProdForm
from django.views.generic.edit import CreateView
from django.template.defaultfilters import slugify
from unidecode import unidecode


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    if request.method == 'POST':
        rform = ReviewForm(request.POST)
        if rform.is_valid():
            cd = rform.cleaned_data
            p = Product.objects.get(pk=id)
            review_obj = Review.objects.create(user=request.user, review_text=cd['review_text'], product=p)
        return redirect(reverse('shop:product_detail', args=[id, p.slug]))
    else:
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        reviews = Review.objects.filter(product=product)
        form = ReviewForm()
        return render(request,
                      'shop/product/detail.html',
                      {'product': product,
                       'reviews': reviews,
                       'form': form})


class CartView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'shop/product/cart.html'

    def get(self, request, *args, **kwargs):
        if 'product_id' in kwargs:
            return redirect(reverse('shop:cart'))
        context = {'orders': Order.objects.filter(user=request.user)}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        p = Product.objects.get(pk=request.POST['product_id'])

        if Order.objects.filter(user=request.user, product=request.POST['product_id']).count() == 0:
            order_obj = Order.objects.create(user=request.user, product=p)
            order_obj.count = 1
            order_obj.save()
        else:
            order_obj = Order.objects.get(user=request.user, product=request.POST['product_id'])
            order_obj.count += 1
            order_obj.save()
        return redirect(request.META['HTTP_REFERER'])

class CreateProd(LoginRequiredMixin, CreateView):
    form_class = ProdForm
    success_url = reverse_lazy('shop:product_list')
    template_name = 'shop/product/create.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.slug = slugify(unidecode(form.instance.name))
            return super().form_valid(form)
        return redirect(reverse_lazy('account:login'))


