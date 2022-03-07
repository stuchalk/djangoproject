import requests
csmiles = 'CCCC'

"""prints the URL to the pubchem rest API for that compound"""
API_URL_json = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/json"
print(API_URL_json)

"""Use the request package to access the data at that URL"""
query_json = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/json")
# print(query_json)
# print(query_json.text)
# print(query_json.json())


"""Use the request package to access the synonyms for the compound"""
synonym_query_json = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/synonyms/json")
# print(synonym_query_json.json())

synonyms = synonym_query_json.json()["InformationList"]["Information"][0]["Synonym"]
# print(synonyms)
