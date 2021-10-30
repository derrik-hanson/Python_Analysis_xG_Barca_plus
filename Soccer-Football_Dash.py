# How Data Explains the Soccer World


import dash 
import dash_core_commponents as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize Dash App --------
app = dash.Dash(__name__)

# Dataframe to be used
# df = pd.read_csv('csv_filename')

# Layout -----------------------
app.layout = html.Div({
	html.H6("This is only the main structure for a Dash app... For Now"),
	html.Div(["Input Placeholder",
		dcc.Input(id='input-1', value='initial value', type='text')
		]),
	html.Br(),
	html.Div(id='output-1'),
})

# CallBacks --------------------
@app.callback(
	Output(component_id='output-1', component_property='children'),
	Input(component_id='input-1', component_property='value')
)
def update_output_div(input_value):
	return	'output: {}'.format(input_value)


# Execution --------------------
if __name__ == '__main__':
	app.run_server(debug-True)