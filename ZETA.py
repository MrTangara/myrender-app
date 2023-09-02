#############################PACKAGES#################################################
from dash import dash, dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_extensions as de
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


###################################################################################
# scop= ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
#        "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('projetzeta-f9b54f86c984.json', scop)
# client = gspread.authorize(creds)

##############################################################################################
###################################### chargement de la base de donnees ######################

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("MOH.json", scope)

client = gspread.authorize(creds)

sheet1 = client.open("ZETA").sheet1
sheet2 = client.open("ZETA").worksheet("classe8")
sheet3 = client.open("ZETA").worksheet("classe9")
sheet4 = client.open("ZETA").worksheet("TRIMESTRE1")
sheet5 = client.open("ZETA").worksheet("TRIMESTRE2")
sheet6 = client.open("ZETA").worksheet("TRIMESTRE2")

df1 = sheet1.get_all_records()
df1 = pd.DataFrame(df1)

df2 = sheet2.get_all_records()
df2 = pd.DataFrame(df2)

df3 = sheet3.get_all_records()
df3 = pd.DataFrame(df3)

df4 = sheet4.get_all_records()
df4 = pd.DataFrame(df4)

df5 = sheet5.get_all_records()
df5 = pd.DataFrame(df5)

df6 = sheet6.get_all_records()
df6 = pd.DataFrame(df6)

##################################################################################################################33

#app = dash.Dash(external_stylesheets=[dbc.themes.MATERIA], meta_tags=[
      #  {"name": "viewport", "content": "width=device-width, initial-scale=1"})
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

card_color = 'red'
marge = '15px'
titre_principal = {'text-align': 'center', 'color': 'black', 'background': 'maroon',
                   'border-radius': '2px', 'font-family': 'Monospace', 'font-weignt': 'bold'}
style_card = { 'background-color': '#ebf5fb', 'font-family': 'Garamond', #'text-align': 'center',
            'color': 'black', 'font-size': '1em', 'font-weight': 'bold'}

###########################################################################################################
#                                       TITLE                                                            #
############################################################################################################
dash_title = dbc.Row(
    dbc.Col(
        dbc.Card([
            dbc.CardBody(html.H2("MON ECOLE"),
                         style=titre_principal)
        ])
    ),
    style={'position': 'fixed', 'left': 0, 'right': 0, 'top': 0}
)

#######################################################################################################
#                                      SIDE BAR                                                         #
#######################################################################################################
app = dash.Dash(external_stylesheets=[dbc.themes.MATERIA],suppress_callback_exceptions=True)
dropdown = html.Div(
    [html.Label("« L'éducation est l'arme la plus puissante que l'on puisse utiliser pour changer le monde »",
               style={'margin-left': '12px', 'margin-top': '10px'
                      }),
            html.Hr(),
     dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(
                    "accueil",active=True, href="/"
                ),
                dbc.DropdownMenuItem(
                    "classe 7",active=True, href="/page-1"
                ),
                dbc.DropdownMenuItem(
                    "classe 8",active=True, href="/page-2"
                ),
                dbc.DropdownMenuItem(
                    "classe 9",active=True,
                    href="/page-3",

                ),
            ],
            label="Menu", menu_variant="dark",
        ),
    ], style={
    'position': 'fixed',
    'top': 0,
    'bottom': 0,
    'width': '200px',
    'background': '#ebf5fb',
    'padding-top': '100px'
}
)


###################################################################################################################
#                                          page accueil                                                      #
###################################################################################################################

accueil = html.Div(
    dbc.Row([
        dbc.Col([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/im1.jpg", "caption":"UNE ECOLE","img_style":{"max-height":"300px"}},
                    {"key": "2", "src": "/assets/education_africa_higher_ed_nurses-996x567.jpg","caption":"D'EXCELLENCE","img_style":{"max-height":"300px"}},
                    {"key": "3", "src":"/assets/im2.jpg", "caption":"A VOTRE SERVICE", "img_style":{"max-height": "300px"}},
                ],
                controls=False,
                indicators=False,
                interval=1000,
                ride="carousel",
            )
        ])
    ], justify="center")

)

###################################################################################################################3
############################################## SITUATION GLOBALE ####################################################


