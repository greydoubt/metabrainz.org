from flask_wtf import FlaskForm
from flask_babel import lazy_gettext
from wtforms import StringField, validators, FieldList


class ApplicationForm(FlaskForm):
    client_name = StringField(lazy_gettext('Application Name'), [
        validators.InputRequired(message=lazy_gettext("Application name field is empty.")),
        validators.Length(min=3, message=lazy_gettext("Application name needs to be at least 3 characters long.")),
        validators.Length(max=64, message=lazy_gettext("Application name needs to be at most 64 characters long."))
    ])
    description = StringField(lazy_gettext('Description'), [
        validators.InputRequired(message=lazy_gettext("Client description field is empty.")),
        validators.Length(min=3, message=lazy_gettext("Client description needs to be at least 3 characters long.")),
        validators.Length(max=512, message=lazy_gettext("Client description needs to be at most 512 characters long."))
    ])
    website = StringField(lazy_gettext('Homepage'), [
        validators.InputRequired(message=lazy_gettext("Homepage field is empty.")),
        validators.URL(require_tld=False, message=lazy_gettext("Homepage is not a valid URI."))
    ])
    redirect_uri = FieldList(StringField(lazy_gettext('Authorization callback URL'), [
        validators.InputRequired(message=lazy_gettext("Authorization callback URL field is empty.")),
        validators.URL(require_tld=False, message=lazy_gettext("Authorization callback URL is invalid."))
    ]))

    def validate_redirect_uri(self, field):
        if not field.data.startswith(("http://", "https://")):
            raise validators.ValidationError(lazy_gettext('Authorization callback URL must use http or https'))

    def validate_website(self, field):
        if not field.data.startswith(("http://", "https://")):
            raise validators.ValidationError(lazy_gettext('Homepage URL must use http or https'))
