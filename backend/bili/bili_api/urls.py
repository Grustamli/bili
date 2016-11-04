from django.conf.urls import (url, include)
from rest_framework_swagger.views import get_swagger_view
from .views import (
                    ProfileListView,
                    ProfileCreateView,
                    ProfileDetailView,
                    PhoneNumberListView,
                    PhoneNumberCreateView,
                    PhoneNumberDetailView,
                    AddressListView,
                    AddressCreateView,
                    AddressDetailView,
                    AdListView,
                    AdCreateView,
                    AdDetailView,
                    AdImageListView,
                    AdImageCreateView,
                    AdImageDetailView,
                    FavoriteListView,
                    FavoriteCreateView,
                    FavouriteDetailView,
                    CategoryListView,
                    CategoryDetailView,
                    api_root)


urlpatterns = [
    url(r'^root/$', api_root),
    url(r'^profiles/$', ProfileListView.as_view(), name='profile-list'),
    url(r'^profiles/create$', ProfileCreateView.as_view(), name='profile-create'),
    url(r'^profiles/(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^phone-numbers/$', PhoneNumberListView.as_view(), name='phone-list'),
    url(r'^phone-numbers/create$', PhoneNumberCreateView.as_view(), name='phone-create'),
    url(r'^phone-numbers/(?P<pk>[1-9]+)/$', PhoneNumberDetailView.as_view(), name='phone-detail'),
    url(r'^addresses/$', AddressListView.as_view(), name='address-list'),
    url(r'^addresses/create$', AddressCreateView.as_view(), name='address-create'),
    url(r'^addresses/(?P<pk>[1-9]+)/$', AddressDetailView.as_view(), name='address-detail'),
    url(r'^ads/$', AdListView.as_view(), name='ad-list'),
    url(r'^ads/create$', AdCreateView.as_view(), name='ad-create'),
    url(r'^ads/(?P<slug>[\w-]+)/$', AdDetailView.as_view(), name='ad-detail'),
    url(r'^ad-images/$', AdImageListView.as_view(), name='adimage-list'),
    url(r'^ad-images/create$', AdImageCreateView.as_view(), name='adimage-create'),
    url(r'^ad-images/(?P<pk>[1-9]+)/$', AdImageDetailView.as_view(), name='adimage-detail'),
    url(r'^favourites/$', FavoriteListView.as_view(), name='favourite-list'),
    url(r'^favourites/create$', FavoriteCreateView.as_view(), name='favourite-create'),
    url(r'^favourites/(?P<pk>[1-9]+)/$', FavouriteDetailView.as_view(), name='favourite-detail'),
    url(r'^categories/$', CategoryListView.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>[1-9]+)/$', CategoryDetailView.as_view(), name='category-detail')
]

schema_view = get_swagger_view(title='Bili API')

urlpatterns += [url(r'^$', schema_view)]
