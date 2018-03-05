# flask_bulma_layout_form
Example layout and macro for Bulma in Flask Jinja template.  It uses CDN version of Bulma and Font-Awesome.

Bulma project: https://bulma.io

Bulma is a very lightweight excellent pure CSS framework based on Flexbox.  No javascript included, so you can pick your
own best of class library.

This is a work in progress intended for only simple projects and won't be formalized-- use at your own risk.
If you find it useful, drop me a note.
Better yet, if you improve it or make a much better package, let me know and I can link to it!!

In the HTML files you can extend the basic layout and then import macro.html for the field rendering.
This first installment includes only VERTICAL fields.  Enjoy.

# An example of usage

```html
{% extends 'layout.html' %}
{% import 'macros.html' as bulma %}
{% block title %}example page{% endblock %}
{% block content %}
<form>
{{ bulma.input(name="username", label="Username", value=some_username) }}
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

## Macros included:

1. field() - input and label with icons and status coloring
2. input() - simple text input field and label
3. checkbox() - simple checkbox field
4. ckeditor() - a CDN javascript rich-text-editor, not really Bulma, but highly useful!
5. textfield() - a simple textarea and label

