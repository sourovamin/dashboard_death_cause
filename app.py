import dash
import data
import layout
from callbacks import register_callbacks

# Define the app
app = dash.Dash(__name__)
server = app.server

# Define the layout
app.layout = layout.main_lo

# Register the callbacks
register_callbacks(app, data)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