classe_9 =  html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                    [
                        dash_table.DataTable(df1.to_dict('records'),
                                             [{"name": i, "id": i} for i in df1.columns[1:]],
                style_cell_conditional=[
                        {'if': {'column_id': c},'textAlign': 'left'} for c in ['PRENOM', 'NOM']
                    ],
                    style_data={
                        'color': 'black','backgroundColor': 'white'
                    },
                    style_data_conditional=[
                        {'if': {'row_index': 'odd'},'backgroundColor': 'rgb(220, 220, 220)',}
                    ],
                    style_header={
                        'backgroundColor': 'rgb(210, 210, 210)','color': 'black','fontWeight': 'bold'
                    },id='tbl'),
                        dbc.Alert(id='tbl_out'),
            ],title="CLASSE 7 année",),
    dbc.AccordionItem(
                        [
                            dbc.Label('Click a cell in the table:'),
                            dash_table.DataTable(df2.to_dict('records'), [{"name": i, "id": i} for i in df2.columns], id='tbl'),
                            dbc.Alert(id='tbl_out'),
                ],title="CLASSE 8 année",),
    dbc.AccordionItem(
                        [
                            dbc.Label('Click a cell in the table:'),
                            dash_table.DataTable(df3.to_dict('records'), [{"name": i, "id": i} for i in df3.columns], id='tbl'),
                            dbc.Alert(id='tbl_out'),
                ],title="CLASSE 9 année",),

                    ])
    )



classe_7 =  html.Div([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H3("CLASSE 7ième ANNEE", style={'color': 'blue', 'font-size': '40px','text-align': 'center'})),
            dbc.CardBody([ html.Label("MATRICULE  : "),
                dcc.Input(id="input-eleve-id",type='number', placeholder='MATRICULE',debounce=True),
                html.Hr(),
                html.P(["Prenom:  ",html.Code(id="output-prenom")]),
                html.P(["Nom:  ",html.Code(id="output-nom")]),

            ])
        ], style=style_card)),
    ], style={'margin': '5px'}),
dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Label("SELECTIONEZ UNE UE")),
                            dbc.CardBody([dcc.Dropdown(
                        options=[{"label": i, "value":i} for i in df1.columns[4:8].tolist()],
                        id ="Mat_SC_7" , style={"width":"100%"}),
                    ],style={'text-align': 'center', 'margin': marge})
                        ])
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Label("Selectionez une periode")),
                            dbc.CardBody([dcc.Dropdown(
                        options=[{"label": i, "value":i} for i in ["TRIMESTRE 1", "TRIMESTRE 2", "TRIMESTRE 3"]],
                        id ="PERIODE_7",value="TRIMESTRE 1", style={"width":"100%"}),
                    ],style={'text-align': 'center', 'margin': marge})
                        ])
                    )
                ]),
                dbc.Row(
                    dbc.Col(
                       dbc.Card([
                            dbc.CardHeader(html.H3("NOTE DISPONIBLE", style={'color': 'yelow', 'font-size': '20px','text-align': 'center'})),
                            dbc.CardBody([
                                html.P(["NOTE 1:  ", html.Code(id="N1_7")]),
                                html.P(["NOTE 2:  ", html.Code(id="N2_7")]),
                                html.P(["NOTE DE CLASSE:  ",html.Code(id="NCL_7")]),
                                html.P(["NOTE COMPO:  ",html.Code(id="NCP_7")]),
                                html.P(["NOTE GENERALE:  ",html.Code(id="NG_7")])
                           ])
                        ])
                    )
                    )
                ]
                , title="Mathematiques et Science"
            ),
            dbc.AccordionItem(
            [
                            dbc.Row([
                                dbc.Col(
                                    dbc.Card([
                                        dbc.CardHeader(html.Label("SELECTIONEZ UNE UE")),
                                        dbc.CardBody([dcc.Dropdown(
                                    options=[{"label": i, "value":i} for i in df1.columns[8:11].tolist()],
                                    id ="FR_ANG_7" , style={"width":"100%"}),
                                ],style={'text-align': 'center', 'margin': marge})
                                    ])
                                ),
                                dbc.Col(
                                    dbc.Card([
                                        dbc.CardHeader(html.Label("Selectionez une periode")),
                                        dbc.CardBody([dcc.Dropdown(
                                    options=[{"label": i, "value":i} for i in ["TRIMESTRE 1", "TRIMESTRE 2", "TRIMESTRE 3"]],
                                    id ="PERIODE_7_L",value="TRIMESTRE 1", style={"width":"100%"}),
                                ],style={'text-align': 'center', 'margin': marge})
                                    ])
                                )
                            ]),
                            dbc.Row(
                                dbc.Col(
                                   dbc.Card([
                                        dbc.CardHeader(html.H3("NOTE DISPONIBLE", style={'color': 'yelow', 'font-size': '20px','text-align': 'center'})),
                                        dbc.CardBody([
                                            html.P(["NOTE 1:  ", html.Code(id="N1_7_L")]),
                                            html.P(["NOTE 2:  ", html.Code(id="N2_7_L")]),
                                            html.P(["NOTE DE CLASSE:  ",html.Code(id="NCL_7_L")]),
                                            html.P(["NOTE COMPO:  ",html.Code(id="NCP_7_L")]),
                                            html.P(["NOTE GENERALE:  ",html.Code(id="NG_7_L")])
                                       ])
                                    ])
                                )
                                )
                            ]

                , title="LANGUES et Litterature"
            ),
            dbc.AccordionItem(
                [
                                            dbc.Row([
                                                dbc.Col(
                                                    dbc.Card([
                                                        dbc.CardHeader(html.Label("SELECTIONEZ UNE UE")),
                                                        dbc.CardBody([dcc.Dropdown(
                                                    options=[{"label": i, "value":i} for i in df1.columns[11:15].tolist()],
                                                    id ="ART_7" , style={"width":"100%"}),
                                                ],style={'text-align': 'center', 'margin': marge})
                                                    ])
                                                ),
                                                dbc.Col(
                                                    dbc.Card([
                                                        dbc.CardHeader(html.Label("Selectionez une periode")),
                                                        dbc.CardBody([dcc.Dropdown(
                                                    options=[{"label": i, "value":i} for i in ["TRIMESTRE 1", "TRIMESTRE 2", "TRIMESTRE 3"]],
                                                    id ="PERIODE_7_S",value="TRIMESTRE 1", style={"width":"100%"}),
                                                ],style={'text-align': 'center', 'margin': marge})
                                                    ])
                                                )
                                            ]),
                                            dbc.Row(
                                                dbc.Col(
                                                   dbc.Card([
                                                        dbc.CardHeader(html.H3("NOTE DISPONIBLE", style={'color': 'yelow', 'font-size': '20px','text-align': 'center'})),
                                                        dbc.CardBody([
                                                            html.P(["NOTE 1:  ", html.Code(id="N1_7_S")]),
                                                            html.P(["NOTE 2:  ", html.Code(id="N2_7_S")]),
                                                            html.P(["NOTE DE CLASSE:  ",html.Code(id="NCL_7_S")]),
                                                            html.P(["NOTE COMPO:  ",html.Code(id="NCP_7_S")]),
                                                            html.P(["NOTE GENERALE:  ",html.Code(id="NG_7_S")])
                                                       ])
                                                    ])
                                                )
                                                )
                                            ]
                , title="Art,Culture ET SPORT"
            ),
        ],
        start_collapsed=True,
    ),

])

