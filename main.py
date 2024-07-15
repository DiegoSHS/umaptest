"""This script creates a webapp with streamlit that uses umap to plot a random dataset."""
from threading import _RLock
from matplotlib import pyplot as plt
from numpy.random import rand
import streamlit as st
from umap import umap_


def main():
    """This function runs UMAP on a random dataset and plots the results."""
    menssage = """
    Este es un ejemplo de un plot de UMAP
    creado para una expo de muestra, la base de código
    es propiedad de CADELmx
    """
    st.header("UMAP plot")
    st.write(menssage)
    data = rand(100, 10)
    reducer = umap_.UMAP()
    embedding = reducer.fit_transform(data)
    with _RLock() as _:
        figure, axes = plt.subplots()
        axes.set_title("UMAP plot")
        axes.scatter(embedding[:, 0], embedding[:, 1])
        st.pyplot(figure)
    st.write("Codigo de esta webapp:")
    st.code(to_string())


def to_string():
    """This function returns the code of the main function as a string."""
    with open(file="main.py", mode="r", encoding='utf-8') as file:
        return file.read()


main()
