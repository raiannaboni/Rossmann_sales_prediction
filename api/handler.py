import pickle
import pandas as pd 
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann

# Loading model
model = pickle.load(open('/home/raianna/Documentos/Repos/ds_em_producao/model/model_rossmann.pkl', 'rb'))

# initialize API
app = Flask(__name__)

@app.route('/rossmann/predict', methods=['POST']) #rota, url que vai receber a request, aí vai rodar a função abaixo da request
def rossmann_predict():
    test_json = request.get_json() #request
    
    # Teste se o dado realmente veio na request
    if test_json: #se tiver dado - conversão do json em DF
        
        if isinstance(test_json, dict): #único exemplo
            test_raw = pd.DataFrame(teste_json, index=[0]) #vai funcionar se tiver uma única linha
            
        else: #exemplos múltiplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate Rossmann class
        pipeline = Rossmann()
        
        # Data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # Feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # Data preparation
        df3 = pipeline.data_preparation(df2)
        
        # Prediction
        df_response = pipeline.get_prediction(model, test_raw, df3) # vai devolver os dados originais para a pessoa de interesse, e os dados modificados serão utilizados no modelo
        
        return df_response
        
    else:
        return Response('{}', status=200, mimetype='application/json') #vazio, porque não existe

if __name__ == '__main__':
    app.run('0.0.0.0') #local
    