classe_8 =  html.Div([
                        dbc.Row([
                            dbc.Col(dbc.Card([
                                dbc.CardHeader(html.H3("CLASSE 8ième ANNEE", style={'color': 'blue', 'font-size': '40px','text-align': 'center'})),
                                dbc.CardBody([ html.Label("MATRICULE  : "),
                                    dcc.Input(id="input-eleve-id-8",type='number', placeholder='MATRICULE',debounce=True),
                                    html.Hr(),
                                    html.P(["Prenom:  ",html.Code(id="output-prenom-8")]),
                                    html.P(["Nom:  ",html.Code(id="output-nom-8")]),

                                ])
                            ], style=style_card)),
                        ], style={'margin': '5px'}),
                    dbc.Accordion(
                            [
                                dbc.AccordionItem(
                                    [
                                    dbc.Row([
                                        dbc.Col(
                                            dbc.Card([
                                                dbc.CardHeader(html.Label("SELECTIONEZ UNE UE")),
                                                dbc.CardBody([dcc.Dropdown(
                                            options=[{"label": i, "value":i} for i in df2.columns[4:8].tolist()],
                                            id ="Mat_SC_8" , style={"width":"100%"}),
                                        ],style={'text-align': 'center', 'margin': marge})
                                            ])
                                        ),
                                        dbc.Col(
                                            dbc.Card([
                                                dbc.CardHeader(html.Label("Selectionez une periode")),
                                                dbc.CardBody([dcc.Dropdown(
                                            options=[{"label": i, "value":i} for i in ["TRIMESTRE 1", "TRIMESTRE 2", "TRIMESTRE 3"]],
                                            id ="PERIODE_8",value="TRIMESTRE 1", style={"width":"100%"}),
                                        ],style={'text-align': 'center', 'margin': marge})
                                            ])
                                        )
                                    ]),
                                    dbc.Row(
                                        dbc.Col(
                                           dbc.Card([
                                                dbc.CardHeader(html.H3("NOTE DISPONIBLE", style={'color': 'yelow', 'font-size': '20px','text-align': 'center'})),
                                                dbc.CardBody([
                                                    html.P(["NOTE 1:  ", html.Code(id="N1_8")]),
                                                    html.P(["NOTE 2:  ", html.Code(id="N2_8")]),
                                                    html.P(["NOTE DE CLASSE:  ",html.Code(id="NCL_8")]),
                                                    html.P(["NOTE COMPO:  ",html.Code(id="NCP_8")]),
                                                    html.P(["NOTE GENERALE:  ",html.Code(id="NG_8")])
                                               ])
                                            ])
                                        )
                                        )
                                    ]
                                    , title="Mathematiques et Science"
                                ),
                                dbc.AccordionItem(
                                [
                                                dbc.Row([
                                                    dbc.Col(
                                                        dbc.Card([
                                                            dbc.CardHeader(html.Label("SELECTIONEZ UNE UE")),
                                                            dbc.CardBody([dcc.Dropdown(
                                                        options=[{"label": i, "value":i} for i in df1.columns[8:11].tolist()],
                                                        id ="FR_ANG_8" , style={"width":"100%"}),
                                                    ],style={'text-align': 'center', 'margin': marge})
                                                        ])
                                                    ),
                                                    dbc.Col(
                                                        dbc.Card([
                                                            dbc.CardHeader(html.Label("Selectionez une periode")),
                                                            dbc.CardBody([dcc.Dropdown(
                                                        options=[{"label": i, "value":i} for i in ["TRIMESTRE 1", "TRIMESTRE 2", "TRIMESTRE 3"]],
                                                        id ="PERIODE_8_L",value="TRIMESTRE 1", style={"width":"100%"}),
                                                    ],style={'text-align': 'center', 'margin': marge})
                                                        ])
                                                    )
                                                ]),
                                                dbc.Row(
                                                    dbc.Col(
                                                       dbc.Card([
                                                            dbc.CardHeader(html.H3("NOTE DISPONIBLE", style={'color': 'yelow', 'font-size': '20px','text-align': 'center'})),
                                                            dbc.CardBody([
                                                                html.P(["NOTE 1:  ", html.Code(id="N1_8_L")]),
                                                                html.P(["NOTE 2:  ", html.Code(id="N2_8_L")]),
                                                                html.P(["NOTE DE CLASSE:  ",html.Code(id="NCL_8_L")]),
                                                                html.P(["NOTE COMPO:  ",html.Code(id="NCP_8_L")]),
                                                                html.P(["NOTE GENERALE:  ",html.Code(id="NG_8_L")])
                                                           ])
                                                        ])
                                                    )
                                                    )
                                                ]

                                    , title="LANGUES et Litterature"
                                ),
                                dbc.AccordionItem(
                                    [
                                                                dbc.Row([
                                                                    dbc.Col(
                                                                        dbc.Card([
                                                                            dbc.CardHeader(html.Label("SELECTIONEZ UNE UE")),
                                                                            dbc.CardBody([dcc.Dropdown(
                                                                        options=[{"label": i, "value":i} for i in df2.columns[11:15].tolist()],
                                                                        id ="ART_7" , style={"width":"100%"}),
                                                                    ],style={'text-align': 'center', 'margin': marge})
                                                                        ])
                                                                    ),
                                                                    dbc.Col(
                                                                        dbc.Card([
                                                                            dbc.CardHeader(html.Label("Selectionez une periode")),
                                                                            dbc.CardBody([dcc.Dropdown(
                                                                        options=[{"label": i, "value":i} for i in ["TRIMESTRE 1", "TRIMESTRE 2", "TRIMESTRE 3"]],
                                                                        id ="PERIODE_8_S",value="TRIMESTRE 1", style={"width":"100%"}),
                                                                    ],style={'text-align': 'center', 'margin': marge})
                                                                        ])
                                                                    )
                                                                ]),
                                                                dbc.Row(
                                                                    dbc.Col(
                                                                       dbc.Card([
                                                                            dbc.CardHeader(html.H3("NOTE DISPONIBLE", style={'color': 'yelow', 'font-size': '20px','text-align': 'center'})),
                                                                            dbc.CardBody([
                                                                                html.P(["NOTE 1:  ", html.Code(id="N1_8_S")]),
                                                                                html.P(["NOTE 2:  ", html.Code(id="N2_8_S")]),
                                                                                html.P(["NOTE DE CLASSE:  ",html.Code(id="NCL_8_S")]),
                                                                                html.P(["NOTE COMPO:  ",html.Code(id="NCP_8_S")]),
                                                                                html.P(["NOTE GENERALE:  ",html.Code(id="NG_8_S")])
                                                                           ])
                                                                        ])
                                                                    )
                                                                    )
                                                                ]
                                    , title="Art,Culture ET SPORT"
                                ),
                            ],
                            start_collapsed=True,
                        ),

                    ])


