from django.core.exceptions import PermissionDenied


class HasCommentPermissionMixin:

    def get(self, request, *args, **kwargs):

        if self.get_object().owner == self.request.user:
            return super().get(self, request, *args, **kwargs)
        else:
            raise PermissionDenied


class HasOrderPermissionMixin:

    def get(self, request, *args, **kwargs):

        if self.get_object().owner == self.request.user:
            return super().get(self, request, *args, **kwargs)
        else:
            raise PermissionDenied
