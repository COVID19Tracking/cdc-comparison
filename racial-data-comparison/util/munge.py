state_abbrevs = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

state_full_names = dict([(value, key) for key, value in state_abbrevs.items()])

cdc_races = {
    'Non-Hispanic White':'white', 
    'Non-Hispanic Black':'black',
    'Non-Hispanic American Indian or Alaska Native':'AIAN',
    'Non-Hispanic Asian':'asian',
    'Non-Hispanic Native Hawaiian or Other Pacific Islander':'NHPI',
    'Non-Hispanic More than one race':'multiracial', 
    'Hispanic or Latino':'latinx', 
    'Unknown':'unknown'}

crdt_to_cdc_races = {
    'deaths_white':'white', 
    'deaths_black':'black',
    'deaths_aian':'AIAN',
    'deaths_asian':'asian',
    'deaths_nhpi':'NHPI',
    'deaths_multiracial':'multiracial', 
    'deaths_latinx':'latinx', 
    'deaths_unknown':'unknown',
    'deaths_hispanic':'hispanic',
    'deaths_nonhispanic':'nonhispanic',
    'deaths_other':'other'}

palette = {
    "pink":"#DB3069",
    "grey":"#313638",
    "lightgrey":"#d3d3d3",
    "gold":"#F5D547",
    "aqua":"#C1FFE8",
    "royal":"#1446A0",
    "fox":"#F06543",
    "red":"#FC3903",
    "green":"#7AE667"
}

def max_print(df):
    """Print the entire contents of a dataframe in Jupyter"""
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
         display(HTML(df.to_html()))