#############################################################################################################
#                                    CONTAINER ET LAYOUT                                                    #
##############################################################################################################

container = html.Div(style={'position':'fixed', 'top':0,'left':0,'right':0,'bottom':0,'background':"#FFFFFF"})
content = html.Div(id='contenu', style={'margin-left':'200px','padding-top':'100px'})


app.layout = html.Div(children=[
    container,
    dropdown,
    dcc.Location(id='url'),
    content,
    dash_title
], style={'background':'black'})



###########################################################################################################
#                                            COLLBACK                                                      #
#############################################################################################################

@app.callback(
                Output(component_id='contenu', component_property='children'),
                Input(component_id='url', component_property='pathname'),

)
def load_page(lien):
    if lien=='/':
        return accueil
    elif lien=='/page-1':
        return classe_7
    elif lien=='/page-2':
        return classe_8
    elif lien=='/page-3':
        return classe_9
    return "Error 404 : Page not found !"


@app.callback(
    Output('output-prenom', 'children'),
    Output('output-nom', 'children'),
    Input('input-eleve-id', 'value')
)
def alpha(V1):
    if V1 is None:
        return '', ''
    filtered_data = df1[df1['ID'] == V1]
    if filtered_data.empty:
        return 'Aucun résultat trouvé', 'Aucun résultat trouvé'
    prenom = filtered_data.iloc[0]['PRENOM']
    nom = filtered_data.iloc[0]['NOM']
    return prenom, nom

@app.callback(
    Output('output-prenom-8', 'children'),
    Output('output-nom-8', 'children'),
    Input('input-eleve-id-8', 'value')
)
def alpha_8(V1):
    if V1 is None:
        return '', ''
    filtered_data = df2[df2['ID'] == V1]
    if filtered_data.empty:
        return 'Aucun résultat trouvé', 'Aucun résultat trouvé'
    prenom = filtered_data.iloc[0]['PRENOM']
    nom = filtered_data.iloc[0]['NOM']
    return prenom, nom


