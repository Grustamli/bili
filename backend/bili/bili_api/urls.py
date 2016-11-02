from django.conf.urls import (url, include)
from .views import (
                    ProfileListView,
                    ProfileDetailView,
                    PhoneNumberListView,
                    PhoneNumberDetailView,
                    AddressListView,
                    AddressDetailView,
                    AdListView,
                    AdDetailView)
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'persons', RegisterViewSet)
# router.register(r'phone-numbers', PhoneViewSet)
# router.register(r'profiles', ProfileViewSet)
# router.register(r'addresses', AddressViewSet)
# router.register(r'ads', AdViewSet)
#

# urlpatterns = router.urls
urlpatterns = [
    url(r'^profiles/$', ProfileListView.as_view(), name='profile-list'),
    url(r'^profiles/(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    url(r'^phone-numbers/$', PhoneNumberListView.as_view(), name='phone-list'),
    url(r'^phone-numbers/(?P<pk>[1-9]+)/$', PhoneNumberDetailView.as_view(), name='phone-detail'),
    url(r'^addresses/$', AddressListView.as_view(), name='address-list'),
    url(r'^addresses/(?P<pk>[1-9]+)/$', AddressDetailView.as_view(), name='address-detail'),
    url(r'^ads/$', AdListView.as_view(), name='ad-list'),
    url(r'^ads/(?P<slug>[\w-]+)/$', AdDetailView.as_view(), name='ad-detail')
    # url(r'^ads/(?P<pk>[1-9]+)/$', AdDetailView.as_view(), name='ad-detail')

]
