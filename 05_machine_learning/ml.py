import category_encoders as ce
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

if __name__ == '__main__':
    colnames = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety',
                'class']
    X = pd.read_csv('car.data', names=colnames, header=None)

    # prediction
    y = X.buying
    X.drop(['buying'], axis=1, inplace=True)

    # unused
    X.drop(['persons'], axis=1, inplace=True)

    rfc_model = RandomForestClassifier(n_estimators=10, random_state=0)
    # encode data
    encoder = ce.OrdinalEncoder(cols=X.columns)
    X = encoder.fit_transform(X)
    accuracy = cross_val_score(rfc_model, X, y, cv=5)
    print("mean accuracy: {0:0.4f}".format(accuracy.mean()))

    # fit the model
    rfc_model.fit(X, y)

    predict = [['high', '4', 'big', 'high', 'good']]
    predict_df = pd.DataFrame(columns=X.columns, data=predict)
    x_predict = encoder.transform(predict_df)
    y_predict = rfc_model.predict(x_predict)
    print(y_predict[0])