@app.callback(
    Output('N1_7', 'children'),
    Output('N2_7', 'children'),
    Output('NCL_7', 'children'),
    Output('NCP_7', 'children'),
    Output('NG_7', 'children'),
    Input('input-eleve-id', 'value'),
    Input('Mat_SC_7', 'value'),
    Input('PERIODE_7', 'value')
)
def beta( V2, V3, V4 ):
    if V2 is None or V3 is None:
        return '', '' , "", "", ""
    VAR1 = df4[df4["ID"] == V2]
    VAR2 = V3
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[4:8].tolist()[0] and V4 == "TRIMESTRE 1" :
        return VAR1.iloc[0]['NOTE_MATH_1'],VAR1.iloc[0]['NOTE_MATH_2'],VAR1.iloc[0]['NOTE_CLASSE_MATH'],VAR1.iloc[0]['NOTE_COMPO_MATH'],VAR1.iloc[0]['NOTE_MATH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[1] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_PH_1'], VAR1.iloc[0]['NOTE_PH_2'], VAR1.iloc[0]['NOTE_CLASSE_PH'], VAR1.iloc[0]['NOTE_COMPO_PH'], VAR1.iloc[0]['NOTE_PH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[2] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_CH_1'], VAR1.iloc[0]['NOTE_CH_2'], VAR1.iloc[0]['NOTE_CLASSE_CH'], VAR1.iloc[0]['NOTE_COMPO_CH'], VAR1.iloc[0]['NOTE_CH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[3] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_BIO_1'], VAR1.iloc[0]['NOTE_BIO_2'], VAR1.iloc[0]['NOTE_CLASSE_BIO'], VAR1.iloc[0]['NOTE_COMPO_BIO'], VAR1.iloc[0]['NOTE_BIO_1'],
    VAR3 = df5[df5["ID"] == V2]
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[4:8].tolist()[0] and V4 == "TRIMESTRE 2" :
        return VAR3.iloc[0]['NOTE_MATH_1'],VAR3.iloc[0]['NOTE_MATH_2'],VAR3.iloc[0]['NOTE_CLASSE_MATH'],VAR3.iloc[0]['NOTE_COMPO_MATH'],VAR3.iloc[0]['NOTE_MATH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[1] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_PH_1'], VAR3.iloc[0]['NOTE_PH_2'], VAR3.iloc[0]['NOTE_CLASSE_PH'], VAR3.iloc[0]['NOTE_COMPO_PH'], VAR3.iloc[0]['NOTE_PH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[2] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_CH_1'], VAR3.iloc[0]['NOTE_CH_2'], VAR3.iloc[0]['NOTE_CLASSE_CH'], VAR3.iloc[0]['NOTE_COMPO_CH'], VAR3.iloc[0]['NOTE_CH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[3] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_BIO_1'], VAR3.iloc[0]['NOTE_BIO_2'], VAR3.iloc[0]['NOTE_CLASSE_BIO'], VAR3.iloc[0]['NOTE_COMPO_BIO'], VAR3.iloc[0]['NOTE_BIO_1'],
    VAR4 = df6[df6["ID"] == V2]
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[4:8].tolist()[0] and V4 == "TRIMESTRE 3" :
        return VAR4.iloc[0]['NOTE_MATH_1'],VAR4.iloc[0]['NOTE_MATH_2'],VAR4.iloc[0]['NOTE_CLASSE_MATH'],VAR4.iloc[0]['NOTE_COMPO_MATH'],VAR4.iloc[0]['NOTE_MATH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[1] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_PH_1'], VAR4.iloc[0]['NOTE_PH_2'], VAR4.iloc[0]['NOTE_CLASSE_PH'], VAR4.iloc[0]['NOTE_COMPO_PH'], VAR4.iloc[0]['NOTE_PH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[2] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_CH_1'], VAR4.iloc[0]['NOTE_CH_2'], VAR4.iloc[0]['NOTE_CLASSE_CH'], VAR4.iloc[0]['NOTE_COMPO_CH'], VAR4.iloc[0]['NOTE_CH_1'],
    elif VAR2 == df1.columns[4:8].tolist()[3] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_BIO_1'], VAR4.iloc[0]['NOTE_BIO_2'], VAR4.iloc[0]['NOTE_CLASSE_BIO'], VAR4.iloc[0]['NOTE_COMPO_BIO'], VAR4.iloc[0]['NOTE_BIO_1'],


############################
# CALLBACK FRANCAIS ANGLAIS #
############################

