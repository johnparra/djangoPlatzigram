from typing import List

# Django
from django.shortcuts import render

data: List = [
    {
        'description': 'The tiger',
        'foot_page': 'One big beast of the Earth',
        'picture': 'https://www.cityofboise.org/media/5049/tiger.jpg'
    }, {
        'description': 'The phoenix',
        'foot_page': 'Bird than burn to recreate your life',
        'picture': 'https://img.elo7.com.br/product/zoom/28C656D/fenix-fenix.jpg'
    }, {
        'description': 'The shark',
        'foot_page': 'One creature with many habilities',
        'picture': 'https://www.24newshd.tv/uploads/facebook_post_images/2020-07-04/facebook_post_image_1593865708.jpg'
    }
]


def list_posts(request):
    return render(request, 'feed.html', {'posts': data})
