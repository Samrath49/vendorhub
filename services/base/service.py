from django.db import transaction


class BaseService:
    def __init__(self):
        self.errors = []

    def add_error(self, error):
        self.errors.append(str(error))

    def has_errors(self):
        return len(self.errors) > 0