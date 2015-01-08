class MarketingRouter(object):
    """
    A router to control all database operations on models in the
    marketing application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read marketing models go to marketing_db.
        """
        if model._meta.app_label == 'marketing':
            return 'marketing_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write marketing models go to marketing_db.
        """
        if model._meta.app_label == 'marketing':
            return 'marketing_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the marketing app is involved.
        """
        if obj1._meta.app_label == 'marketing' or \
           obj2._meta.app_label == 'marketing':
           return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the marketing app only appears in the 'marketing_db'
        database.
        """
        if db == 'marketing_db':
            return model._meta.app_label == 'marketing'
        elif model._meta.app_label == 'marketing':
            return False
        return None