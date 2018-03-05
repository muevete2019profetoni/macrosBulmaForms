# flask_bulma_layout_form
Example layout and macro for bulma in Flask Jinja template.  It uses CDN version of bulma and font-awesome

This is a work in progress and won't be formalized, use at your own risk.

In the HTML files you can extend the basic layout and then import macro.html for the field rendering.
This first installment includes only VERTICAL fields.  Enjoy.

# An example of usage

```html
{% extends 'layout.html' %}
{% import macros.html as bulma %}
{% block title %}example page{% endblock %}
{% block content %}
<form>
{{ bulma.input(name="username", label="Username" value=some_username) }}
{{ bulma.field(name="email", label="Email", value=some_email, licon="fa-envelope") }}
{{ bulma.textfield(name="comments", label="comments") }}

<!-- buttons are too simple, so I don't use a macro approach -->
<div class="field is-grouped">
  <div class="control">
    <button class="button is-link">Submit</button>
  </div>
  <div class="control">
    <button class="button is-text">Cancel</button>
  </div>
</div>

</form>
{% endblock %}
```
