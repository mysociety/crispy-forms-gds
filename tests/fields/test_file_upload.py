"""
Tests to verify file uploads are rendered correctly.

"""
import os

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Field, Layout

from tests.forms import FileUploadForm
from tests.utils import TEST_DIR, parse_form, parse_contents

RESULT_DIR = os.path.join(TEST_DIR, "fields", "results", "file_upload")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = FileUploadForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = FileUploadForm(data={})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "validation_errors.html")


def test_show_label_as_heading():
    """Verify the field label can be displayed as the page heading."""
    form = FileUploadForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Field("file", context=dict(field_label_is_heading=True))
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_heading.html")


def test_change_label_size():
    """Verify size of the field label can be changed from the default."""
    form = FileUploadForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Field("file", context=dict(field_label_size="l")))
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_size.html")
