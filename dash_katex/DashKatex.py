# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashKatex(Component):
    """A DashKatex component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- expression (string; optional): Expression to be rendered
- displayMode (boolean; optional): If true the math will be rendered in display mode, which will put the
math in display style (so \int and \sum are large, for example), and
will center the math on the page on its own line. If false the math
will be rendered in inline mode. (default: false)
- throwOnError (boolean; optional): If true (the default), KaTeX will throw a ParseError when it encounters
an unsupported command or invalid LaTeX. If false, KaTeX will render
unsupported commands as text, and render invalid LaTeX as its source
code with hover text giving the error, in the color given by errorColor.
- errorColor (string; optional): A color string given in the format "#XXX" or "#XXXXXX". This option
determines the color that unsupported commands and invalid LaTeX are
rendered in when throwOnError is set to false. (default: #cc0000)
- macros (string; optional): A collection of custom macros. Each macro is a property with a name
 like \name (written "\\name" in JavaScript) which maps to a string
 that describes the expansion of the macro, or a function that accepts
 an instance of MacroExpander as first argument and returns the
 expansion as a string.

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, expression=Component.UNDEFINED, displayMode=Component.UNDEFINED, throwOnError=Component.UNDEFINED, errorColor=Component.UNDEFINED, macros=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'expression', 'displayMode', 'throwOnError', 'errorColor', 'macros']
        self._type = 'DashKatex'
        self._namespace = 'dash_katex'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'expression', 'displayMode', 'throwOnError', 'errorColor', 'macros']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashKatex, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('DashKatex(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'DashKatex(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
