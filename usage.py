import dash_katex
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    html.Div("Expression Input:"),
    dcc.Input(id='input-latex-expression'),

    html.Div("Display Mode:"),
    dcc.RadioItems(
        id='radio-item-display-mode',
        options=[
            {'label': "Display/Equation Mode", 'value': 'Display'},
            {'label': "Inline Mode", 'value': 'Inline'}
        ],
        value = 'Inline',
    ),


    html.Div("Throw on error:"),
    dcc.RadioItems(
        id='radio-item-throw-on-error',
        options=[
            {'label': "Throw Errors", 'value': "Throw"},
            {'label': "Pass Error", 'value': "Pass"}
        ],
        value = "Pass",
    ),

    html.Div('Here is some latex:'),
    dash_katex.DashKatex(
        id='katex',
        expression="",
        displayMode = True,
        throwOnError = False,
    )
])


@app.callback(Output('katex', 'expression'),
              [Input('input-latex-expression', 'value')])
def updateExpression(value):
    return str(value)


@app.callback(Output('katex', 'displayMode'),
              [Input('radio-item-display-mode', 'value')])
def updateDisplayMode(value):
    return value == "Display"


@app.callback(Output('katex', 'throwOnError'),
              [Input('radio-item-throw-on-error', 'value')])
def updatethrowOnError(value):
    return value == "Throw"


if __name__ == '__main__':
    app.run_server(debug=True)
