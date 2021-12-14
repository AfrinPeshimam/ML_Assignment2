import pickle
def predict(df):
    df['age_married']= df['age']- df['yrs_married']
    df['mar_child']= df['yrs_married']- df['children']
    filename = 'finalized_model.pickle'
    loaded_model = pickle.load(open(filename, 'rb'))
    prediction=loaded_model.predict(df)
    if prediction==0:
        return 'No Affair'
    else:
        return 'Affair'
