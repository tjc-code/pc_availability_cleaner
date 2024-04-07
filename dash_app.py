from dash import Dash, html, dcc, Input, Output, callback
from cleaner import clean_dataframe
import io
import pandas as pd
import base64

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Do you want to remove people who haven't filled in their availability on Play Cricket?"
        ),
        dcc.Upload(
            html.Div(
                [html.A("click here to upload xlsx file")],
                style={
                    "width": "50%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
            ),
            id="file-upload",
        ),
        dcc.Download(id="file-download"),
    ]
)


@callback(
    Output("file-download", "data"),
    Input("file-upload", "filename"),
    Input("file-upload", "contents"),
    prevent_initial_call=True,
)
def upload_and_download_file(file_name, file_contents):
    if file_contents is not None:
        _, content_string = file_contents.split(",")
        decoded_content = base64.b64decode(content_string)

        df = pd.read_excel(io.BytesIO(decoded_content))
        cleaned_df = clean_dataframe(df, file_name)

        output_file_name = f"cleaned_{file_name}"
        cleaned_df.to_excel(output_file_name, index=False)

        return dcc.send_file(output_file_name)
    return None


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0")
