from django.shortcuts import render
from django.core.paginator import Paginator


def human_list_view(request):
    humans = Human.objects.all()

    # Создаем объект Paginator
    paginator = Paginator(humans, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'human_list.html', context)
