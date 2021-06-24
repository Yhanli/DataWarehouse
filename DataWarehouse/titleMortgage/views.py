from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, renderers, generics
from rest_framework import permissions
from titleMortgage.models import *
from .serializers import *


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class StaffBrowsableMixin(object):
#     def get_renderers(self):
#         """
#         Add Browsable API renderer if user is staff.
#         """
#         rends = self.renderer_classes
#         if self.request.user and self.request.user.is_staff:
#             rends.append(renderers.BrowsableAPIRenderer)
#         return [renderer() for renderer in rends]


class TitleMortgageViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TitleMortgageSerializer
    queryset = TitleMortgage.objects.all()