@app.callback(
    Output('N1_7_L', 'children'),
    Output('N2_7_L', 'children'),
    Output('NCL_7_L', 'children'),
    Output('NCP_7_L', 'children'),
    Output('NG_7_L', 'children'),
    Input('input-eleve-id', 'value'),
    Input('FR_ANG_7', 'value'),
    Input('PERIODE_7_L', 'value')
)
def gama( V2, V3, V4 ):
    if V2 is None or V3 is None:
        return '', '' , "", "", ""
    VAR1 = df4[df4["ID"] == V2]
    VAR2 = V3
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[8:11].tolist()[0] and V4 == "TRIMESTRE 1" :
        return VAR1.iloc[0]['NOTE_FR_1'],VAR1.iloc[0]['NOTE_FR_2'],VAR1.iloc[0]['NOTE_CLASSE_FR'],VAR1.iloc[0]['NOTE_COMPO_FR'],VAR1.iloc[0]['NOTE_FR_1'],
    elif VAR2 == df1.columns[8:11].tolist()[1] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_ANG_1'], VAR1.iloc[0]['NOTE_ANG_2'], VAR1.iloc[0]['NOTE_CLASSE_ANG'], VAR1.iloc[0]['NOTE_COMPO_ANG'], VAR1.iloc[0]['NOTE_ANG_1'],
    elif VAR2 == df1.columns[8:11].tolist()[2] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_DQ_1'], VAR1.iloc[0]['NOTE_DQ_2'], VAR1.iloc[0]['NOTE_CLASSE_DQ'], VAR1.iloc[0]['NOTE_COMPO_DQ'], VAR1.iloc[0]['NOTE_DQ_1'],
    VAR3 = df5[df5["ID"] == V2]
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[8:11].tolist()[0] and V4 == "TRIMESTRE 2" :
        return VAR3.iloc[0]['NOTE_FR_1'],VAR3.iloc[0]['NOTE_FR_2'],VAR3.iloc[0]['NOTE_CLASSE_FR'],VAR3.iloc[0]['NOTE_COMPO_FR'],VAR3.iloc[0]['NOTE_FR_1'],
    elif VAR2 == df1.columns[8:11].tolist()[1] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_ANG_1'], VAR3.iloc[0]['NOTE_ANG_2'], VAR3.iloc[0]['NOTE_CLASSE_ANG'], VAR3.iloc[0]['NOTE_COMPO_ANG'], VAR3.iloc[0]['NOTE_ANG_1'],
    elif VAR2 == df1.columns[8:11].tolist()[2] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_DQ_1'], VAR3.iloc[0]['NOTE_DQ_2'], VAR3.iloc[0]['NOTE_CLASSE_DQ'], VAR3.iloc[0]['NOTE_COMPO_DQ'], VAR3.iloc[0]['NOTE_DQ_1'],
    VAR4 = df6[df6["ID"] == V2]
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[8:11].tolist()[0] and V4 == "TRIMESTRE 3" :
        return VAR4.iloc[0]['NOTE_FR_1'],VAR4.iloc[0]['NOTE_FR_2'],VAR4.iloc[0]['NOTE_CLASSE_FR'],VAR4.iloc[0]['NOTE_COMPO_FR'],VAR4.iloc[0]['NOTE_FR_1'],
    elif VAR2 == df1.columns[8:11].tolist()[1] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_ANG_1'], VAR4.iloc[0]['NOTE_ANG_2'], VAR4.iloc[0]['NOTE_CLASSE_ANG'], VAR4.iloc[0]['NOTE_COMPO_ANG'], VAR4.iloc[0]['NOTE_ANG_1'],
    elif VAR2 == df1.columns[8:11].tolist()[2] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_DQ_1'], VAR4.iloc[0]['NOTE_DQ_2'], VAR4.iloc[0]['NOTE_CLASSE_DQ'], VAR4.iloc[0]['NOTE_COMPO_DQ'], VAR4.iloc[0]['NOTE_DQ_1'],

##############################
# CALLBACK SPORT ART CULTURE #
##############################

