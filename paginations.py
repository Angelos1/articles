from rest_framework.pagination import CursorPagination

class CustomCursorPagination(CursorPagination):
    """Custom paginator extending the CursorPagination.
    The only thing changed is the field against which the cursor based pagination will be applied,
    set to the id field (default ordering field is the -created field which we do not have in the Article model)"""

    ordering = 'id'
