import streamlit as st
import pandas as pd
import seaborn as sns  
import matplotlib.pyplot as plt
from sklearn import datasets


def app():
    st.title('Data')
    st.write("This is the `Data` page of the multi-page app.")


    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['class'] = pd.Series(iris.target).map({0: "setosa", 1: "versicolor", 2: "virginica"})


    sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='class', data=df)
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Sepal Length vs Sepal Width')
    st.pyplot()
if __name__ == '__main__':
    app()