@app.callback(
    Output('N1_7_S', 'children'),
    Output('N2_7_S', 'children'),
    Output('NCL_7_S', 'children'),
    Output('NCP_7_S', 'children'),
    Output('NG_7_S', 'children'),
    Input('input-eleve-id', 'value'),
    Input('ART_7', 'value'),
    Input('PERIODE_7_S', 'value')
)
def delta( V2, V3, V4 ):
    if V2 is None or V3 is None:
        return '', '' , "", "", ""
    VAR1 = df4[df4["ID"] == V2]
    VAR2 = V3
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[11:15].tolist()[0] and V4 == "TRIMESTRE 1" :
        return VAR1.iloc[0]['NOTE_ECM_1'],VAR1.iloc[0]['NOTE_ECM_2'],VAR1.iloc[0]['NOTE_CLASSE_ECM'],VAR1.iloc[0]['NOTE_COMPO_ECM'],VAR1.iloc[0]['NOTE_ECM_1'],
    elif VAR2 == df1.columns[11:15].tolist()[1] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_EPS_1'], VAR1.iloc[0]['NOTE_EPS_2'], VAR1.iloc[0]['NOTE_CLASSE_EPS'], VAR1.iloc[0]['NOTE_COMPO_EPS'], VAR1.iloc[0]['NOTE_EPS_1'],
    elif VAR2 == df1.columns[11:15].tolist()[2] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_DES_1'], VAR1.iloc[0]['NOTE_DES_2'], VAR1.iloc[0]['NOTE_CLASSE_DES'], VAR1.iloc[0]['NOTE_COMPO_DES'], VAR1.iloc[0]['NOTE_DES_1'],
    elif VAR2 == df1.columns[11:15].tolist()[3] and V4 == "TRIMESTRE 1":
        return VAR1.iloc[0]['NOTE_COND_1'], VAR1.iloc[0]['NOTE_COND_2'], VAR1.iloc[0]['NOTE_CLASSE_COND'], VAR1.iloc[0]['NOTE_COMPO_COND'], VAR1.iloc[0]['NOTE_COND_1'],
    VAR3 = df5[df5["ID"] == V2]
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[11:15].tolist()[0] and V4 == "TRIMESTRE 2" :
        return VAR3.iloc[0]['NOTE_ECM_1'],VAR3.iloc[0]['NOTE_ECM_2'],VAR3.iloc[0]['NOTE_CLASSE_ECM'],VAR3.iloc[0]['NOTE_COMPO_ECM'],VAR3.iloc[0]['NOTE_ECM_1'],
    elif VAR2 == df1.columns[11:15].tolist()[1] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_EPS_1'], VAR3.iloc[0]['NOTE_EPS_2'], VAR3.iloc[0]['NOTE_CLASSE_EPS'], VAR3.iloc[0]['NOTE_COMPO_EPS'], VAR3.iloc[0]['NOTE_EPS_1'],
    elif VAR2 == df1.columns[11:15].tolist()[2] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_DES_1'], VAR3.iloc[0]['NOTE_DES_2'], VAR3.iloc[0]['NOTE_CLASSE_DES'], VAR3.iloc[0]['NOTE_COMPO_DES'], VAR3.iloc[0]['NOTE_DES_1'],
    elif VAR2 == df1.columns[11:15].tolist()[3] and V4 == "TRIMESTRE 2":
        return VAR3.iloc[0]['NOTE_COND_1'], VAR3.iloc[0]['NOTE_COND_2'], VAR3.iloc[0]['NOTE_CLASSE_COND'], VAR3.iloc[0]['NOTE_COMPO_COND'], VAR3.iloc[0]['NOTE_COND_1'],
    VAR4 = df6[df6["ID"] == V2]
    if VAR1.empty:
        return "","","","","",
    elif VAR2 == df1.columns[11:15].tolist()[0] and V4 == "TRIMESTRE 3" :
        return VAR4.iloc[0]['NOTE_ECM_1'],VAR4.iloc[0]['NOTE_ECM_2'],VAR4.iloc[0]['NOTE_CLASSE_ECM'],VAR4.iloc[0]['NOTE_COMPO_ECM'],VAR4.iloc[0]['NOTE_ECM_1'],
    elif VAR2 == df1.columns[11:15].tolist()[1] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_EPS_1'], VAR4.iloc[0]['NOTE_EPS_2'], VAR4.iloc[0]['NOTE_CLASSE_EPS'], VAR4.iloc[0]['NOTE_COMPO_EPS'], VAR4.iloc[0]['NOTE_EPS_1'],
    elif VAR2 == df1.columns[11:15].tolist()[2] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_DES_1'], VAR4.iloc[0]['NOTE_DES_2'], VAR4.iloc[0]['NOTE_CLASSE_DES'], VAR4.iloc[0]['NOTE_COMPO_DES'], VAR4.iloc[0]['NOTE_DES_1'],
    elif VAR2 == df1.columns[11:15].tolist()[3] and V4 == "TRIMESTRE 3":
        return VAR4.iloc[0]['NOTE_COND_1'], VAR4.iloc[0]['NOTE_COND_2'], VAR4.iloc[0]['NOTE_CLASSE_COND'], VAR4.iloc[0]['NOTE_COMPO_COND'], VAR4.iloc[0]['NOTE_COND_1'],





if __name__ == '__main__':
    app.run_server(debug=True,port=700)
